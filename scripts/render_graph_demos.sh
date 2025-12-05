#!/bin/bash

# Script to render all graph function demos

cd /Users/ashraf/manim-ws/robo-manim-add-ons

echo "Rendering graph demos..."

# List of all demo scenes from graph_demo.py
graph_scenes=(
    "ExplicitPlotDemo"
    "ImplicitPlotDemo"
    "ParametricPlotDemo"
    "MultipleGraphsDemo"
    "StyledAxesDemo"
    "AnimatedGraphDemo"
    "ComplexExpressionDemo"
    "CustomRangeDemo"
    "EllipseImplicitDemo"
)

# List of all demo scenes from trig_graph_demo.py
trig_scenes=(
    "AutoPiTicksDemo"
    "InverseTrigDemo"
    "ManualPiTicksDemo"
    "DisablePiTicksDemo"
    "BothAxesPiDemo"
    "MultipleTrigGraphsDemo"
    "CoarsePiTicksDemo"
    "AtanDemo"
)

# Render graph demos
for scene in "${graph_scenes[@]}"; do
    echo "Rendering $scene..."
    manim -qm --format=png demos/graphing/graph_demo.py "$scene"
    manim -qm demos/graphing/graph_demo.py "$scene"
done

# Render trig graph demos
for scene in "${trig_scenes[@]}"; do
    echo "Rendering $scene..."
    manim -qm --format=png demos/graphing/trig_graph_demo.py "$scene"
    manim -qm demos/graphing/trig_graph_demo.py "$scene"
done

# Move files to demos/graphing directory
echo "Moving files to demos/graphing..."
mkdir -p demos/graphing

# Move PNG files from graph_demo
if [ -d "media/images/graph_demo" ]; then
    find media/images/graph_demo -name "*.png" -exec sh -c '
        for file; do
            scene_name=$(basename "$file" | sed "s/_ManimCE_v[0-9.]*\.png//")
            cp "$file" "demos/graphing/${scene_name}.png"
        done
    ' sh {} +
fi

# Move MP4 files from graph_demo
if [ -d "media/videos/graph_demo/720p30" ]; then
    find media/videos/graph_demo/720p30 -name "*.mp4" -exec sh -c '
        for file; do
            scene_name=$(basename "$file" .mp4)
            cp "$file" "demos/graphing/${scene_name}.mp4"
        done
    ' sh {} +
fi

# Move PNG files from trig_graph_demo
if [ -d "media/images/trig_graph_demo" ]; then
    find media/images/trig_graph_demo -name "*.png" -exec sh -c '
        for file; do
            scene_name=$(basename "$file" | sed "s/_ManimCE_v[0-9.]*\.png//")
            cp "$file" "demos/graphing/${scene_name}.png"
        done
    ' sh {} +
fi

# Move MP4 files from trig_graph_demo
if [ -d "media/videos/trig_graph_demo/720p30" ]; then
    find media/videos/trig_graph_demo/720p30 -name "*.mp4" -exec sh -c '
        for file; do
            scene_name=$(basename "$file" .mp4)
            cp "$file" "demos/graphing/${scene_name}.mp4"
        done
    ' sh {} +
fi

echo "Done! Files are in demos/graphing/"
