#!/usr/bin/env python3
"""Build the static academic site from YAML content and Jinja2 templates."""

from __future__ import annotations

import shutil
from pathlib import Path
from typing import Any

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).resolve().parent
CONTENT_DIR = ROOT / "content"
TEMPLATE_DIR = ROOT / "templates"
STATIC_DIR = ROOT / "static"
ASSETS_DIR = ROOT / "assets"
OUT_DIR = ROOT / "site"


def load_yaml(path: Path) -> dict[str, Any]:
    """Load a YAML content file used as site data."""
    with path.open(encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or {}
    if not isinstance(data, dict):
        raise ValueError(f"Expected mapping in {path}")
    return data


def load_all_content() -> dict[str, Any]:
    """Merge global and page content for template rendering."""
    site = load_yaml(CONTENT_DIR / "site.yaml")
    pages = {
        "home": load_yaml(CONTENT_DIR / "home.yaml"),
        "about": load_yaml(CONTENT_DIR / "about.yaml"),
        "research": load_yaml(CONTENT_DIR / "research.yaml"),
        "teaching": load_yaml(CONTENT_DIR / "teaching.yaml"),
        "resources": load_yaml(CONTENT_DIR / "resources.yaml"),
        "contact": load_yaml(CONTENT_DIR / "contact.yaml"),
    }
    publications = load_yaml(CONTENT_DIR / "publications.yaml")
    return {
        "site": site,
        "pages": pages,
        "publications": publications.get("items", []),
    }


def copy_tree(src: Path, dest: Path) -> None:
    """Copy static or asset trees into the build output."""
    if not src.exists():
        return
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(src, dest)


def build() -> None:
    """Generate the full static site into ./site."""
    context = load_all_content()
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATE_DIR)),
        autoescape=select_autoescape(["html", "xml"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )

    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)
    OUT_DIR.mkdir(parents=True)

    pages_to_render = [
        ("index.html", "home.html.j2", "home"),
        ("about/index.html", "about.html.j2", "about"),
        ("research/index.html", "research.html.j2", "research"),
        ("teaching/index.html", "teaching.html.j2", "teaching"),
        ("resources/index.html", "resources.html.j2", "resources"),
        ("contact/index.html", "contact.html.j2", "contact"),
    ]

    for output_rel, template_name, page_key in pages_to_render:
        template = env.get_template(template_name)
        html = template.render(
            site=context["site"],
            page=context["pages"][page_key],
            publications=context["publications"],
            active=page_key,
        )
        out_path = OUT_DIR / output_rel
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(html, encoding="utf-8")

    copy_tree(STATIC_DIR, OUT_DIR / "static")
    copy_tree(ASSETS_DIR, OUT_DIR / "assets")

    # Custom domain for GitHub Pages / Cloudflare Pages
    domain = context["site"].get("domain", "drsahanawaz.com")
    (OUT_DIR / "CNAME").write_text(f"{domain}\n", encoding="utf-8")
    (OUT_DIR / ".nojekyll").write_text("", encoding="utf-8")

    print(f"Built site → {OUT_DIR}")


if __name__ == "__main__":
    build()
