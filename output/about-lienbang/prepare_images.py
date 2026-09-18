from pathlib import Path
from PIL import Image

OUT = Path(r"C:\Users\yutin\Documents\網站相關\output\about-lienbang")
OUT.mkdir(parents=True, exist_ok=True)

PAIRS = [
    (
        Path(r"C:\Users\yutin\.codex\generated_images\019f63f0-424e-7363-a0d5-8840b401a33f\exec-2f51e3af-3179-4abb-8296-b591bc72b2f4.png"),
        OUT / "ntu-campus-meeting.webp",
    ),
    (
        Path(r"C:\Users\yutin\.codex\generated_images\019f63f0-424e-7363-a0d5-8840b401a33f\exec-7f5d7ace-5321-448f-bb54-3d9a739363cb.png"),
        OUT / "tcm-physical-therapy-paths.webp",
    ),
    (
        Path(r"C:\Users\yutin\.codex\generated_images\019f63f0-424e-7363-a0d5-8840b401a33f\exec-7e7db32b-df7f-4961-b4cc-7781b6d1dd0b.png"),
        OUT / "integrated-care-direction.webp",
    ),
]

for source, destination in PAIRS:
    with Image.open(source) as image:
        resized = image.convert("RGB").resize((1600, 1067), Image.Resampling.LANCZOS)
        resized.save(destination, "WEBP", quality=84, method=6)
    print(f"{destination.name}: {destination.stat().st_size} bytes")
