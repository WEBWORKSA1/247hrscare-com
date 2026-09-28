"""Generate OG image and PNG app icon (requires Pillow)."""
import os, glob
from PIL import Image, ImageDraw, ImageFont
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
cands = [p for p in glob.glob('/usr/share/fonts/**/*.ttf', recursive=True) if p.endswith(('LiberationSans-Bold.ttf','DejaVuSans-Bold.ttf'))]
def f(s):
    return ImageFont.truetype(cands[0], s) if cands else ImageFont.load_default()
im = Image.new('RGB', (1200, 630)); d = ImageDraw.Draw(im)
for i in range(630): d.line([(0, i), (1200, i)], fill=(10, int(95 + i * .06), int(103 + i * .06)))
d.rounded_rectangle((80, 80, 200, 200), 30, fill='#11939e'); d.arc((105, 105, 175, 175), 0, 300, fill='white', width=8)
d.ellipse((125, 128, 155, 158), fill='#ff6b4a')
d.text((230, 95), "247hrsCare", font=f(84), fill='white')
d.text((80, 260), "Find trusted care -", font=f(64), fill='white')
d.text((80, 340), "day, night & everything in between", font=f(52), fill='#ffd2c6')
d.text((80, 470), "24-hour  |  Live-in  |  Overnight  |  Dementia care  |  Free care match", font=f(30), fill='#dff5f6')
os.makedirs(os.path.join(ROOT, 'assets/img'), exist_ok=True)
im.save(os.path.join(ROOT, 'assets/img/og.png'))
ic = Image.new('RGB', (512, 512), '#0e7c86'); d = ImageDraw.Draw(ic)
d.arc((96, 96, 416, 416), 30, 330, fill='white', width=36); d.ellipse((206, 206, 306, 306), fill='#ff6b4a')
ic.save(os.path.join(ROOT, 'assets/img/icon-512.png'))
print("images ok")
