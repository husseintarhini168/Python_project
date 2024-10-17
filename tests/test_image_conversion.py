import pytest
from PIL import Image
from checkio1.image_conversion import(
    average_color,
    hexagon_to_svg
)  

# Load an example image
image = Image.new('RGB', (100, 100), (255, 0, 0)) 

def test_average_color():
    color = average_color(image, 0, 0, 10, 10)
    
    assert color == (255, 0, 0), "The color should be (255, 0, 0)."

def test_hexagon_to_svg():
    x, y, size = 100, 100, 15
    color = (255, 255, 255)  

    svg_hex = hexagon_to_svg(x, y, size, color)

    assert 'rgb(255,255,255)' in svg_hex, "SVG hexagon should be white."
