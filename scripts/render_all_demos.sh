#!/bin/bash
set -e

echo "🎬 Rendering all demos for GitHub Pages..."

# Function to render a demo and extract preview
render_demo() {
    local demo_file=$1
    local category=$2

    echo "  📹 Rendering $(basename $demo_file)..."

    # Render all scenes in the file
    cd /Users/ashraf/manim-ws/robo-manim-add-ons
    manim -ql "$demo_file" -a --format=mp4 2>&1 | grep -E "(Rendered|Scene)" || true

    # Extract PNG previews from videos
    local output_dir="media/videos/$(basename ${demo_file%.py})/480p15"
    if [ -d "$output_dir" ]; then
        for video in "$output_dir"/*.mp4; do
            if [ -f "$video" ]; then
                local scene_name=$(basename "$video" .mp4)
                local png_name="${scene_name}.png"

                # Extract last frame as PNG preview
                ffmpeg -sseof -1 -i "$video" -vframes 1 "demos/$category/$png_name" -y 2>/dev/null || true

                # Copy video to demos directory
                cp "$video" "demos/$category/" 2>/dev/null || true

                echo "    ✓ $scene_name"
            fi
        done
    fi
}

# Render vectors category
echo ""
echo "📦 VECTORS"
echo "=========="
for demo in demos/vectors/*.py; do
    render_demo "$demo" "vectors"
done

# Render geometry category
echo ""
echo "📦 GEOMETRY"
echo "==========="
for demo in demos/geometry/*.py; do
    render_demo "$demo" "geometry"
done

# Render other categories
for category in annotation labels intersection transform arrows; do
    if [ -d "demos/$category" ]; then
        echo ""
        echo "📦 $(echo $category | tr '[:lower:]' '[:upper:]')"
        echo "==========="
        for demo in demos/$category/*.py; do
            if [ -f "$demo" ]; then
                render_demo "$demo" "$category"
            fi
        done
    fi
done

echo ""
echo "✅ All demos rendered!"
echo "📊 Generating documentation..."

python scripts/generate_docs.py

echo ""
echo "🎉 Done! GitHub Pages are ready."
