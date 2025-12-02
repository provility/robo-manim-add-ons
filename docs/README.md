# Documentation Folder

This folder contains the documentation website for Robo Manim Add-ons, hosted on GitHub Pages.

## Structure

```
docs/
├── _config.yml          # Jekyll/GitHub Pages configuration
├── index.md             # Documentation homepage
├── api/                 # API reference documentation
│   └── index.md
├── examples/            # Example scenes and usage patterns
│   └── index.md
├── images/              # Screenshots and images
│   └── (place PNG/JPG files here)
└── videos/              # Demo videos
    └── (place MP4 files here)
```

## Adding Content

### Adding Images

1. Place PNG or JPG files in `docs/images/`
2. Reference them in markdown:
   ```markdown
   ![Alt text](../images/your-image.png)
   ```

### Adding Videos

1. Place MP4 files in `docs/videos/`
2. Reference them in markdown:
   ```markdown
   <video width="640" height="480" controls>
     <source src="../videos/your-video.mp4" type="video/mp4">
   </video>
   ```

### Generating Demo Videos

Use Manim to generate demo videos:

```bash
# From the project root
cd examples

# Render a scene
manim -pqh demo.py DemoScene

# Copy output to docs
cp media/videos/demo/1080p60/DemoScene.mp4 ../docs/videos/demo_scene.mp4
```

### Generating Thumbnails

Extract a frame from a video as a thumbnail:

```bash
# Using ffmpeg
ffmpeg -i docs/videos/demo.mp4 -ss 00:00:01 -frames:v 1 docs/images/demo.png
```

## Viewing Locally

### Option 1: Using Jekyll locally

```bash
# Install Jekyll (one time)
gem install jekyll bundler

# Serve the docs
cd docs
jekyll serve

# Visit http://localhost:4000
```

### Option 2: Using Python HTTP server

```bash
cd docs
python -m http.server 8000

# Visit http://localhost:8000
```

## Deployment

Documentation is automatically deployed to GitHub Pages when changes are pushed to the `main` branch.

### Setting up GitHub Pages

1. Go to your repository settings
2. Navigate to **Pages** section
3. Under **Source**, select **GitHub Actions**
4. The workflow in `.github/workflows/deploy-docs.yml` will handle deployment

### Accessing Published Docs

After deployment, your documentation will be available at:
```
https://provility.github.io/robo-manim-add-ons/
```

### Manual Deployment

You can manually trigger deployment:
1. Go to **Actions** tab in GitHub
2. Select **Deploy Documentation to GitHub Pages**
3. Click **Run workflow**

## Customization

### Changing Theme

Edit `_config.yml`:
```yaml
theme: jekyll-theme-minimal  # or other GitHub Pages themes
```

Available themes:
- jekyll-theme-cayman (current)
- jekyll-theme-minimal
- jekyll-theme-slate
- jekyll-theme-architect
- jekyll-theme-modernist

### Adding Navigation

Edit `_config.yml` to add more navigation items:
```yaml
navigation:
  - title: Your Page
    url: /your-page/
```

## Tips

1. **Keep videos small** - Compress MP4 files to reduce repository size
2. **Use relative paths** - Reference images/videos with relative paths (e.g., `../images/`)
3. **Test locally first** - Preview changes locally before pushing
4. **Name files clearly** - Use descriptive names for images and videos

## Markdown Features

GitHub Pages supports:
- Code syntax highlighting
- Tables
- Emoji :rocket:
- Math equations (with KaTeX)
- HTML embedding

Example code block with syntax highlighting:
```python
from manim import *
from robo_manim_add_ons import CustomCircle

class Demo(Scene):
    def construct(self):
        circle = CustomCircle()
        self.play(Create(circle))
```
