#!/bin/bash
# Render all vector-related demos with updated arrow tips

set -e

# Define demo categories that use vectors
CATEGORIES=("vectors" "geometry" "transform")

for category in "${CATEGORIES[@]}"; do
    echo "Rendering $category demos..."

    # Get all demo names from the demos directory
    if [ -d "demos/$category" ]; then
        for mp4 in demos/$category/*.mp4; do
            demo_name=$(basename "$mp4" .mp4)

            # Find the corresponding example file
            example_file="examples/geometry/${demo_name}.py"

            # Try to find the scene class name in the file
            if [ -f "$example_file" ]; then
                echo "  Rendering $demo_name..."

                # Render the scene
                manim -ql "$example_file" "$demo_name" || echo "    Warning: Could not render $demo_name"

                # Copy to demos folder
                video_file="media/videos/$(basename ${example_file%.py})/480p15/${demo_name}.mp4"
                if [ -f "$video_file" ]; then
                    cp "$video_file" "demos/$category/${demo_name}.mp4"

                    # Generate PNG from last frame
                    ffmpeg -sseof -1 -i "demos/$category/${demo_name}.mp4" \
                           -update 1 -q:v 1 "demos/$category/${demo_name}.png" -y \
                           > /dev/null 2>&1

                    echo "    ✓ Updated demos/$category/${demo_name}.mp4 and .png"
                fi
            fi
        done
    fi
done

echo ""
echo "✅ Demo rendering complete!"
