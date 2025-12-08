#!/bin/bash
# SVGをPNGに変換するスクリプト

cd "$(dirname "$0")"

echo "Converting YANA avatar SVGs to PNGs..."

# rsvg-convertを使用（librsvg2-binパッケージ）
if command -v rsvg-convert &> /dev/null; then
    rsvg-convert -w 140 -h 140 yana_idle.svg -o yana_idle.png
    rsvg-convert -w 140 -h 140 yana_talk.svg -o yana_talk.png
    echo "✅ Converted using rsvg-convert"
# Inkscapeを使用
elif command -v inkscape &> /dev/null; then
    inkscape --export-type=png --export-filename=yana_idle.png -w 140 -h 140 yana_idle.svg
    inkscape --export-type=png --export-filename=yana_talk.png -w 140 -h 140 yana_talk.svg
    echo "✅ Converted using Inkscape"
# ImageMagickを使用
elif command -v convert &> /dev/null; then
    convert -background none yana_idle.svg yana_idle.png
    convert -background none yana_talk.svg yana_talk.png
    echo "✅ Converted using ImageMagick"
# Pythonのcairosvgを使用
elif python3 -c "import cairosvg" 2>/dev/null; then
    python3 -c "
import cairosvg
cairosvg.svg2png(url='yana_idle.svg', write_to='yana_idle.png', output_width=140, output_height=140)
cairosvg.svg2png(url='yana_talk.svg', write_to='yana_talk.png', output_width=140, output_height=140)
print('✅ Converted using cairosvg')
"
else
    echo "❌ No SVG converter found!"
    echo "Install one of:"
    echo "  sudo apt install librsvg2-bin"
    echo "  sudo apt install inkscape"
    echo "  sudo apt install imagemagick"
    echo "  pip install cairosvg"
    exit 1
fi

echo ""
echo "Done! Files created:"
ls -la yana_*.png 2>/dev/null || echo "No PNG files found"
