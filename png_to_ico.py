# icon.png -> icon.ico (Windows exe용, 탐색기 크기별로 선명하게)
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("Pillow required: pip install Pillow")
    sys.exit(1)

png_path = Path(__file__).parent / "icon.png"
ico_path = Path(__file__).parent / "icon.ico"

if not png_path.exists():
    print("icon.png not found")
    sys.exit(1)

# Windows 탐색기에서 쓰는 표준 크기 (큰 것부터; 일부 뷰어는 순서에 민감)
SIZES = [(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (24, 24), (16, 16)]

img = Image.open(png_path).convert("RGBA")
# 각 크기를 LANCZOS로 리사이즈해 ICO에 포함 (크기 바꿀 때마다 해당 해상도 사용)
resized = [img.resize(sz, Image.Resampling.LANCZOS) for sz in SIZES]
resized[0].save(ico_path, format="ICO", sizes=SIZES, append_images=resized[1:])
print("Created icon.ico (sizes: %s)" % ", ".join("%dx%d" % s for s in SIZES))
