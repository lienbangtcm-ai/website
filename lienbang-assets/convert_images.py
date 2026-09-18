from pathlib import Path
from PIL import Image

ROOT = Path(__file__).parent
NAMES = [
    "lienbang-premium-home-hero",
    "pulse-prescription",
    "individualized-acupuncture",
    "acupuncture-physical-integration",
    "pulse-premium-v2",
    "acupuncture-premium-v2",
    "integration-premium-v2",
    "home-integrated-care-v3",
]

for name in NAMES:
    source = ROOT / f"{name}.png"
    target = ROOT / f"{name}.webp"
    image = Image.open(source).convert("RGB")
    image.thumbnail((1600, 1600), Image.Resampling.LANCZOS)
    image.save(target, "WEBP", quality=82, method=6)
    print(target)
