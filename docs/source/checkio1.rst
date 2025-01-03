checkio1.image_conversion
==========================

This module processes an input image (`screenshot.png`) to generate a scalable SVG file (`output.svg`).

Functions
---------
.. autofunction:: checkio1.image_conversion.load_image
.. autofunction:: checkio1.image_conversion.average_color
.. autofunction:: checkio1.image_conversion.create_hexagon_points
.. autofunction:: checkio1.image_conversion.hexagon_to_svg
.. autofunction:: checkio1.image_conversion.generate_svg_hexagon
.. autofunction:: checkio1.image_conversion.generate_svg_aligned
.. autofunction:: checkio1.image_conversion.save_svg_to_file

Example Usage
-------------
Generate an SVG from an input PNG file:

```python
from checkio1.image_conversion import load_image, generate_svg_aligned, save_svg_to_file

image = load_image('screenshot.png')
svg_content = generate_svg_aligned(image, hex_size=15, width=image.width, height=image.height)
save_svg_to_file(svg_content, 'output.svg')
