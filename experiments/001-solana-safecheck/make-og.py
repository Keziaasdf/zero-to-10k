"""Genera og.png (1200x630) para el social card de Solana SafeCheck.
Uso: python make-og.py   (requiere Pillow)
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
img = Image.new("RGB", (W, H), "#0d1117")
d = ImageDraw.Draw(img)


def font(paths, size):
    for p in paths:
        try:
            return ImageFont.truetype(p, size)
        except Exception:
            pass
    return ImageFont.load_default()


big = font([r"C:\Windows\Fonts\segoeuib.ttf", r"C:\Windows\Fonts\arialbd.ttf", "DejaVuSans-Bold.ttf"], 92)
mid = font([r"C:\Windows\Fonts\segoeui.ttf", r"C:\Windows\Fonts\arial.ttf", "DejaVuSans.ttf"], 40)
smal = font([r"C:\Windows\Fonts\segoeui.ttf", r"C:\Windows\Fonts\arial.ttf", "DejaVuSans.ttf"], 30)

d.rectangle([0, 0, 14, H], fill="#2ea043")

x = 80
for t, bg, fg in [("PASS", "#0f2e18", "#2ea043"), ("CAUTION", "#3a2d05", "#d29922"), ("KILL", "#3a0d0d", "#f85149")]:
    w = d.textlength(t, font=smal) + 40
    d.rounded_rectangle([x, 470, x + w, 520], radius=10, fill=bg, outline=fg, width=2)
    d.text((x + 20, 478), t, font=smal, fill=fg)
    x += w + 16

d.text((80, 150), "Solana SafeCheck", font=big, fill="#e6edf3")
d.text((82, 270), "Chequeo de riesgo de un token, en español", font=mid, fill="#c9d1d9")
d.text((82, 330), "CA → 5 señales → veredicto. Sin wallet, sin firmar, open source.", font=smal, fill="#8b949e")

img.save("og.png", optimize=True)
print("wrote og.png", img.size)
