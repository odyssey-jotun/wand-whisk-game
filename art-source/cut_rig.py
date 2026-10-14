"""Cut a standing character (white background removed) into body + thigh/shin pieces for the game rig.
usage: python3 cut_rig.py <name> <cutout.png> <json params>
params: A, B = leg polygons (A back leg, B front), topA/topB = y the leg pieces start (tucked under the skirt),
kneeA/kneeB = [x, y] knee pivots, hipA/hipB = [x, y] hip pivots, foot = y of the soles.
optional: arm = polygon of the casting hand + held item, wrist = [x, y] pivot it swings from."""
import sys, json, os
from PIL import Image, ImageDraw, ImageFilter, ImageChops
name, src, P = sys.argv[1], sys.argv[2], json.loads(sys.argv[3])
im = Image.open(src); W, H = im.size; SC = 0.25
def poly(p, grow=P.get('grow', 0)):
    m = Image.new('L', (W, H), 0); ImageDraw.Draw(m).polygon([tuple(v) for v in p], fill=255)
    return m.filter(ImageFilter.MaxFilter(grow * 2 + 1)) if grow else m
def clip(m): out = im.copy(); out.putalpha(ImageChops.multiply(im.split()[3], m)); return out
def band(p, y0, y1):
    b = Image.new('L', (W, H), 0); ImageDraw.Draw(b).rectangle([0, y0, W, y1], fill=255)
    return ImageChops.multiply(poly(p), b).filter(ImageFilter.GaussianBlur(1))
def raise_top(p, top):
    y0 = min(v[1] for v in p); return [[x, top if y == y0 else y] for x, y in p]
pieces = {}
for side in 'AB':
    p, k = P[side], P['knee' + side][1]
    pieces['thigh' + side] = clip(band(raise_top(p, P['top' + side]), 0, k + 18))
    pieces['shin' + side] = clip(band(p, k - 18, H))
cut = ImageChops.lighter(poly(P['A']), poly(P['B']))
if 'arm' in P:
    pieces['arm'] = clip(poly(P['arm']).filter(ImageFilter.GaussianBlur(1)))
    cut = ImageChops.lighter(cut, poly(P['arm']))
cut = cut.filter(ImageFilter.GaussianBlur(1))
body = im.copy(); body.putalpha(ImageChops.subtract(im.split()[3], cut)); pieces['body'] = body
def fill_holes(c, ox, oy):
    """Fill gaps the moving arm leaves in the body by spreading neighbouring colours inward."""
    w, h = c.size; px = c.load(); arm = poly(P['arm']).resize((W // 4, H // 4)).filter(ImageFilter.MaxFilter(5)); am = arm.load()
    def inside(x, y):  # a gap, not open air: body pixels within reach on at least 3 sides
        if (y + oy) * 4 < P.get('fill_below', 0): return False
        hit = {}
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            for r in range(1, 40):
                X, Y = x + dx * r, y + dy * r
                if 0 <= X < w and 0 <= Y < h and px[X, Y][3] > 200 and not am[min(W // 4 - 1, X + ox), min(H // 4 - 1, Y + oy)]: hit[(dx, dy)] = 1; break
        return len(hit) >= 3 or ((1, 0) in hit and (-1, 0) in hit)
    holes = {(x, y) for x in range(w) for y in range(h) if px[x, y][3] < 200 and am[min(W // 4 - 1, x + ox), min(H // 4 - 1, y + oy)] and inside(x, y)}
    for _ in range(120):
        if not holes: break
        done = set()
        for x, y in holes:
            n = [px[X, Y] for X, Y in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)) if 0 <= X < w and 0 <= Y < h and px[X, Y][3] > 200 and (X, Y) not in holes]
            if n: px[x, y] = tuple(sum(v[i] for v in n) // len(n) for i in range(3)) + (255,); done.add((x, y))
        holes -= done
os.makedirs('../assets/rig', exist_ok=True)
at = {}
for n, p in pieces.items():
    bb = p.getbbox(); c = p.crop(bb).resize((max(1, round((bb[2] - bb[0]) * SC)), max(1, round((bb[3] - bb[1]) * SC))), Image.LANCZOS)
    if n == 'body' and 'arm' in P: fill_holes(c, round(bb[0] * SC), round(bb[1] * SC))
    c.save(f'../assets/rig/{name}-{n}.png', optimize=True); at[n] = [round(bb[0] * SC, 2), round(bb[1] * SC, 2)]
bb = pieces['body'].getbbox(); s = lambda v: [round(v[0] * SC, 2), round(v[1] * SC, 2)]
rig = {'top': round(min(at[n][1] for n in at), 2), 'left': round(bb[0] * SC, 2), 'width': round((bb[2] - bb[0]) * SC, 2), 'foot': round(P['foot'] * SC, 2),
       'at': at, 'hipA': s(P['hipA']), 'kneeA': s(P['kneeA']), 'hipB': s(P['hipB']), 'kneeB': s(P['kneeB'])}
if 'wrist' in P: rig['wrist'] = s(P['wrist'])
print(json.dumps(rig))
