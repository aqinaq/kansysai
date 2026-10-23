"""Render the planned Intelligent Kanban UML use-case diagram as PNG.

Run with the workspace Python runtime and Pillow:
    python render_use_case.py

The diagram is a product design artifact, not evidence of implementation.
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


HERE = Path(__file__).resolve().parent
OUTPUT = HERE / "use-case-diagram.png"
W, H = 2200, 1850
BG = "#f7f8fc"
INK = "#19243a"
MUTED = "#536179"
LINE = "#8290a8"
BLUE = "#dfeaff"
VIOLET = "#eee5ff"
GREEN = "#e4f5ed"
WHITE = "#ffffff"

def load_font(size, is_bold=False):
    names = (
        ["/System/Library/Fonts/Supplemental/Arial Bold.ttf", "DejaVuSans-Bold.ttf"]
        if is_bold else
        ["/System/Library/Fonts/Supplemental/Arial.ttf", "DejaVuSans.ttf"]
    )
    for name in names:
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default(size=size)


font = load_font(32)
small = load_font(25)
tiny = load_font(22)
bold = load_font(35, True)
title_font = load_font(45, True)

im = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(im)


def centered(text, x, y, f=font, fill=INK):
    box = d.textbbox((0, 0), text, font=f)
    d.text((x - (box[2] - box[0]) / 2, y - (box[3] - box[1]) / 2), text, font=f, fill=fill)


def ellipse(cx, cy, lines, fill=WHITE):
    rx, ry = 202, 65
    d.ellipse((cx-rx, cy-ry, cx+rx, cy+ry), fill=fill, outline=INK, width=3)
    for i, line in enumerate(lines):
        centered(line, cx, cy + (i-(len(lines)-1)/2)*35, small)


def actor(x, y, lines):
    d.ellipse((x-18, y-85, x+18, y-49), outline=INK, width=4)
    d.line((x, y-49, x, y+32), fill=INK, width=4)
    d.line((x-48, y-14, x+48, y-14), fill=INK, width=4)
    d.line((x, y+32, x-42, y+88), fill=INK, width=4)
    d.line((x, y+32, x+42, y+88), fill=INK, width=4)
    for i, line in enumerate(lines):
        label_y = y+126+i*34
        box = d.textbbox((0, 0), line, font=small)
        half_width = (box[2]-box[0])/2
        d.rounded_rectangle((x-half_width-8, label_y-19, x+half_width+8, label_y+21), 8, fill=BG)
        centered(line, x, label_y, small)


def arrow(x1, y1, x2, y2, label=None, dashed=False, color=LINE):
    if dashed:
        import math
        length = math.hypot(x2-x1, y2-y1)
        ux, uy = (x2-x1)/length, (y2-y1)/length
        pos = 0
        while pos < length:
            end = min(pos+15, length)
            d.line((x1+ux*pos, y1+uy*pos, x1+ux*end, y1+uy*end), fill=color, width=3)
            pos += 27
        ax, ay = x2-ux*22, y2-uy*22
        px, py = -uy*12, ux*12
        d.line((ax+px, ay+py, x2, y2, ax-px, ay-py), fill=color, width=3)
    else:
        d.line((x1, y1, x2, y2), fill=color, width=3)
    if label:
        mx, my = (x1+x2)/2, (y1+y2)/2
        box = d.textbbox((0, 0), label, font=tiny)
        tw, th = box[2]-box[0], box[3]-box[1]
        d.rounded_rectangle((mx-tw/2-8, my-th/2-7, mx+tw/2+8, my+th/2+7), 8, fill=BG)
        centered(label, mx, my, tiny, MUTED)


d.text((82, 28), "Intelligent Kanban System", font=title_font, fill=INK)
d.text((84, 85), "UML use-case view · planned product interactions", font=font, fill=MUTED)

# System boundary.
d.rounded_rectangle((360, 150, 1730, 1690), radius=20, fill=WHITE, outline=INK, width=4)
centered("Intelligent Kanban System", 1045, 184, bold)

# User-facing and supporting use cases. The eight AI actions are detailed in the
# adjacent Markdown table; this diagram shows their shared interaction pattern.
cases = {
    "project": (740, 300, ["Access workspace", "and project"], BLUE),
    "board": (740, 485, ["Manage Kanban", "board and tasks"], BLUE),
    "voice": (740, 670, ["Submit voice", "command"], VIOLET),
    "text": (740, 855, ["Submit text", "command"], VIOLET),
    "review": (740, 1040, ["Review and edit", "proposals"], VIOLET),
    "confirm": (740, 1225, ["Confirm selected", "changes"], BLUE),
    "search": (740, 1410, ["Search accessible", "tasks"], BLUE),
    "summary": (740, 1595, ["View project", "summary"], BLUE),
    "transcribe": (1350, 670, ["Transcribe audio"], GREEN),
    "interpret": (1350, 855, ["Interpret command", "and extract fields"], GREEN),
    "clarify": (1350, 1040, ["Clarify missing or", "ambiguous details"], VIOLET),
    "validate": (1350, 1225, ["Validate and save", "authorized change"], GREEN),
    "notify": (1350, 1410, ["Send notification", "when enabled"], GREEN),
}

# Relationships are drawn before ellipses so the endpoints remain legible.
# Solid lines are actor associations. Dashed arrows are UML dependencies.
for y in (300, 485, 670, 855, 1040, 1225, 1410, 1595):
    d.line((215, 900, 360, y, 538, y), fill="#b0bad0", width=2)

d.line((1895, 600, 1730, 670, 1552, 670), fill=LINE, width=3)
d.line((1895, 900, 1730, 855, 1552, 855), fill=LINE, width=3)
d.line((1895, 1430, 1730, 1410, 1552, 1410), fill=LINE, width=3)

arrow(942, 670, 1148, 670, "<<include>>", dashed=True)
arrow(942, 855, 1148, 855, "<<include>>", dashed=True)
arrow(942, 690, 1148, 820, "<<include>>", dashed=True)
arrow(1148, 1040, 942, 1040, "<<extend>>", dashed=True)
arrow(942, 1225, 1148, 1225, "<<include>>", dashed=True)
arrow(1350, 1345, 1350, 1290, "<<extend>>", dashed=True)

actor(155, 900, ["Workspace member"])
actor(1945, 600, ["External STT service"])
actor(1945, 900, ["External LLM service"])
actor(1945, 1430, ["External email service"])

for cx, cy, lines, fill in cases.values():
    ellipse(cx, cy, lines, fill)

d.text((75, 1764), "External services are supporting actors; the AI assistant is inside the system boundary.", font=small, fill=MUTED)
d.text((75, 1800), "Dashed <<include>> / <<extend>> links describe planned behavior. No implementation is claimed.", font=tiny, fill=MUTED)
im.save(OUTPUT, optimize=True)
print(OUTPUT)
