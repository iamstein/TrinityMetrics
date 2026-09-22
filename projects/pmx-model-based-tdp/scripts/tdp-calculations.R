# Illustrative fixed-design comparisons; no clinical data or PK model.
# Run from the repository root:
# source("projects/pmx-model-based-tdp/scripts/tdp-calculations.R")
# results <- run_tdp_benchmark()

tdp_settings <- list(n = 10L, doses = c(1, 2, 4), threshold = log(0.2),
                     target = 0.9, alpha = 0.05, nsim = 10000L, seed = 20260922L)

binomial_pass <- function(p, n = 10L, target = 0.9) {
  pbinom(ceiling(n * target - 1e-12) - 1L, n, p, lower.tail = FALSE)
}

exact_lower <- function(k, n, alpha = 0.05) {
  ifelse(k == 0, 0, qbeta(alpha, pmax(k, 1), n - k + 1))
}

normal_efficiency <- function(p) {
  z <- qnorm(p)
  data.frame(p = p,
             known_sd = p * (1 - p) / dnorm(z)^2,
             estimated_sd = p * (1 - p) / (dnorm(z)^2 * (1 + z^2 / 2)))
}

tdp_scenarios <- function() {
  x <- c(-1, 0, 1)
  list(
    list(name = "Smooth: middle qualifies", p = pnorm(qnorm(.92) + .7 * x),
         sigma = rep(.45, 3)),
    list(name = "Smooth: high qualifies", p = pnorm(qnorm(.84) + .5 * x),
         sigma = rep(.45, 3)),
    list(name = "Plateau: none qualifies", p = rep(.85, 3),
         sigma = rep(.45, 3)),
    list(name = "Late rise: high qualifies", p = c(.45, .65, .97),
         sigma = rep(.45, 3)),
    list(name = "Unequal SD: none qualifies", p = c(.75, .84, .89),
         sigma = c(.2, .4, .9))
  )
}

# Under a correct normal linear model, (c - fitted mean)/(s*sqrt(h))
# is noncentral t, df = residual df, noncentrality = qnorm(p)/sqrt(h).
# Testing p <= target therefore has an exact critical value. Bonferroni
# controls declaring any inadequate dose across the three tested doses.
normal_certify <- function(mu, s, h, df, cfg = tdp_settings) {
  stat <- sweep((cfg$threshold - mu) / s, 2, sqrt(h), "/")
  critical <- qt(1 - cfg$alpha / length(cfg$doses), df = df,
                 ncp = qnorm(cfg$target) / sqrt(h))
  sweep(stat, 2, critical, ">")
}

first_qualifying <- function(pass) {
  # Column 4 is the explicit 'no dose' decision, including failed fits.
  max.col(cbind(pass, TRUE), ties.method = "first")
}

decision_summary <- function(pass, truth, scenario, method, cfg) {
  selected <- first_qualifying(pass)
  target <- if (any(truth >= cfg$target)) which(truth >= cfg$target)[1] else 4L
  selected_p <- c(truth, NA_real_)[selected]
  outcomes <- list(
    correct = selected == target,
    inadequate = !is.na(selected_p) & selected_p < cfg$target,
    higher_adequate = selected < 4L & selected != target &
      !is.na(selected_p) & selected_p >= cfg$target,
    no_dose = selected == 4L
  )
  ans <- data.frame(scenario = scenario, method = method)
  for (nm in names(outcomes)) {
    prob <- mean(outcomes[[nm]])
    ans[[nm]] <- prob
    ans[[paste0(nm, "_mcse")]] <- sqrt(prob * (1 - prob) / cfg$nsim)
  }
  ans
}

run_tdp_benchmark <- function(cfg = tdp_settings) {
  stopifnot(length(cfg$doses) == 3L, cfg$n >= 3L, cfg$nsim > 0L)
  RNGkind("Mersenne-Twister", "Inversion", "Rejection")
  set.seed(cfg$seed)
  n <- cfg$n
  nr <- cfg$nsim
  x <- log2(cfg$doses / cfg$doses[2])
  design <- cbind(1, rep(x, each = n))
  prediction <- cbind(1, x)
  transform <- solve(crossprod(design), t(design))
  h <- diag(prediction %*% solve(crossprod(design)) %*% t(prediction))
  point <- certified <- estimates <- list()
  for (sc in tdp_scenarios()) {
    mu <- cfg$threshold - sc$sigma * qnorm(sc$p)
    y <- matrix(rnorm(3L * n * nr), 3L * n, nr)
    y <- y * rep(sc$sigma, each = n) + rep(mu, each = n)
    means <- counts <- sds <- matrix(NA_real_, nr, 3)
    for (j in 1:3) {
      yy <- y[((j - 1L) * n + 1L):(j * n), , drop = FALSE]
      means[, j] <- colMeans(yy)
      counts[, j] <- colSums(yy <= cfg$threshold)
      sds[, j] <- sqrt(colSums((yy - rep(means[, j], each = n))^2) / (n - 1L))
    }
    s_common <- sqrt(rowSums(sds^2) / 3)
    beta <- transform %*% y
    fitted <- t(prediction %*% beta)
    s_curve <- sqrt(colSums((y - design %*% beta)^2) / (3L * n - 2L))
    p_est <- list(
      "M0 Counts" = counts / n,
      "M1 Binary monotone" = t(apply(counts / n, 1, function(v)
        pmin(1, pmax(0, isoreg(x, v)$yf)))),
      "M2 Continuous per arm" = pnorm((cfg$threshold - means) / sds),
      "M3 Shared SD" = pnorm((cfg$threshold - means) / s_common),
      "M4 Dose curve" = pnorm((cfg$threshold - fitted) / s_curve)
    )
    for (method in names(p_est)) {
      pp <- p_est[[method]]
      stopifnot(all(is.finite(pp)), all(pp >= 0 & pp <= 1))
      point[[length(point) + 1L]] <- decision_summary(
        pp >= cfg$target - 1e-12, sc$p, sc$name, method, cfg)
      estimates[[length(estimates) + 1L]] <- data.frame(
        scenario = sc$name, method = method, dose = cfg$doses, truth = sc$p,
        bias = colMeans(pp) - sc$p,
        rmse = sqrt(colMeans(sweep(pp, 2, sc$p, "-")^2)))
    }
    exact_p <- matrix(pbinom(as.vector(counts) - 1L, n, cfg$target,
                            lower.tail = FALSE), nr, 3)
    cert <- list(
      "M0 Counts" = exact_p <= cfg$alpha / 3,
      "M2 Continuous per arm" = normal_certify(means, sds, rep(1/n, 3), n-1, cfg),
      "M3 Shared SD" = normal_certify(means, s_common, rep(1/n, 3), 3*(n-1), cfg),
      "M4 Dose curve" = normal_certify(fitted, s_curve, h, 3*n-2, cfg)
    )
    for (method in names(cert)) {
      certified[[length(certified) + 1L]] <- decision_summary(
        cert[[method]], sc$p, sc$name, method, cfg)
    }
  }
  list(point = do.call(rbind, point), certified = do.call(rbind, certified),
       estimates = do.call(rbind, estimates), config = cfg,
       truth = do.call(rbind, lapply(tdp_scenarios(), function(s)
         data.frame(scenario = s$name, dose = cfg$doses, p = s$p, sigma = s$sigma))))
}

validate_tdp_calculations <- function() {
  stopifnot(abs(binomial_pass(.9) - (.9^10 + 10*.9^9*.1)) < 1e-12,
            abs(exact_lower(10, 10) - .05^(1/10)) < 1e-12,
            binomial_pass(0) == 0, binomial_pass(1) == 1,
            identical(first_qualifying(rbind(c(FALSE,FALSE,FALSE),
                                            c(FALSE,TRUE,TRUE),
                                            c(TRUE,FALSE,TRUE))), c(4L,2L,1L)))
  # Numerical integration verifies the noncentral-t rule at the null boundary.
  # Integrate over the residual chi-square; conditional fitted mean is normal.
  h <- 1/10
  df <- 9
  a <- .05/3
  q <- qt(1-a, df, ncp=qnorm(.9)/sqrt(h))
  probability <- integrate(function(v)
    pnorm(qnorm(.9)/sqrt(h) - q*sqrt(v/df)) * dchisq(v, df),
    0, Inf, rel.tol=1e-8)$value
  stopifnot(abs(probability-a) < 1e-6)
  invisible(TRUE)
}
