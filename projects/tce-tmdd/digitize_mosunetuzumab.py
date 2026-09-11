"""Digitize Figure 4a of Bender et al. 2024 (mosunetuzumab, PMC11134317).

Panel (a) is one patient on 1/2/60/30 mg with only 0.5 ug/mL residual
rituximab, so it is the cleanest individual profile in the figure. Filled
black circles are observed concentrations; a thin solid line is the individual
model fit and a dotted line is receptor occupancy, both of which must be
excluded. A 3x3 erosion keeps the interiors of the filled markers and removes
every 1-2 px line.

Figure from the Europe PMC supplementary zip:
  curl -s https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11134317/supplementaryFiles \
       -o supp.zip && unzip -o supp.zip
giving CTS-17-e13825-g005.jpg at 709 x 706 px.

The y axis is calibrated by regression on eleven labelled gridlines, which is
linear in log concentration to within 0.03 decades. The x axis is calibrated
on the eight dose tick bars drawn under the panel, which also give the dose
times on the same pixel scale the observations are read from.
"""
import sys, csv
import numpy as np
from PIL import Image

GRID_ROWS = np.array([38.5, 58.5, 87.5, 107.5, 137.5, 157.5, 187, 207, 235.5, 255.5])
GRID_LOG10 = np.array([2.398, 2, 1.398, 1, 0.398, 0, -0.602, -1, -1.602, -2])
PANEL = dict(x0=88, x1=389, y0=27, y1=317)
DOSE_BAR_BAND = (280, 312)
NOMINAL_DAYS = [0, 7, 14, 21, 42, 63, 84, 105]


def _clusters(xs, ys, tol=4):
    used, out = np.zeros(len(xs), bool), []
    for i in np.argsort(xs):
        if used[i]:
            continue
        d = (np.abs(xs - xs[i]) <= tol) & (np.abs(ys - ys[i]) <= tol) & (~used)
        used |= d
        out.append((xs[d].mean(), ys[d].mean(), int(d.sum())))
    return out


def digitize(path):
    g = np.array(Image.open(path).convert("RGB")).astype(int).mean(axis=2)
    ycal = np.polyfit(GRID_ROWS, GRID_LOG10, 1)

    strip = (g[DOSE_BAR_BAND[0]:DOSE_BAR_BAND[1], PANEL["x0"]:PANEL["x1"]] < 110)
    hit = np.nonzero(strip.sum(axis=0) >= (DOSE_BAR_BAND[1] - DOSE_BAR_BAND[0]) * 0.6)[0] + PANEL["x0"]
    bars = [np.mean(c) for c in np.split(hit, np.nonzero(np.diff(hit) > 3)[0] + 1)]
    xcal = np.polyfit(bars, NOMINAL_DAYS, 1)          # px -> day

    dark = g[PANEL["y0"]:PANEL["y1"], PANEL["x0"]:PANEL["x1"]] < 110
    e = dark[1:-1, 1:-1]
    for dy in (-1, 0, 1):                              # 3x3 erosion
        for dx in (-1, 0, 1):
            e = e & dark[1 + dy:dark.shape[0] - 1 + dy, 1 + dx:dark.shape[1] - 1 + dx]
    ys, xs = np.nonzero(e)
    ys, xs = ys + PANEL["y0"] + 1, xs + PANEL["x0"] + 1

    rows = []
    for cx, cy, n in _clusters(xs, ys):
        if n < 2:
            continue
        day, conc = np.polyval(xcal, cx), 10 ** np.polyval(ycal, cy)
        if -1 <= day <= 107 and conc >= 0.004:
            rows.append(dict(day=round(float(day), 2),
                             conc_ug_mL=float("%.4g" % conc), blob_px=n))
    return sorted(rows, key=lambda r: r["day"]), [round(float(b), 1) for b in bars], xcal


if __name__ == "__main__":
    rows, bars, xcal = digitize(sys.argv[1] if len(sys.argv) > 1 else "CTS-17-e13825-g005.jpg")
    with open("data/mosunetuzumab_fig4a_obs.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["day", "conc_ug_mL", "blob_px"])
        w.writeheader()
        w.writerows(rows)
    print(f"{len(rows)} observations written")
    print("dose bars at days", [round(float(np.polyval(xcal, b)), 2) for b in bars])
