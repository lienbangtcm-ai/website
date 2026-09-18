from pathlib import Path
from PIL import Image, ImageOps


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output" / "insomnia" / "images"
OUT.mkdir(parents=True, exist_ok=True)

SOURCES = {
    "insomnia-hero": Path(r"C:\Users\yutin\.codex\generated_images\01a06f9e-8ac9-72c1-a871-95f36e2f17bf\exec-f2baee76-e21f-414d-aa51-eeb40cf30d5f.png"),
    "insomnia-factors": Path(r"C:\Users\yutin\.codex\generated_images\01a06f9e-8ac9-72c1-a871-95f36e2f17bf\exec-4007c0d4-793b-4943-a3dc-e65165105746.png"),
    "insomnia-evaluation": Path(r"C:\Users\yutin\.codex\generated_images\01a06f9e-8ac9-72c1-a871-95f36e2f17bf\exec-3be01bb2-0780-4b3d-83d4-dc65cd0c50bf.png"),
    "insomnia-daily-care": Path(r"C:\Users\yutin\.codex\generated_images\01a06f9e-8ac9-72c1-a871-95f36e2f17bf\exec-e410afa6-37e1-427f-8bfd-1dff84390219.png"),
}


def save_under_limit(image: Image.Image, path: Path, fmt: str) -> None:
    for quality in range(82, 49, -4):
        options = {"quality": quality, "optimize": True}
        if fmt == "JPEG":
            options.update(progressive=True, subsampling=2)
        else:
            options.update(method=6)
        image.save(path, fmt, **options)
        if path.stat().st_size <= 200_000:
            return
    raise RuntimeError(f"Could not compress {path.name} below 200 KB")


for stem, source in SOURCES.items():
    if not source.exists():
        raise FileNotFoundError(source)
    with Image.open(source) as original:
        image = ImageOps.fit(original.convert("RGB"), (1200, 800), Image.Resampling.LANCZOS)
        save_under_limit(image, OUT / f"{stem}.webp", "WEBP")
        save_under_limit(image, OUT / f"{stem}.jpg", "JPEG")

for path in sorted(OUT.iterdir()):
    print(f"{path.name}: {path.stat().st_size // 1024} KB")
