#!/usr/bin/env python3
"""
Desert Liturgy — Visual Expression for Bright Side Cafe
Second pass: Refined composition, stronger presence, pristine execution.
"""

from PIL import Image, ImageDraw, ImageFont
import math
import random

W, H = 2700, 3600
img = Image.new('RGBA', (W, H), (30, 20, 16, 255))
draw = ImageDraw.Draw(img)

# === PALETTE ===
espresso_rgb = (30, 20, 16)
warm_ochre = '#D4A052'
warm_ochre_rgb = (212, 160, 82)
bleached_cream = '#F5EDE3'
cream_rgb = (245, 237, 227)
charcoal = '#3D2E24'
charcoal_rgb = (61, 46, 36)
sand = '#B8A48C'
sand_rgb = (184, 164, 140)
muted_gold = '#A8824A'
muted_gold_rgb = (168, 130, 74)
soft_gold_rgb = (200, 150, 90)
deep_rgb = (36, 26, 20)

# === FONTS ===
supp = '/System/Library/Fonts/Supplemental/'
font_didot_xl = ImageFont.truetype(supp + 'Didot.ttc', 200)
font_didot_lg = ImageFont.truetype(supp + 'Didot.ttc', 140)
font_didot_md = ImageFont.truetype(supp + 'Didot.ttc', 60)
font_didot_sm = ImageFont.truetype(supp + 'Didot.ttc', 40)
font_didot_italic = ImageFont.truetype(supp + 'Didot.ttc', 42, index=1)
font_futura_sm = ImageFont.truetype(supp + 'Futura.ttc', 20)
font_futura_xs = ImageFont.truetype(supp + 'Futura.ttc', 16)
font_futura_md = ImageFont.truetype(supp + 'Futura.ttc', 26)


# === BACKGROUND GRADIENT ===
for y in range(H):
    t = y / H
    r = int(30 + t * 8)
    g = int(20 + t * 5)
    b = int(16 + t * 4)
    draw.line([(0, y), (W, y)], fill=(r, g, b, 255))

# === GRAIN TEXTURE ===
random.seed(42)
for _ in range(60000):
    x = random.randint(0, W-1)
    y = random.randint(0, H-1)
    v = random.randint(200, 255)
    a = random.randint(2, 8)
    draw.point((x, y), fill=(v, v, v, a))

# === OUTER FRAME (thin, precise) ===
m = 80
draw.rectangle([m, m, W-m, H-m], outline=charcoal_rgb + (80,), width=1)

# Registration marks at corners
mk = 15
for cx, cy in [(m, m), (W-m, m), (m, H-m), (W-m, H-m)]:
    draw.line([(cx-mk, cy), (cx+mk, cy)], fill=muted_gold_rgb + (120,), width=1)
    draw.line([(cx, cy-mk), (cx, cy+mk)], fill=muted_gold_rgb + (120,), width=1)

# === TOP FIELD NOTATION ===
draw.text((180, 140), 'I', font=font_futura_xs, fill=muted_gold_rgb)
draw.text((180, 162), 'DESERT LITURGY', font=font_futura_xs, fill=charcoal_rgb)

draw.text((W - 500, 140), 'FIELD STUDY NO. 01', font=font_futura_xs, fill=charcoal_rgb)
draw.text((W - 500, 162), 'SCOTTSDALE, ARIZONA', font=font_futura_xs, fill=charcoal_rgb + (120,))

# === THIN HORIZONTAL RULE (top boundary) ===
draw.line([(180, 280), (W-180, 280)], fill=charcoal_rgb + (100,), width=1)

# === VERTICAL SPINE TEXT (left edge) ===
spine = "OLD TOWN SCOTTSDALE  \u00b7  THE MERCANTILE"
for i, ch in enumerate(spine):
    if ch == ' ':
        continue
    alpha = 100 if ch == '\u00b7' else 60
    draw.text((120, 380 + i * 24), ch, font=font_futura_xs, fill=charcoal_rgb + (alpha,))

# === SACRED GEOMETRY: Central mandala ===
cx, cy = W // 2, 980

# Outermost circle — barely there
for r in [480, 470]:
    draw.ellipse([cx-r, cy-r, cx+r, cy+r], outline=charcoal_rgb + (40,), width=1)

# Second ring
r2 = 360
draw.ellipse([cx-r2, cy-r2, cx+r2, cy+r2], outline=charcoal_rgb + (70,), width=1)

# Third ring — gold accent
r3 = 240
draw.ellipse([cx-r3, cy-r3, cx+r3, cy+r3], outline=muted_gold_rgb + (100,), width=1)

# Inner ring
r4 = 140
draw.ellipse([cx-r4, cy-r4, cx+r4, cy+r4], outline=warm_ochre_rgb + (150,), width=2)

# Core — filled gold circle (the cup viewed from above)
r5 = 50
draw.ellipse([cx-r5, cy-r5, cx+r5, cy+r5], fill=soft_gold_rgb + (220,))

# Inner glow around core
r5b = 65
draw.ellipse([cx-r5b, cy-r5b, cx+r5b, cy+r5b], outline=warm_ochre_rgb + (60,), width=1)

# === RADIATING LINES (sunrise / steam / saguaro ribs) ===
for angle_deg in range(0, 360, 15):
    angle = math.radians(angle_deg)
    # Short inner rays
    x1 = cx + 75 * math.cos(angle)
    y1 = cy + 75 * math.sin(angle)
    x2 = cx + 130 * math.cos(angle)
    y2 = cy + 130 * math.sin(angle)
    alpha = 150 if angle_deg % 30 == 0 else 60
    draw.line([(x1, y1), (x2, y2)], fill=muted_gold_rgb + (alpha,), width=1)

# Long cardinal rays extending outward
for angle_deg in [0, 90, 180, 270]:
    angle = math.radians(angle_deg)
    x1 = cx + 250 * math.cos(angle)
    y1 = cy + 250 * math.sin(angle)
    x2 = cx + 460 * math.cos(angle)
    y2 = cy + 460 * math.sin(angle)
    draw.line([(x1, y1), (x2, y2)], fill=charcoal_rgb + (50,), width=1)

# Spiral arcs (the pour)
for i, (r, start, span) in enumerate([
    (190, 30, 100), (210, 60, 80), (230, 10, 120)
]):
    color = warm_ochre_rgb + (80,) if i == 0 else charcoal_rgb + (50,)
    draw.arc([cx-r, cy-r, cx+r, cy+r], start, start + span, fill=color, width=1)

# === TITLE BLOCK ===
# "BRIGHT SIDE" — large, centered Didot
title = "BRIGHT SIDE"
bb = draw.textbbox((0, 0), title, font=font_didot_xl)
tw = bb[2] - bb[0]
tx = (W - tw) // 2
ty = 1580
draw.text((tx, ty), title, font=font_didot_xl, fill=cream_rgb + (240,))

# Gold accent line beneath
line_w = tw + 40
lx = (W - line_w) // 2
draw.line([(lx, ty + 240), (lx + line_w, ty + 240)], fill=warm_ochre_rgb + (180,), width=1)

# "C A F E" — spaced Futura
cafe = "C   A   F   E"
bb_c = draw.textbbox((0, 0), cafe, font=font_futura_md)
cw = bb_c[2] - bb_c[0]
draw.text(((W - cw) // 2, ty + 268), cafe, font=font_futura_md, fill=sand_rgb + (180,))

# === VERTICAL SLAT PATTERN (counter paneling / saguaro ribs) ===
slat_top = 2080
slat_bot = 2550
slat_count = 55
slat_margin_l = 250
slat_margin_r = 250
total_w = W - slat_margin_l - slat_margin_r
spacing = total_w / (slat_count - 1)

for i in range(slat_count):
    x = slat_margin_l + i * spacing
    # Organic height variation
    h_var = int(20 * math.sin(i * 0.35 + 0.5))
    top = slat_top + h_var
    bot = slat_bot - h_var

    # Every 7th slat is gold accent
    if i % 7 == 0:
        draw.line([(x, top - 10), (x, bot + 10)], fill=warm_ochre_rgb + (140,), width=2)
    else:
        alpha = 50 + int(30 * abs(math.sin(i * 0.2)))
        draw.line([(x, top), (x, bot)], fill=charcoal_rgb + (alpha,), width=1)

# Horizontal rules framing the slats
draw.line([(slat_margin_l, slat_top - 30), (W - slat_margin_r, slat_top - 30)], fill=charcoal_rgb + (60,), width=1)
draw.line([(slat_margin_l, slat_bot + 30), (W - slat_margin_r, slat_bot + 30)], fill=charcoal_rgb + (60,), width=1)

# Figure caption
draw.text((slat_margin_l, slat_bot + 55), 'FIG. 1', font=font_futura_xs, fill=muted_gold_rgb + (180,))
draw.text((slat_margin_l + 60, slat_bot + 55), '\u2014  VERTICAL RHYTHM  /  MATERIAL STUDY', font=font_futura_xs, fill=charcoal_rgb + (100,))

# === LOWER SECTION: Data inscription ===
data_y = 2780
draw.line([(180, data_y), (W - 180, data_y)], fill=charcoal_rgb + (80,), width=1)

# Coordinates
draw.text((180, data_y + 30), '33.4942\u00b0 N, 111.9261\u00b0 W', font=font_futura_sm, fill=muted_gold_rgb + (200,))
draw.text((180, data_y + 60), 'INSIDE THE MERCANTILE  /  3965 N BROWN AVE  /  SCOTTSDALE AZ 85251', font=font_futura_xs, fill=charcoal_rgb + (120,))

# Right column
draw.text((W - 680, data_y + 30), 'ORGANIC  \u00b7  HANDCRAFTED  \u00b7  INTENTIONAL', font=font_futura_xs, fill=charcoal_rgb + (100,))
draw.text((W - 680, data_y + 55), 'WHERE EVERY CUP TELLS A STORY', font=font_futura_sm, fill=muted_gold_rgb + (160,))

# === DOT PATTERN (sacred rhythm) ===
dot_y = 2970
dot_count = 33
dot_margin = 250
for i in range(dot_count):
    dx = dot_margin + i * (W - 2 * dot_margin) / (dot_count - 1)
    if i % 4 == 0:
        draw.ellipse([dx-5, dot_y-5, dx+5, dot_y+5], fill=warm_ochre_rgb + (180,))
    else:
        draw.ellipse([dx-2, dot_y-2, dx+2, dot_y+2], fill=charcoal_rgb + (80,))

# === WHISPERED PHRASE ===
phrase = "the slow pour"
bb_p = draw.textbbox((0, 0), phrase, font=font_didot_italic)
pw = bb_p[2] - bb_p[0]
draw.text(((W - pw) // 2, 3120), phrase, font=font_didot_italic, fill=sand_rgb + (140,))

# === SUNRISE ICON (the bright side) ===
sun_cx, sun_cy = W // 2, 3280
# Half circle
draw.arc([sun_cx-45, sun_cy-45, sun_cx+45, sun_cy+45], 180, 360, fill=warm_ochre_rgb + (200,), width=2)
# Horizon line
draw.line([(sun_cx-65, sun_cy), (sun_cx+65, sun_cy)], fill=warm_ochre_rgb + (200,), width=1)
# Rays
for angle_deg in range(195, 350, 22):
    angle = math.radians(angle_deg)
    x1 = sun_cx + 52 * math.cos(angle)
    y1 = sun_cy + 52 * math.sin(angle)
    x2 = sun_cx + 72 * math.cos(angle)
    y2 = sun_cy + 72 * math.sin(angle)
    draw.line([(x1, y1), (x2, y2)], fill=warm_ochre_rgb + (160,), width=1)

# === EDITION FOOTER ===
draw.text((180, H - 140), 'DESERT LITURGY  \u00b7  BSC', font=font_futura_xs, fill=charcoal_rgb + (80,))
draw.text((W - 440, H - 140), 'EDITION 01  /  APRIL 2026', font=font_futura_xs, fill=charcoal_rgb + (80,))

# Second thin rule near bottom
draw.line([(180, H - 170), (W - 180, H - 170)], fill=charcoal_rgb + (50,), width=1)

# === SAVE ===
output = '/Users/jalenjohn/Agent Owen/bright-side-cafe/bright-side-desert-liturgy.png'
img.convert('RGB').save(output, 'PNG', quality=100)
print(f'Canvas saved: {output}')
print(f'Size: {W}x{H}px')
