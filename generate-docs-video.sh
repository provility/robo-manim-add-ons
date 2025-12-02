#!/bin/bash

# Helper script to generate documentation videos from Manim scenes
# Usage: ./generate-docs-video.sh <scene_file.py> <SceneName> <output_name>

set -e

if [ "$#" -lt 3 ]; then
    echo "Usage: ./generate-docs-video.sh <scene_file.py> <SceneName> <output_name>"
    echo ""
    echo "Example:"
    echo "  ./generate-docs-video.sh examples/demo.py DemoScene demo_scene"
    echo ""
    echo "This will:"
    echo "  1. Render the scene in high quality"
    echo "  2. Copy video to docs/videos/<output_name>.mp4"
    echo "  3. Generate thumbnail to docs/images/<output_name>.png"
    exit 1
fi

SCENE_FILE=$1
SCENE_NAME=$2
OUTPUT_NAME=$3

echo "📹 Rendering $SCENE_NAME from $SCENE_FILE..."

# Render the scene in high quality
manim -qh --format=mp4 "$SCENE_FILE" "$SCENE_NAME"

# Find the output video (Manim puts it in media/videos/)
# Extract directory name from scene file
DIR_NAME=$(basename "$SCENE_FILE" .py)
VIDEO_PATH="media/videos/${DIR_NAME}/1080p60/${SCENE_NAME}.mp4"

if [ ! -f "$VIDEO_PATH" ]; then
    echo "❌ Error: Video not found at $VIDEO_PATH"
    echo "Looking for video files..."
    find media/videos -name "${SCENE_NAME}.mp4" -type f
    exit 1
fi

echo "✅ Video rendered successfully"

# Copy to docs/videos
echo "📂 Copying video to docs/videos/${OUTPUT_NAME}.mp4..."
cp "$VIDEO_PATH" "docs/videos/${OUTPUT_NAME}.mp4"

# Generate thumbnail using ffmpeg
if command -v ffmpeg &> /dev/null; then
    echo "🖼️  Generating thumbnail..."
    ffmpeg -i "$VIDEO_PATH" -ss 00:00:01 -frames:v 1 "docs/images/${OUTPUT_NAME}.png" -y
    echo "✅ Thumbnail saved to docs/images/${OUTPUT_NAME}.png"
else
    echo "⚠️  ffmpeg not found - skipping thumbnail generation"
    echo "   Install with: brew install ffmpeg (macOS) or apt-get install ffmpeg (Linux)"
fi

echo ""
echo "✅ Done! Files created:"
echo "   - docs/videos/${OUTPUT_NAME}.mp4"
if command -v ffmpeg &> /dev/null; then
    echo "   - docs/images/${OUTPUT_NAME}.png"
fi
echo ""
echo "Add to your documentation with:"
echo ""
echo "![${SCENE_NAME}](../images/${OUTPUT_NAME}.png)"
echo ""
echo "<video width=\"640\" height=\"480\" controls>"
echo "  <source src=\"../videos/${OUTPUT_NAME}.mp4\" type=\"video/mp4\">"
echo "</video>"
