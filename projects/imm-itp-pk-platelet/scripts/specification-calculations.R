# Illustrative calculations for specification.md, Section 14.
# These are not operating characteristics for the proposed clinical decision.
# Run with: Rscript scripts/specification-calculations.R
# Base R only; sourcing the file defines functions without printing tables.

pcs_two <- function(n, p_high, p_low) {
  stopifnot(length(n) == 1L, n >= 1, n == as.integer(n),
            p_high >= 0, p_high <= 1, p_low >= 0, p_low <= 1)
  k <- 0:n
  sum(dbinom(k, n, p_high) *
        (pbinom(k - 1, n, p_low) + 0.5 * dbinom(k, n, p_low)))
}

minimum_selection_n <- function(p_high, p_low, target = 0.80, max_n = 5000L) {
  for (n in seq_len(max_n)) {
    if (pcs_two(n, p_high, p_low) >= target) return(n)
  }
  NA_integer_
}

# Local asymptotic variance ratio: binary logistic dose-response versus
# unpooled response proportions at the top two doses. Both use all patients
# at those top doses, including escalation patients. No PK or platelets enter.
pooling_ratio <- function(p_top, delta, x, n) {
  K <- length(x)
  stopifnot(K >= 2, length(n) == K, all(n > 0), all(diff(x) > 0),
            p_top > delta, delta > 0, p_top < 1)
  b <- (qlogis(p_top) - qlogis(p_top - delta)) / (x[K] - x[K - 1])
  a <- qlogis(p_top) - b * x[K]
  p <- plogis(a + b * x)
  w <- n * p * (1 - p)
  info <- rbind(c(sum(w), sum(w * x)), c(sum(w * x), sum(w * x^2)))
  g <- c(p[K] * (1 - p[K]) - p[K - 1] * (1 - p[K - 1]),
         x[K] * p[K] * (1 - p[K]) - x[K - 1] * p[K - 1] * (1 - p[K - 1]))
  v_model <- drop(t(g) %*% solve(info, g))
  v_pair <- p[K] * (1 - p[K]) / n[K] +
    p[K - 1] * (1 - p[K - 1]) / n[K - 1]
  v_pair / v_model
}

report_calculations <- function() {
  selection <- data.frame(p_low = c(.45, .45, .45, .50, .50),
                          p_high = .55, n_per_arm = c(6, 20, 40, 141, 142))
  selection$probability_correct <- mapply(pcs_two, selection$n_per_arm,
                                         selection$p_high, selection$p_low)
  cat("Exact two-arm selection probability; ties split equally\n")
  print(selection, row.names = FALSE, digits = 7)
  pairs <- data.frame(p_low = c(.30, .40, .50, .50),
                      p_high = c(.50, .60, .60, .55))
  pairs$n_superiority <- mapply(function(lo, hi)
    ceiling(power.prop.test(p1 = lo, p2 = hi, power = .8,
                            sig.level = .05, alternative = "two.sided")$n),
    pairs$p_low, pairs$p_high)
  cat("\nApproximate superiority-test sizes: two-sided 5%, power 80%\n")
  print(pairs, row.names = FALSE)
  cat("\nExact minimum n for 80% selection at 55% versus 50%:",
      minimum_selection_n(.55, .50), "\n")
  pooling <- expand.grid(n_exp = c(20, 30, 40), delta = c(.05, .10, .15, .20))
  pooling$variance_ratio <- mapply(function(ne, d)
    pooling_ratio(.55, d, 0:4, c(4, 4, 4, 4 + ne, 4 + ne)),
    pooling$n_exp, pooling$delta)
  cat("\nBinary logistic pooling illustration; not PK model sample savings\n")
  print(pooling, row.names = FALSE, digits = 4)
  invisible(list(selection = selection, superiority = pairs, pooling = pooling))
}

if (sys.nframe() == 0L) report_calculations()
