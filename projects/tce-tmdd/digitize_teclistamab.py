"""Digitize Supplemental Figure 3 of Miao et al. 2023 (teclistamab, PMC10518021).

The main paper carries no concentration-time figure; every figure in it is
exposure-response. Supplemental Figure 3 is the final population PK model's
simulated median profile at the recommended phase II dose (1.5 mg/kg weekly
subcutaneous, preceded by 0.06 and 0.3 mg/kg step-up doses, n = 1000), which
is the published model's own summary of the data and the only
concentration-time curve the paper provides.

Supplement from the Europe PMC supplementary zip:
  curl -s https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10518021/supplementaryFiles \
       -o supp.zip && unzip -o supp.zip
then render page 5 at 300 dpi:
  pdftoppm -f 5 -l 5 -r 300 -png 11523_2023_989_MOESM1_ESM.pdf tecp5

The solid red median line is extracted column by column as the median red
pixel; the pale pink 90% predictive interval is excluded by requiring a
saturated red. Axis calibration is measured from the tick marks and is linear
to within 0.006 decades in y and 0.004 weeks in x.

Time is reported relative to the FIRST step-up dose, which the figure places
at week -1: the curve begins at day -7.1 on the figure's own axis, so `day` in
the output keeps the figure's origin (the first full treatment dose) and `t`
is recovered downstream as day + 7.
"""
import sys, csv
import numpy as np
from PIL import Image

X_TICKS = np.array([660.0, 872.5, 1085.0, 1297.0, 1509.5, 1722.0, 1934.5])
X_WEEKS = np.array([0, 4, 8, 12, 16, 20, 24])
Y_TICKS = np.array([506.0, 735.0, 966.0, 1194.0, 1426.0])
Y_LOG10 = np.array([2, 1, 0, -1, -2])                 # 100 down to 0.01 ug/mL
PLOT = dict(top=420, bottom=1470, left=546)
MIN_SPACING_DAYS = 0.5


def digitize(path):
    a = np.array(Image.open(path).convert("RGB")).astype(int)
    R, G, B = a[:, :, 0], a[:, :, 1], a[:, :, 2]
    red = (R > 170) & (G < 110) & (B < 110)           # solid line, not the pale band
    red[:PLOT["top"], :] = False
    red[PLOT["bottom"]:, :] = False
    red[:, :PLOT["left"]] = False

    ycal, xcal = np.polyfit(Y_TICKS, Y_LOG10, 1), np.polyfit(X_TICKS, X_WEEKS, 1)
    cols = np.nonzero(red.any(axis=0))[0]
    rows, last = [], -np.inf
    for x in cols:
        ys = np.nonzero(red[:, x])[0]
        week = float(np.polyval(xcal, x))
        day = week * 7
        if day - last < MIN_SPACING_DAYS:
            continue
        last = day
        rows.append(dict(week=round(week, 4), day=round(day, 3),
                         conc_ug_mL=float("%.4g" % 10 ** float(np.polyval(ycal, np.median(ys))))))
    return rows, ycal, xcal


if __name__ == "__main__":
    rows, ycal, xcal = digitize(sys.argv[1] if len(sys.argv) > 1 else "tecp5-5.png")
    with open("data/teclistamab_suppfig3_median.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["week", "day", "conc_ug_mL"])
        w.writeheader()
        w.writerows(rows)
    print(f"{len(rows)} points, day {rows[0]['day']} to {rows[-1]['day']}, "
          f"{-1/ycal[0]:.1f} px/decade, {1/xcal[0]:.1f} px/week")
