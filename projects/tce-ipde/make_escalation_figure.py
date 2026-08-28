"""Draw the MCLA-117 Cycle 1 dose escalation scheme as dose against study day.

Source of the numbers: the Cycle 1 dose escalation table in the EHA 2020
MCLA-117 CL01 e-poster (Merus; NCT03038230). Doses are converted to mg.

Writes mcla117-escalation.svg beside this file. Raw SVG with no plotting
library, so nothing has to be installed to reproduce it and the site build
never runs it:

    python3 make_escalation_figure.py
"""

import math
import pathlib

# (cohort label, [(study day, dose in mg), ...])
COHORTS = [
    ("1",  [(1, 0.025), (3, 0.05), (5, 0.1), (8, 0.2), (11, 0.3), (15, 0.45), (22, 0.675)]),
    ("2",  [(1, 0.1), (3, 0.2), (5, 0.4), (8, 0.75), (11, 1.0), (15, 1.25), (22, 1.5)]),
    ("3",  [(1, 0.3), (4, 1), (8, 2), (15, 2), (22, 2)]),
    ("4",  [(1, 0.6), (4, 2), (8, 6), (15, 6), (22, 6)]),
    ("5",  [(1, 0.6), (4, 2), (8, 9), (15, 9), (22, 9)]),
    ("6",  [(1, 1), (4, 3), (8, 15), (15, 15), (22, 15)]),
    ("7",  [(1, 1), (4, 3), (8, 15), (15, 25), (22, 25)]),
    ("8a", [(1, 1), (4, 3), (8, 25), (15, 40), (22, 40)]),
    ("8b", [(1, 3), (4, 10), (8, 25), (15, 40), (22, 40)]),
    ("9",  [(1, 5), (4, 15), (8, 25), (15, 60), (22, 60)]),
    ("10", [(1, 5), (4, 15), (8, 25), (15, 120), (22, 120)]),
    ("11", [(1, 5), (4, 15), (8, 25), (15, 240), (22, 240)]),
    ("12", [(1, 5), (4, 15), (8, 25), (15, 400), (22, 400)]),
]

W, H = 780, 470
L, R, T, B = 62, 118, 34, 52          # margins
DAY_MIN, DAY_MAX = 0, 23
LOG_MIN, LOG_MAX = math.log10(0.02), math.log10(600)

Y_TICKS = [(0.025, "25 µg"), (0.1, "100 µg"), (0.3, "300 µg"), (1, "1 mg"),
           (3, "3 mg"), (10, "10 mg"), (30, "30 mg"), (100, "100 mg"),
           (400, "400 mg")]
X_TICKS = [1, 3, 5, 8, 11, 15, 22]

INK = "#1f2933"
MUTED = "#6b7580"
GRID = "#e3e7ea"


def x(day):
    return L + (day - DAY_MIN) / (DAY_MAX - DAY_MIN) * (W - L - R)


def y(dose):
    f = (math.log10(dose) - LOG_MIN) / (LOG_MAX - LOG_MIN)
    return H - B - f * (H - B - T)


def colour(i, n):
    """Light-to-dark blue ramp, so cohort order is readable without a legend."""
    t = i / (n - 1)
    r = round(0x9e + (0x0b - 0x9e) * t)
    g = round(0xc4 + (0x37 - 0xc4) * t)
    b = round(0xe0 + (0x6b - 0xe0) * t)
    return f"#{r:02x}{g:02x}{b:02x}"


def main():
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
         f'width="100%" role="img" aria-label="MCLA-117 Cycle 1 dose escalation, '
         f'dose against study day, log scale, thirteen cohorts">',
         '<style>text{font-family:system-ui,-apple-system,"Segoe UI",Helvetica,'
         'Arial,sans-serif}</style>',
         f'<rect width="{W}" height="{H}" fill="#ffffff"/>']

    for dose, label in Y_TICKS:
        yy = round(y(dose), 1)
        p.append(f'<line x1="{L}" y1="{yy}" x2="{W-R}" y2="{yy}" stroke="{GRID}" stroke-width="1"/>')
        p.append(f'<text x="{L-8}" y="{yy+4}" text-anchor="end" font-size="11" fill="{MUTED}">{label}</text>')

    for day in X_TICKS:
        xx = round(x(day), 1)
        p.append(f'<line x1="{xx}" y1="{T}" x2="{xx}" y2="{H-B}" stroke="{GRID}" stroke-width="1"/>')
        p.append(f'<text x="{xx}" y="{H-B+18}" text-anchor="middle" font-size="11" fill="{MUTED}">D{day}</text>')

    p.append(f'<line x1="{L}" y1="{H-B}" x2="{W-R}" y2="{H-B}" stroke="{INK}" stroke-width="1"/>')
    p.append(f'<line x1="{L}" y1="{T}" x2="{L}" y2="{H-B}" stroke="{INK}" stroke-width="1"/>')

    n = len(COHORTS)

    # Cohorts 8a/8b and 2/3 end at doses too close together to label in place,
    # so push overlapping labels apart before drawing them.
    labels = sorted(((y(pts[-1][1]), i) for i, (_, pts) in enumerate(COHORTS)))
    placed = {}
    last = None
    for yy, i in labels:
        if last is not None and yy - last < 13:
            yy = last + 13
        placed[i] = yy
        last = yy

    for i, (label, pts) in enumerate(COHORTS):
        c = colour(i, n)
        path = " ".join(f"{round(x(d),1)},{round(y(v),1)}" for d, v in pts)
        p.append(f'<polyline points="{path}" fill="none" stroke="{c}" stroke-width="2" '
                 f'stroke-linejoin="round" stroke-linecap="round"/>')
        for d, v in pts:
            p.append(f'<circle cx="{round(x(d),1)}" cy="{round(y(v),1)}" r="3" fill="{c}"/>')
        ld, lv = pts[-1]
        lx, ly = x(ld) + 9, placed[i]
        if abs(ly - y(lv)) > 2:      # label moved, so join it to its line
            p.append(f'<line x1="{round(x(ld)+3,1)}" y1="{round(y(lv),1)}" x2="{round(lx-2,1)}" '
                     f'y2="{round(ly,1)}" stroke="{c}" stroke-width="1" opacity="0.55"/>')
        p.append(f'<text x="{round(lx,1)}" y="{round(ly+4,1)}" font-size="11" '
                 f'fill="{c}" font-weight="600">Cohort {label}</text>')

    p.append(f'<text x="{L}" y="{H-10}" font-size="11" fill="{MUTED}">Study day, Cycle 1</text>')
    p.append(f'<text x="14" y="{T-14}" font-size="11" fill="{MUTED}">Dose (log scale)</text>')
    p.append("</svg>")

    out = pathlib.Path(__file__).with_name("mcla117-escalation.svg")
    out.write_text("\n".join(p) + "\n", encoding="utf-8")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
