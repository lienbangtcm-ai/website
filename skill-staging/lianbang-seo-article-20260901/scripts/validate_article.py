#!/usr/bin/env python3
from html.parser import HTMLParser
from pathlib import Path
import sys
import urllib.parse


class ArticleParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.h1_count = 0
        self.images = []
        self.links = []
        self.contenteditable = []

    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if tag == "h1":
            self.h1_count += 1
        if tag == "img":
            self.images.append(data)
        if tag == "a":
            self.links.append(data)
        if data.get("contenteditable", "").lower() == "true":
            self.contenteditable.append(tag)


def main():
    if len(sys.argv) != 2:
        print("Usage: validate_article.py <html-path>")
        return 2

    path = Path(sys.argv[1])
    parser = ArticleParser()
    parser.feed(path.read_text(encoding="utf-8"))
    errors = []

    if parser.h1_count != 1:
        errors.append(f"expected exactly one H1, found {parser.h1_count}")
    if parser.contenteditable:
        errors.append("publishable HTML contains contenteditable=true")

    for index, image in enumerate(parser.images, 1):
        if not image.get("src"):
            errors.append(f"image {index} has no src")
        if not image.get("alt"):
            errors.append(f"image {index} has empty alt")
        if not image.get("width") or not image.get("height"):
            errors.append(f"image {index} has no fixed width/height")

    line_links = [link for link in parser.links if "lin.ee" in link.get("href", "")]
    if len(line_links) != 1:
        errors.append(f"expected one LINE CTA, found {len(line_links)}")
    elif line_links[0].get("href") != "https://lin.ee/UWWKmse":
        errors.append("LINE CTA does not use the saved clinic URL")

    for index, link in enumerate(parser.links, 1):
        href = link.get("href", "").strip()
        if not href or href == "#":
            errors.append(f"link {index} has an empty or placeholder href")
        if link.get("target") == "_blank":
            rel = set(link.get("rel", "").split())
            if not {"noopener", "noreferrer"}.issubset(rel):
                errors.append(f"external link {index} lacks noopener noreferrer")
        parsed = urllib.parse.urlparse(href)
        if parsed.scheme and parsed.scheme not in {"http", "https", "mailto", "tel"}:
            errors.append(f"link {index} uses unsupported scheme {parsed.scheme}")

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validation passed: {len(parser.images)} images, {len(parser.links)} links")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
