#!/usr/bin/env python3
"""Convert API.md to API.html with proper code block formatting."""

import re
from pathlib import Path


def markdown_to_html(md_content):
    """Convert markdown to HTML with proper code block handling."""
    html_parts = []
    in_code_block = False
    code_buffer = []

    lines = md_content.split('\n')
    i = 0

    while i < len(lines):
        line = lines[i]

        # Handle code blocks
        if line.strip().startswith('```'):
            if not in_code_block:
                # Start of code block
                in_code_block = True
                lang = line.strip()[3:].strip() or 'python'
                code_buffer = []
                i += 1
                continue
            else:
                # End of code block
                in_code_block = False
                code = '\n'.join(code_buffer)
                html_parts.append(f'<pre><code class="language-python">{html_escape(code)}</code></pre>\n')
                code_buffer = []
                i += 1
                continue

        if in_code_block:
            code_buffer.append(line)
            i += 1
            continue

        # Handle headers
        if line.startswith('# '):
            html_parts.append(f'<h1>{html_escape(line[2:])}</h1>\n')
        elif line.startswith('## '):
            html_parts.append(f'<h2>{html_escape(line[3:])}</h2>\n')
        elif line.startswith('### '):
            html_parts.append(f'<h3>{html_escape(line[4:])}</h3>\n')
        # Handle horizontal rules
        elif line.strip() == '---':
            html_parts.append('<hr />\n')
        # Handle bold text
        elif '**' in line:
            line = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', line)
            html_parts.append(f'<p>{html_escape_preserve_tags(line)}</p>\n')
        # Handle inline code
        elif '`' in line:
            line = re.sub(r'`([^`]+)`', r'<code>\1</code>', line)
            html_parts.append(f'<p>{html_escape_preserve_tags(line)}</p>\n')
        # Handle empty lines
        elif not line.strip():
            html_parts.append('\n')
        # Regular paragraph
        else:
            html_parts.append(f'<p>{html_escape(line)}</p>\n')

        i += 1

    return ''.join(html_parts)


def html_escape(text):
    """Escape HTML special characters."""
    return (text
            .replace('&', '&amp;')
            .replace('<', '&lt;')
            .replace('>', '&gt;')
            .replace('"', '&quot;'))


def html_escape_preserve_tags(text):
    """Escape HTML but preserve already inserted tags."""
    # This is a simple version that assumes tags are already properly formatted
    return text.replace('&', '&amp;').replace('"', '&quot;')


def main():
    """Convert API.md to API.html."""
    # Get project root
    project_root = Path(__file__).parent.parent
    api_md_path = project_root / "docs" / "API.md"
    api_html_path = project_root / "docs" / "API.html"

    # Read API.md
    print(f"Reading {api_md_path}...")
    md_content = api_md_path.read_text()

    # Convert to HTML
    print("Converting markdown to HTML...")
    body_html = markdown_to_html(md_content)

    # Wrap in full HTML template
    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>API Reference - Robo Manim Add-ons</title>
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
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.7;
            color: #1a1a1a;
            background: #ffffff;
            font-size: 16px;
            padding: 16px;
            max-width: 1400px;
            margin: 0 auto;
        }}
        h1 {{
            font-size: 42px;
            font-weight: 700;
            margin: 16px 0 12px 0;
            border-bottom: 2px solid #000;
            padding-bottom: 6px;
            color: #000;
        }}
        h2 {{
            font-size: 32px;
            font-weight: 700;
            margin: 24px 0 12px 0;
            border-bottom: 2px solid #000;
            padding-bottom: 4px;
            color: #000;
        }}
        h3 {{
            font-size: 22px;
            font-weight: 600;
            margin: 16px 0 8px 0;
            color: #000;
        }}
        p {{
            margin: 6px 0;
            line-height: 1.7;
            font-size: 16px;
        }}
        pre {{
            background: #f8f8f8;
            border: 1px solid #e0e0e0;
            border-left: 3px solid #000;
            padding: 12px;
            overflow-x: auto;
            margin: 8px 0;
        }}
        pre code {{
            font-family: 'JetBrains Mono', 'Fira Code', 'Cascadia Code', Consolas, 'Courier New', monospace;
            font-size: 15px;
            line-height: 1.6;
            background: transparent !important;
            padding: 0 !important;
            color: #000;
        }}
        code {{
            font-family: 'JetBrains Mono', 'Fira Code', 'Cascadia Code', Consolas, monospace;
            background: #f0f0f0;
            padding: 2px 5px;
            font-size: 15px;
            color: #d73a49;
            border: 1px solid #e0e0e0;
        }}
        hr {{
            border: none;
            border-top: 1px solid #ccc;
            margin: 24px 0;
        }}
        strong {{
            font-weight: 700;
            color: #000;
        }}
        .github-link {{
            position: fixed;
            top: 8px;
            right: 8px;
            background: #000;
            color: #fff;
            padding: 8px 14px;
            text-decoration: none;
            font-size: 15px;
            font-weight: 600;
            border: 2px solid #000;
        }}
        .github-link:hover {{
            background: #fff;
            color: #000;
        }}
        .back-link {{
            display: inline-block;
            color: #0366d6;
            text-decoration: none;
            margin-bottom: 12px;
            font-size: 16px;
            font-weight: 600;
        }}
        .back-link:hover {{
            text-decoration: underline;
        }}
    </style>
</head>
<body>
    <a href="https://github.com/provility/robo-manim-add-ons" class="github-link">GitHub →</a>
    <a href="index.html" class="back-link">← Back to Home</a>

{body_html}

    <script>
        // Initialize syntax highlighting
        hljs.highlightAll();
    </script>
</body>
</html>
"""

    # Write API.html
    print(f"Writing {api_html_path}...")
    api_html_path.write_text(full_html)

    print(f"\n✅ Successfully generated API.html")
    print(f"📁 Output: {api_html_path}")


if __name__ == "__main__":
    main()
