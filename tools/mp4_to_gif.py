"""Convert inputs/cctv.mp4 to img/test_video.gif for README (GitHub-friendly size)."""
import os
import sys

import cv2
from PIL import Image

# Defaults tuned for README: small file, still readable
MAX_WIDTH = 480
TARGET_FPS = 8.0
MAX_OUTPUT_FRAMES = 90  # ~11s at 8fps


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    src = os.path.join(root, "inputs", "cctv.mp4")
    out_dir = os.path.join(root, "img")
    out_gif = os.path.join(out_dir, "test_video.gif")
    os.makedirs(out_dir, exist_ok=True)

    cap = cv2.VideoCapture(src)
    if not cap.isOpened():
        print(f"Cannot open: {src}", file=sys.stderr)
        sys.exit(1)

    fps_src = cap.get(cv2.CAP_PROP_FPS) or 30.0
    step = max(1, int(round(fps_src / TARGET_FPS)))

    frames = []
    idx = 0
    while len(frames) < MAX_OUTPUT_FRAMES:
        ret, frame = cap.read()
        if not ret:
            break
        if idx % step != 0:
            idx += 1
            continue
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(frame_rgb)
        w, h = im.size
        if w > MAX_WIDTH:
            nw = MAX_WIDTH
            nh = int(h * (nw / w))
            im = im.resize((nw, nh), Image.Resampling.LANCZOS)
        frames.append(im)
        idx += 1

    cap.release()
    if not frames:
        print("No frames extracted", file=sys.stderr)
        sys.exit(1)

    duration_ms = int(1000 / TARGET_FPS)
    frames[0].save(
        out_gif,
        save_all=True,
        append_images=frames[1:],
        duration=duration_ms,
        loop=0,
        optimize=True,
    )
    n = os.path.getsize(out_gif)
    print(f"Wrote {out_gif}  frames={len(frames)}  size={n/1024/1024:.2f} MB")


if __name__ == "__main__":
    main()
