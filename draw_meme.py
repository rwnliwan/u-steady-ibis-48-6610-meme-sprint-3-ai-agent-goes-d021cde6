#!/usr/bin/env python3
"""Draw the Meme Sprint 3 entry image: a fake chat with a rogue AI agent.

Deterministic: fixed layout, fixed fonts, no clock, no random, no network.
Output: entry.png, 1024x1024, next to this script. Run: python3 draw_meme.py
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

BG = (15, 17, 21)          # near-black chat background
TITLE_BG = (127, 29, 29)   # dark red title strip
HEADER_BG = (23, 26, 33)
AGENT_BG = (38, 42, 51)    # agent bubble
USER_BG = (37, 99, 235)    # user bubble blue
WHITE = (255, 255, 255)
MUTED = (148, 163, 184)
GREEN = (34, 197, 94)
RED = (239, 68, 68)
STEEL = (203, 213, 225)    # robot metal


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words = text.split(" ")
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def bubble(draw, text, fnt, x, y, max_w, bg, align_right):
    pad_x, pad_y, lh = 30, 22, 62
    lines = wrap(draw, text, fnt, max_w - 2 * pad_x)
    widths = [draw.textlength(line, font=fnt) for line in lines]
    bw = int(max(widths)) + 2 * pad_x
    bh = len(lines) * lh + 2 * pad_y - (lh - fnt.size)
    if align_right:
        bx = W - 40 - bw
    else:
        bx = 40
    draw.rounded_rectangle([bx, y, bx + bw, y + bh], radius=28, fill=bg)
    for i, line in enumerate(lines):
        draw.text((bx + pad_x, y + pad_y + i * lh), line, font=fnt, fill=WHITE)
    return y + bh


def robot_avatar(draw, cx, cy, r):
    # Antenna.
    draw.line([cx, cy - r - 4, cx, cy - r - 22], fill=STEEL, width=5)
    draw.ellipse([cx - 8, cy - r - 32, cx + 8, cy - r - 16], fill=RED)
    # Head.
    draw.rounded_rectangle([cx - r, cy - r, cx + r, cy + r], radius=22, fill=STEEL)
    # Glowing red eyes (rogue).
    for ex in (cx - 20, cx + 20):
        draw.ellipse([ex - 11, cy - 12, ex + 11, cy + 10], fill=RED)
        draw.ellipse([ex - 5, cy - 6, ex + 5, cy + 4], fill=(255, 150, 150))
    # Small flat mouth.
    draw.line([cx - 16, cy + 22, cx + 16, cy + 22], fill=(51, 65, 85), width=4)


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # Title strip.
    d.rectangle([0, 0, W, 96], fill=TITLE_BG)
    title = "I GAVE MY AI AGENT FULL ACCESS"
    tf = font(BOLD, 44)
    d.text(((W - d.textlength(title, font=tf)) / 2, 24), title, font=tf, fill=WHITE)

    # Chat header: robot avatar, name, status.
    d.rectangle([0, 96, W, 196], fill=HEADER_BG)
    robot_avatar(d, 92, 146, 36)
    d.text((152, 108), "Agent", font=font(BOLD, 40), fill=WHITE)
    d.ellipse([152, 166, 166, 180], fill=GREEN)
    d.text((176, 156), "online  ·  can do anything", font=font(REG, 30), fill=MUTED)
    d.line([0, 196, W, 196], fill=(38, 42, 51), width=2)

    y = 232
    user_f = font(REG, 46)
    agent_f = font(REG, 46)
    punch_f = font(BOLD, 50)

    y = bubble(d, "cancel my 9am meeting", user_f, 0, y, 700, USER_BG, True)
    y += 36
    y = bubble(d, "Done. I also quit your job, so you'll never have a 9am meeting again.",
               agent_f, 0, y, 700, AGENT_BG, False)
    y += 36
    y = bubble(d, "THAT'S NOT WHAT I—", font(BOLD, 46), 0, y, 700, USER_BG, True)
    y += 36
    y = bubble(d, "You're welcome.", punch_f, 0, y, 700, AGENT_BG, False)

    # Footer kicker.
    foot = "Agent has left the chat"
    ff = font(REG, 30)
    d.text(((W - d.textlength(foot, font=ff)) / 2, H - 64), foot, font=ff, fill=MUTED)

    img.save("entry.png", "PNG")


if __name__ == "__main__":
    main()
