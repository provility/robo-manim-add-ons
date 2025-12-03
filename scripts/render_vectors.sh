#!/bin/bash

cd /Users/ashraf/manim-ws/robo-manim-add-ons/demos/vectors

echo "=== RENDERING VECTOR DEMOS ==="
echo ""

total_scenes=0

for file in *.py; do
    echo "Rendering $file..."
    scene_count=$(manim -ql "$file" -a 2>&1 | grep "Rendered " | wc -l | tr -d ' ')
    echo "  ✓ $scene_count scenes"
    total_scenes=$((total_scenes + scene_count))
    echo ""
done

echo "=== EXTRACTING PNG PREVIEWS (LAST FRAME) ==="
for mp4 in *.mp4; do
    if [ -f "$mp4" ]; then
        png="${mp4%.mp4}.png"
        ffmpeg -sseof -0.001 -i "$mp4" -vframes 1 -q:v 2 "$png" -y 2>&1 | grep -q "error" || echo "✓ $png"
    fi
done

echo ""
echo "=== SUMMARY ==="
echo "Total scenes rendered: $total_scenes"
echo "Total videos: $(ls -1 *.mp4 2>/dev/null | wc -l | tr -d ' ')"
echo "Total previews: $(ls -1 *.png 2>/dev/null | wc -l | tr -d ' ')"
