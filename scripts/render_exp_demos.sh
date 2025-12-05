#!/bin/bash

# Script to render all exp utility function demos

cd /Users/ashraf/manim-ws/robo-manim-add-ons

echo "Rendering exp utility demos..."

# List of all demo scenes
scenes=(
    "XDemo"
    "YDemo"
    "StDemo"
    "EdDemo"
    "MagDemo"
    "UvDemo"
    "VecDemo"
    "AngDemo"
    "SlopeDemo"
    "ValDemo"
    "PtDemo"
    "M2vDemo"
    "V2mDemo"
    "VlDemo"
    "HlDemo"
    "LlaDemo"
    "VlaDemo"
    "LraDemo"
    "VraDemo"
    "R2pDemo"
)

# Render each scene
for scene in "${scenes[@]}"; do
    echo "Rendering $scene..."
    manim -qm --format=png demos/exp/exp_demo.py "$scene"
    manim -qm demos/exp/exp_demo.py "$scene"
done

# Move files to demos/exp directory
echo "Moving files to demos/exp..."
mkdir -p demos/exp

# Move PNG files (last frame)
if [ -d "media/images/exp_demo" ]; then
    find media/images/exp_demo -name "*.png" -exec sh -c '
        for file; do
            scene_name=$(basename "$file" | sed "s/_ManimCE_v[0-9.]*\.png//")
            cp "$file" "demos/exp/${scene_name}.png"
        done
    ' sh {} +
fi

# Move MP4 files
if [ -d "media/videos/exp_demo/720p30" ]; then
    find media/videos/exp_demo/720p30 -name "*.mp4" -exec sh -c '
        for file; do
            scene_name=$(basename "$file" .mp4)
            cp "$file" "demos/exp/${scene_name}.mp4"
        done
    ' sh {} +
fi

echo "Done! Files are in demos/exp/"
