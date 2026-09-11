"""Digitize Figure 4A of Kovalenko et al. 2026 (odronextamab, PMC12823311).

Extracts the pink observed-median markers from the cycle 1-3 concentration-time
panels, one for DLBCL and one for FL, and writes data/odronextamab_fig4A_medians.csv.

The figure is fetched from the Europe PMC supplementary-files zip:
  curl -s https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12823311/supplementaryFiles \
       -o supp.zip && unzip -o supp.zip
giving PSP4-15-e70162-g004.jpg at 709 x 1703 px.

Axis calibration is read off the image rather than assumed, and is checked
against the published assay limit of quantification of 0.00313 mg/L, which the
figure draws as a dashed line: the line is found at row 179.5 and the
calibration predicts 180.3, so the mapping is good to about 1 px (~5% in
concentration). Run: python3 digitize_odronextamab.py <path-to-g004.jpg>
"""
import sys, csv
import numpy as np
from PIL import Image

# Panel A axis calibration, in pixels, measured from tick marks in the image.
Y_TICKS = [24.0, 68.5, 113.0, 157.5, 202.4]        # 1e+01 down to 1e-03
PANELS = {
    "DLBCL": dict(x0=74,  x1=389, x_week0=86.0,  px_per_week=(364.0 - 86.0) / 3),
    "FL":    dict(x0=393, x1=708, x_week0=405.0, px_per_week=(683.0 - 405.0) / 3),
}
LLOQ = 0.00313


def medians(path):
    a = np.array(Image.open(path).convert("RGB")).astype(int)
    R, G, B = a[:, :, 0], a[:, :, 1], a[:, :, 2]
    pink = (R > 150) & (G < 110) & (B > 70) & (B < 190) & ((R - G) > 70)
    px_decade = (Y_TICKS[-1] - Y_TICKS[0]) / 4.0
    rows = []
    for name, p in PANELS.items():
        sub = np.zeros_like(pink)
        sub[:212, p["x0"]:p["x1"]] = pink[:212, p["x0"]:p["x1"]]
        ys, xs = np.nonzero(sub)
        used, blobs = np.zeros(len(xs), bool), []
        for i in np.argsort(xs):                     # cluster pixels into markers
            if used[i]:
                continue
            d = (np.abs(xs - xs[i]) <= 4) & (np.abs(ys - ys[i]) <= 4) & (~used)
            used |= d
            blobs.append((xs[d].mean(), ys[d].mean(), int(d.sum())))
        blobs = sorted([b for b in blobs if b[2] >= 4], key=lambda q: (q[0], -q[2]))
        merged = []
        for q in blobs:                              # drop fragments of one marker
            if merged and abs(q[0] - merged[-1][0]) <= 4 and abs(q[1] - merged[-1][1]) <= 8:
                continue
            merged.append(q)
        for cx, cy, n in merged:
            rows.append(dict(
                subtype=name,
                day=round((cx - p["x_week0"]) / p["px_per_week"] * 7, 2),
                conc_mg_L=float("%.4g" % (10 ** (-3 + (Y_TICKS[-1] - cy) / px_decade))),
                blob_px=n))
    return sorted(rows, key=lambda r: (r["subtype"], r["day"]))


if __name__ == "__main__":
    rows = medians(sys.argv[1] if len(sys.argv) > 1 else "PSP4-15-e70162-g004.jpg")
    with open("data/odronextamab_fig4A_medians.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["subtype", "day", "conc_mg_L", "blob_px"])
        w.writeheader()
        w.writerows(rows)
    print(f"{len(rows)} medians written; "
          f"{sum(r['conc_mg_L'] <= LLOQ * 1.12 for r in rows)} sit at the assay limit")
