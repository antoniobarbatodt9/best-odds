#!/usr/bin/env python3
"""Costruisce una slideshow mp4 numerata da una lista di URL immagine e la carica su un upload_url.

Da eseguire dentro il sandbox Higgsfield (sandbox_exec), che ha accesso a internet, ffmpeg e Pillow.
Uso (in un solo comando sandbox, perché il sandbox si resetta tra le chiamate):

    python3 slideshow_qa.py --label OUT --seconds 3 --out qa.mp4 \
        --upload-url '<upload_url da media_upload>' \
        61=https://.../a.png 62=https://.../b.png 63=https://.../c.png

Ogni argomento posizionale è `etichetta=url`. Dopo il PUT chiama media_confirm(type=video) e
video_analysis_create(video_input_id=<media_id>).
"""
import argparse, glob, os, subprocess, urllib.request
from PIL import Image, ImageDraw, ImageFont, ImageOps

UA = "best-odds-backgrounds/1.0"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("items", nargs="+", help="label=url")
    ap.add_argument("--label", default="OUT")
    ap.add_argument("--seconds", type=float, default=3)
    ap.add_argument("--out", default="qa.mp4")
    ap.add_argument("--upload-url", default=None)
    a = ap.parse_args()

    os.makedirs("frames", exist_ok=True)
    fonts = glob.glob("/usr/share/fonts/**/*.ttf", recursive=True)
    font = ImageFont.truetype(fonts[0], 64) if fonts else ImageFont.load_default()
    names = []
    for item in a.items:
        label, url = item.split("=", 1)
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        data = urllib.request.urlopen(req, timeout=60).read()
        src = f"src_{label}.img"
        open(src, "wb").write(data)
        im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
        im.thumbnail((1280, 720))
        canvas = Image.new("RGB", (1280, 720), "black")
        canvas.paste(im, ((1280 - im.width) // 2, (720 - im.height) // 2))
        d = ImageDraw.Draw(canvas)
        d.rectangle([10, 10, 380, 100], fill="black")
        d.text((20, 15), f"{a.label} {label}", fill="white", font=font)
        name = f"frames/{label}.png"
        canvas.save(name)
        names.append(name)
        print("frame", label)
    with open("list.txt", "w") as L:
        for n in names:
            L.write(f"file '{n}'\nduration {a.seconds}\n")
        L.write(f"file '{names[-1]}'\n")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", "list.txt",
                    "-vf", "fps=25,format=yuv420p", "-c:v", "libx264", "-preset", "veryfast", "-crf", "23", a.out], check=True)
    print("video", a.out, os.path.getsize(a.out))
    if a.upload_url:
        r = subprocess.run(["curl", "-f", "-s", "-o", "/dev/null", "-w", "%{http_code}", "-X", "PUT",
                            "-H", "Content-Type: video/mp4", "--upload-file", a.out, a.upload_url],
                           capture_output=True, text=True)
        print("PUT", r.stdout)

if __name__ == "__main__":
    main()
