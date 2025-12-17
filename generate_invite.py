import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

W, H = 1200, 630
url = 'https://akinot84.github.io/anuncio-bb/invitation.html'
qr_api = 'https://api.qrserver.com/v1/create-qr-code/?size=360x360&data=' + requests.utils.requote_uri(url)

# Create background
# Background: neon gradient
bg = Image.new('RGBA', (W, H), (6,8,12,255))
g = Image.new('RGBA', (W, H))
gd = ImageDraw.Draw(g)
for i in range(H):
    # interpolate between neon cyan and pink
    r = int(6 + (255-6) * (i / H) * 0.06)
    gcol = int(8 + (0-8) * (i / H) * 0.02)
    b = int(18 + (234-18) * (i / H) * 0.03)
    gd.line([(0,i),(W,i)], fill=(r, int(80 + 120*(i/H)), int(120 + 100*(i/H)), 12))
bg = Image.alpha_composite(bg, g)

# decorative soft neon blobs
dec = Image.new('RGBA', (W, H))
dd = ImageDraw.Draw(dec)
dd.ellipse((W*0.04, H*0.06, W*0.44, H*0.46), fill=(255,0,234,40))
dd.ellipse((W*0.62, H*0.52, W*0.98, H*0.98), fill=(15,255,193,36))
bg = Image.alpha_composite(bg, dec)

draw = ImageDraw.Draw(bg)
try:
    font_title = ImageFont.truetype('Baloo-Regular.ttf', 64)
    font_sub = ImageFont.truetype('Baloo-Regular.ttf', 22)
    font_btn = ImageFont.truetype('Baloo-Regular.ttf', 28)
    font_url = ImageFont.truetype('arial.ttf', 18)
except Exception:
    font_title = ImageFont.truetype('arial.ttf', 48)
    font_sub = ImageFont.truetype('arial.ttf', 20)
    font_btn = ImageFont.truetype('arial.ttf', 24)
    font_url = ImageFont.load_default()

# Title (neon gradient text simulated with shadow)
title = '¡Un regalo de Fam Akime!'
tb = draw.textbbox((0,0), title, font=font_title)
tw = tb[2]-tb[0]
draw.text(((W-tw)/2, 60), title, font=font_title, fill=(255,255,255,255))
draw.text(((W-tw)/2, 60), title, font=font_title, fill=(255,0,234,200))
sub_text = 'Haz clic en abrir regalo para ver la sorpresa'
sb = draw.textbbox((0,0), sub_text, font=font_sub)
draw.text(((W-sb[2])/2, 140), sub_text, font=font_sub, fill=(200,255,240,230))

# Fetch QR
resp = requests.get(qr_api)
qr = Image.open(BytesIO(resp.content)).convert('RGBA')
qr_size = 300
qr = qr.resize((qr_size, qr_size), Image.LANCZOS)
qr_x = W - qr_size - 60
qr_y = H - qr_size - 80
# rounded bg rectangle
rect = Image.new('RGBA', (qr_size+36, qr_size+36), (0,0,0,140))
rdraw = ImageDraw.Draw(rect)
rdraw.rounded_rectangle((0,0,qr_size+36, qr_size+36), radius=20, fill=(0,0,0,140))
bg.paste(rect, (qr_x-18, qr_y-18), rect)
bg.paste(qr, (qr_x, qr_y), qr)

# draw a neon "Abrir invitación" button near center-left
btn_w, btn_h = 360, 68
btn_x = 80
btn_y = qr_y + qr_size - 20
btn = Image.new('RGBA', (btn_w, btn_h), (0,0,0,0))
bd = ImageDraw.Draw(btn)
# neon gradient
for i in range(btn_h):
    rcol = int(255 - (i/btn_h)*30)
    gcol = int(0 + (i/btn_h)*200)
    bd.line([(0,i),(btn_w,i)], fill=(rcol, int(120 + i/btn_h*80), int(200 - i/btn_h*60), 220))
bd.rounded_rectangle((0,0,btn_w,btn_h), radius=18, outline=(255,0,234,200), width=3)
# button text
text = 'Abrir invitación'
tb = bd.textbbox((0,0), text, font=font_btn)
bd.text(((btn_w - (tb[2]-tb[0]))/2, (btn_h - (tb[3]-tb[1]))/2 -2), text, font=font_btn, fill=(255,255,255,255))
bg.paste(btn, (btn_x, btn_y), btn)

# URL text
url_text = url
try:
    font_url = ImageFont.truetype('arial.ttf', 18)
except:
    font_url = ImageFont.load_default()
bboxu = draw.textbbox((0,0), url_text, font=font_url)
w_url = bboxu[2]-bboxu[0]
draw.text((qr_x + qr_size/2 - w_url/2, qr_y + qr_size + 6), url_text, font=font_url, fill=(202,255,240))

out_path = 'invite-card.png'
bg.convert('RGB').save(out_path, format='PNG')
print('Saved', out_path)
