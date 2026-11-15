#!/usr/bin/env python3
"""Genera los motivos Eichler Gold en SVG (currentColor: se colorean desde CSS).

starburst.svg   starburst atómico: 12 rayos largos con esfera + 12 cortos + órbitas
mini-burst.svg  estrellita de 8 rayos con puntas (detalles, viñetas)
sparkle.svg     destello de 4 puntas
boomerang.svg   boomerang de los 50
"""
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def save(name, body, size=200):
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}" '
           f'fill="none" stroke="currentColor" stroke-linecap="round">\n{body}\n</svg>\n')
    with open(os.path.join(HERE, name), "w") as fh:
        fh.write(svg)


def f(v):
    return f"{v:.2f}".rstrip("0").rstrip(".")


# Starburst atómico
c, parts = 100, []
for tilt in (60, -60):
    parts.append(f'  <ellipse cx="{c}" cy="{c}" rx="92" ry="34" transform="rotate({tilt} {c} {c})" '
                 f'stroke-width="1.5" opacity=".55"/>')
for k in range(24):
    a = k * math.pi / 12
    L = 78 if k % 2 == 0 else 52
    x, y = c + L * math.cos(a), c + L * math.sin(a)
    parts.append(f'  <line x1="{c}" y1="{c}" x2="{f(x)}" y2="{f(y)}" stroke-width="2.4"/>')
    if k % 2 == 0:
        parts.append(f'  <circle cx="{f(x)}" cy="{f(y)}" r="4.5" fill="currentColor" stroke="none"/>')
parts.append(f'  <circle cx="{c}" cy="{c}" r="10" fill="currentColor" stroke="none"/>')
save("starburst.svg", "\n".join(parts))

# Mini burst
c, parts = 50, []
for k in range(8):
    a = k * math.pi / 4
    x, y = c + 40 * math.cos(a), c + 40 * math.sin(a)
    parts.append(f'  <line x1="{c}" y1="{c}" x2="{f(x)}" y2="{f(y)}" stroke-width="3"/>')
    parts.append(f'  <circle cx="{f(x)}" cy="{f(y)}" r="5" fill="currentColor" stroke="none"/>')
parts.append(f'  <circle cx="{c}" cy="{c}" r="6" fill="currentColor" stroke="none"/>')
save("mini-burst.svg", "\n".join(parts), 100)

# Destello de 4 puntas
r, k, c = 46, 0.22, 50
pts = [(c, c - r), (c + r * k, c - r * k), (c + r, c), (c + r * k, c + r * k),
       (c, c + r), (c - r * k, c + r * k), (c - r, c), (c - r * k, c - r * k)]
save("sparkle.svg", '  <polygon points="' + " ".join(f"{f(x)},{f(y)}" for x, y in pts) +
     '" fill="currentColor" stroke="none"/>', 100)

# Boomerang
save("boomerang.svg",
     '  <path d="M14 150 C 40 70, 120 40, 186 58 C 140 62, 92 92, 62 150 C 50 168, 24 170, 14 150 Z" '
     'fill="currentColor" stroke="none"/>')

print("motivos:", sorted(x for x in os.listdir(HERE) if x.endswith(".svg")))
