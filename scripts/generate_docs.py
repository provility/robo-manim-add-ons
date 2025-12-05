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
    "arrows": {
        "title": "Arrow Demos",
        "icon": "➡️",
        "description": "Advanced arrow utilities with dashing, curves, perpendicular offsets, and markers",
        "count": 8
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
    },
    "exp": {
        "title": "Expression Utilities",
        "icon": "⚙️",
        "description": "Utility functions for extracting coordinates, creating points, and working with Manim objects",
        "count": 20
    }
}


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Robo Manim Add-ons</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/python.min.js"></script>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.5;
            color: #24292e;
            background: #ffffff;
            font-size: 14px;
        }}
        .header {{
            background: #f6f8fa;
            border-bottom: 1px solid #d0d7de;
            padding: 12px 16px;
        }}
        .header-content {{
            max-width: 1280px;
            margin: 0 auto;
        }}
        .back-link {{
            color: #0969da;
            text-decoration: none;
            font-size: 14px;
        }}
        .back-link:hover {{
            text-decoration: underline;
        }}
        h1 {{
            font-size: 20px;
            font-weight: 600;
            margin: 8px 0 4px 0;
        }}
        .subtitle {{
            color: #57606a;
            font-size: 14px;
        }}
        .container {{
            max-width: 1280px;
            margin: 0 auto;
            padding: 16px;
        }}
        .demo-grid {{
            display: grid;
            gap: 24px;
        }}
        .demo-card {{
            border: 1px solid #d0d7de;
            border-radius: 6px;
            background: #ffffff;
        }}
        .demo-content {{
            padding: 16px;
        }}
        .demo-title {{
            font-size: 16px;
            font-weight: 600;
            color: #24292e;
            margin-bottom: 4px;
        }}
        .demo-description {{
            color: #57606a;
            margin-bottom: 12px;
            font-size: 14px;
        }}
        .media-row {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
            margin-bottom: 12px;
        }}
        .media-item {{
            border: 1px solid #d0d7de;
            border-radius: 6px;
            overflow: hidden;
        }}
        .media-item img {{
            width: 100%;
            display: block;
        }}
        video {{
            width: 100%;
            display: block;
        }}
        .media-label {{
            font-size: 12px;
            color: #57606a;
            margin-bottom: 4px;
            font-weight: 500;
        }}
        .code-section {{
            background: #f6f8fa;
            border: 1px solid #d0d7de;
            border-radius: 6px;
            padding: 12px;
            position: relative;
        }}
        .code-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 8px;
        }}
        .code-title {{
            font-weight: 600;
            color: #24292e;
            font-size: 14px;
        }}
        .copy-button {{
            background: #ffffff;
            border: 1px solid #d0d7de;
            border-radius: 6px;
            padding: 4px 8px;
            font-size: 12px;
            color: #24292e;
            cursor: pointer;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        }}
        .copy-button:hover {{
            background: #f6f8fa;
            border-color: #0969da;
        }}
        .copy-button:active {{
            background: #e6e8ea;
        }}
        .copy-button.copied {{
            color: #1a7f37;
            border-color: #1a7f37;
        }}
        pre {{
            margin: 0;
            padding: 12px;
            border-radius: 6px;
            overflow-x: auto;
            background: #ffffff !important;
            border: 1px solid #d0d7de;
        }}
        pre code {{
            font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace;
            font-size: 12px;
            line-height: 1.5;
            background: transparent !important;
            padding: 0 !important;
        }}
        code {{
            font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace;
        }}
        .github-link {{
            position: fixed;
            top: 12px;
            right: 16px;
            background: #24292e;
            color: #ffffff;
            padding: 6px 12px;
            border-radius: 6px;
            text-decoration: none;
            font-size: 14px;
            font-weight: 500;
        }}
        .github-link:hover {{
            background: #57606a;
        }}
    </style>
</head>
<body>
    <a href="https://github.com/provility/robo-manim-add-ons" class="github-link">GitHub →</a>

    <div class="header">
        <div class="header-content">
            <a href="index.html" class="back-link">← Back</a>
            <h1>{title}</h1>
            <p class="subtitle">{description}</p>
        </div>
    </div>

    <div class="container">
        <div class="demo-grid">
            {demos}
        </div>
    </div>

    <script>
        // Initialize syntax highlighting
        hljs.highlightAll();

        // Copy button functionality
        function copyCode(button) {{
            const codeBlock = button.closest('.code-section').querySelector('code');
            const text = codeBlock.textContent;

            navigator.clipboard.writeText(text).then(() => {{
                const originalText = button.textContent;
                button.textContent = 'Copied!';
                button.classList.add('copied');

                setTimeout(() => {{
                    button.textContent = originalText;
                    button.classList.remove('copied');
                }}, 2000);
            }});
        }}
    </script>
</body>
</html>
"""


DEMO_CARD_TEMPLATE = """            <!-- {demo_name} -->
            <div class="demo-card">
                <div class="demo-content">
                    <h2 class="demo-title">{demo_name}</h2>
                    <p class="demo-description">{demo_desc}</p>

                    <div class="media-row">
                        <div>
                            <div class="media-label">Preview</div>
                            <div class="media-item">
                                <img src="https://raw.githubusercontent.com/provility/robo-manim-add-ons/main/demos/{category}/{png_file}" alt="{demo_name} preview">
                            </div>
                        </div>
                        <div>
                            <div class="media-label">Video</div>
                            <div class="media-item">
                                <video controls>
                                    <source src="https://raw.githubusercontent.com/provility/robo-manim-add-ons/main/demos/{category}/{video_file}" type="video/mp4">
                                </video>
                            </div>
                        </div>
                    </div>

                    <div class="code-section">
                        <div class="code-header">
                            <div class="code-title">Code Example</div>
                            <button class="copy-button" onclick="copyCode(this)">Copy</button>
                        </div>
                        <pre><code class="language-python">{code_snippet}</code></pre>
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


def extract_demo_info(category, demo_name):
    """Extract description from INDEX.md and code from source .py file."""
    import re

    # Get description from INDEX.md
    index_file = Path(__file__).parent.parent / "demos" / category / "INDEX.md"
    description = f"Demo: {demo_name}"

    if index_file.exists():
        content = index_file.read_text()
        pattern = rf"##\s+{re.escape(demo_name)}\s*\n\*\*(.+?)\*\*"
        match = re.search(pattern, content)
        if match:
            description = match.group(1)

    # Extract code from source Python file in demos directory
    demos_dir = Path(__file__).parent.parent / "demos" / category
    code = f"# Code not found for {demo_name}"

    for examples_dir in [demos_dir]:
        if not examples_dir.exists():
            continue

        for py_file in examples_dir.glob("*.py"):
            try:
                source = py_file.read_text()

                # Check if this file contains the scene class
                if f"class {demo_name}(Scene)" in source:
                    # Extract the entire class using simple text parsing
                    lines = source.split('\n')

                    # Find class start
                    class_start = None
                    for i, line in enumerate(lines):
                        if f"class {demo_name}(Scene):" in line:
                            class_start = i
                            break

                    if class_start is not None:
                        # Find construct method
                        construct_start = None
                        for i in range(class_start, len(lines)):
                            if 'def construct(self):' in lines[i]:
                                construct_start = i + 1  # Start after the def line
                                break

                        if construct_start is not None:
                            # Extract construct body until next method or class end
                            construct_body = []
                            base_indent = None

                            for i in range(construct_start, len(lines)):
                                line = lines[i]

                                # Stop at next method definition or empty class
                                if line.strip() and not line.startswith(' ' * 4):
                                    break
                                if line.strip().startswith('def ') and i > construct_start:
                                    break

                                # Set base indentation from first non-empty line
                                if base_indent is None and line.strip():
                                    base_indent = len(line) - len(line.lstrip())

                                # Add line with dedented content
                                if base_indent is not None:
                                    if line.strip():
                                        dedented = line[base_indent:] if len(line) >= base_indent else line
                                        construct_body.append(dedented)
                                    else:
                                        construct_body.append('')

                            if construct_body:
                                # Remove trailing empty lines
                                while construct_body and not construct_body[-1].strip():
                                    construct_body.pop()
                                code = '\n'.join(construct_body)
                                break
            except Exception as e:
                print(f"  Warning: Could not extract code for {demo_name}: {e}")
                continue

        # If we found the code, stop searching other directories
        if code and not code.startswith("# Code not found"):
            break

    return {"description": description, "code": code}


def generate_category_page(category, config):
    """Generate HTML page for a category."""

    # Get demo videos
    demo_names = get_demos_from_directory(category)

    # Generate demo cards
    demo_cards = []
    for demo_name in demo_names:
        # Extract real description and code from INDEX.md
        info = extract_demo_info(category, demo_name)

        card = DEMO_CARD_TEMPLATE.format(
            demo_name=demo_name,
            demo_desc=info["description"],
            category=category,
            video_file=f"{demo_name}.mp4",
            png_file=f"{demo_name}.png",
            code_snippet=info["code"]
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
