Python Project Documentation
============================

Welcome to the Python Project documentation! This project generates a scalable SVG version of a low-resolution PNG image by sampling colors in a hexagonal grid and reconstructing the image.

Project Description
-------------------
For this project, we aim to:
- Load an input image (`screenshot.png`).
- Use a hexagonal grid to sample colors from the image.
- Generate a scalable SVG file (`output.svg`) based on the sampled colors.
- Save the result as a high-resolution wallpaper.

Features
--------
- **Load Image**: Reads the input image using the PIL library.
- **Hexagonal Sampling**: Samples average colors of hexagons to mimic the image in SVG.
- **Scalable Output**: Outputs a resolution-independent SVG file.
- **Pythonic Implementation**: Uses Python and its ecosystem for seamless development.

Quick Start
-----------
Run the following commands to process an image:

```python
from checkio1.image_conversion import load_image, generate_svg_aligned, save_svg_to_file

image = load_image('screenshot.png')
svg_content = generate_svg_aligned(image, hex_size=15, width=image.width, height=image.height)
save_svg_to_file(svg_content, 'output.svg')
