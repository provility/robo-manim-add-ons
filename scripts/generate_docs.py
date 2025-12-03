#!/usr/bin/env python3
"""
Generate GitHub Pages documentation from demo files.

This script reads demo metadata and generates HTML pages with inline video players.
"""

import os
from pathlib import Path
import json


# Demo categories configuration
CATEGORIES = {
    "geometry": {
        "title": "Geometry Demos",
        "icon": "🔷",
        "description": "Perpendicular and parallel line construction utilities",
        "count": 10
    },
    "vectors": {
        "title": "Vector Demos",
        "icon": "🔢",
        "description": "Vector operations including projection, decomposition, and transformations",
        "count": 18
    },
    "annotation": {
        "title": "Annotation Demos",
        "icon": "📏",
        "description": "Distance markers and geometric annotation utilities",
        "count": 7
    },
    "labels": {
        "title": "Label Demos",
        "icon": "🏷️",
        "description": "Vertex and edge labeling for polygons",
        "count": 5
    },
    "intersection": {
        "title": "Intersection Demos",
        "icon": "⚡",
        "description": "Line-line and line-circle intersection utilities",
        "count": 6
    },
    "transform": {
        "title": "Transform Demos",
        "icon": "🔄",
        "description": "Vector transformation utilities (translated, rotated, scaled)",
        "count": 6
    }
}


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Robo Manim Add-ons</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            background: #f8f9fa;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 2rem;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        .header-content {{
            max-width: 1200px;
            margin: 0 auto;
        }}
        .back-link {{
            color: white;
            text-decoration: none;
            display: inline-block;
            margin-bottom: 1rem;
            opacity: 0.9;
        }}
        .back-link:hover {{
            opacity: 1;
        }}
        h1 {{
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
        }}
        .subtitle {{
            opacity: 0.9;
            font-size: 1.1rem;
        }}
        .container {{
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 2rem;
        }}
        .demo-grid {{
            display: grid;
            gap: 3rem;
        }}
        .demo-card {{
            background: white;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }}
        .demo-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 8px 15px rgba(0,0,0,0.2);
        }}
        .demo-content {{
            padding: 2rem;
        }}
        .demo-title {{
            font-size: 1.8rem;
            color: #667eea;
            margin-bottom: 0.5rem;
        }}
        .demo-description {{
            color: #666;
            margin-bottom: 1.5rem;
            font-size: 1.1rem;
        }}
        video {{
            width: 100%;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            margin-bottom: 1.5rem;
        }}
        .code-section {{
            background: #f8f9fa;
            border-radius: 8px;
            padding: 1.5rem;
            border-left: 4px solid #667eea;
        }}
        .code-title {{
            font-weight: bold;
            margin-bottom: 0.5rem;
            color: #333;
        }}
        pre {{
            background: #2d2d2d;
            color: #f8f8f2;
            padding: 1rem;
            border-radius: 6px;
            overflow-x: auto;
            font-size: 0.9rem;
            line-height: 1.5;
        }}
        code {{
            font-family: 'Monaco', 'Menlo', 'Courier New', monospace;
        }}
        .github-badge {{
            position: fixed;
            top: 20px;
            right: 20px;
            background: white;
            padding: 0.75rem 1.5rem;
            border-radius: 25px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.15);
            text-decoration: none;
            color: #667eea;
            font-weight: bold;
            transition: transform 0.2s;
        }}
        .github-badge:hover {{
            transform: scale(1.05);
        }}
    </style>
</head>
<body>
    <a href="https://github.com/provility/robo-manim-add-ons" class="github-badge">⭐ GitHub</a>

    <div class="header">
        <div class="header-content">
            <a href="index.html" class="back-link">← Back to Gallery</a>
            <h1>{icon} {title}</h1>
            <p class="subtitle">{description}</p>
        </div>
    </div>

    <div class="container">
        <div class="demo-grid">
            {demos}
        </div>
    </div>
</body>
</html>
"""


DEMO_CARD_TEMPLATE = """            <!-- {demo_name} -->
            <div class="demo-card">
                <div class="demo-content">
                    <h2 class="demo-title">{demo_name}</h2>
                    <p class="demo-description">{demo_desc}</p>

                    <video controls>
                        <source src="../demos/{category}/{video_file}" type="video/mp4">
                        Your browser does not support the video tag.
                    </video>

                    <div class="code-section">
                        <div class="code-title">Code Example:</div>
                        <pre><code>{code_snippet}</code></pre>
                    </div>
                </div>
            </div>"""


def get_demos_from_directory(category):
    """Get list of demo videos from demos directory."""
    demos_dir = Path(__file__).parent.parent / "demos" / category

    if not demos_dir.exists():
        return []

    videos = sorted([f.stem for f in demos_dir.glob("*.mp4")])
    return videos


def generate_category_page(category, config):
    """Generate HTML page for a category."""

    # Get demo videos
    demo_names = get_demos_from_directory(category)

    # Generate demo cards
    demo_cards = []
    for demo_name in demo_names:
        card = DEMO_CARD_TEMPLATE.format(
            demo_name=demo_name,
            demo_desc=f"Demo: {demo_name}",
            category=category,
            video_file=f"{demo_name}.mp4",
            code_snippet=f"# Code for {demo_name}\n# See examples/{category}/ for full source"
        )
        demo_cards.append(card)

    # Generate full page
    html = HTML_TEMPLATE.format(
        title=config["title"],
        icon=config["icon"],
        description=config["description"],
        demos="\n\n".join(demo_cards)
    )

    return html


def main():
    """Generate all documentation pages."""

    # Get project root
    project_root = Path(__file__).parent.parent
    docs_dir = project_root / "docs"

    # Create docs directory if it doesn't exist
    docs_dir.mkdir(exist_ok=True)

    # Generate category pages
    for category, config in CATEGORIES.items():
        print(f"Generating {category}.html...")

        html = generate_category_page(category, config)

        output_file = docs_dir / f"{category}.html"
        output_file.write_text(html)

        print(f"  ✓ Created {output_file}")

    print(f"\n✅ Generated {len(CATEGORIES)} category pages")
    print(f"📁 Output directory: {docs_dir}")
    print("\nTo view locally:")
    print(f"  cd {docs_dir}")
    print("  python -m http.server 8000")
    print("  Open http://localhost:8000")


if __name__ == "__main__":
    main()
