import pytest
from PIL import Image
from checkio1.image_conversion import (
    load_image,
    average_color,
    create_hexagon_points,
    hexagon_to_svg,
    generate_svg_hexagon,
    generate_svg_aligned
)

@pytest.fixture
def sample_image():
    return Image.new('RGB', (100, 100), (255, 0, 0)) 

#Test Load Image
def test_load_image():
    image = load_image('screenshot.png')
    assert isinstance(image, Image.Image), "Expected a PIL Image object"

#Test Average Color
def test_average_color(sample_image):
    color = average_color(sample_image, 0, 0, 10, 10)
    assert color == (255, 0, 0), "Expected red color (255, 0, 0) in the selected region"

def test_average_color_empty_region(sample_image):
    color = average_color(sample_image, 110, 110, 120, 120)
    assert color == (255, 255, 255), "Expected default white color for out-of-bounds region"

#Test Create Hexagon Points
def test_create_hexagon_points():
    points = create_hexagon_points(100, 100, 15)
    assert len(points) == 6, "Expected 6 points for a hexagon"

#Test Hexagon to SVG
def test_hexagon_to_svg():
    points = create_hexagon_points(100, 100, 15)
    svg_hex = hexagon_to_svg(points, (255, 255, 255))
    assert 'rgb(255,255,255)' in svg_hex, "Expected white fill color in the SVG hexagon"
    assert '<polygon' in svg_hex, "Expected the SVG element to be a polygon"

#Test Generate SVG Hexagon
def test_generate_svg_hexagon(sample_image):
    svg_hex = generate_svg_hexagon(sample_image, 50, 50, 15)
    assert 'rgb(255,0,0)' in svg_hex, "Expected the SVG hexagon to have red fill color from the sample image"

#Test Generate SVG Aligned Hexagons
def test_generate_svg_aligned(sample_image):
    width, height = sample_image.width, sample_image.height
    svg_content = generate_svg_aligned(sample_image, 15, width, height)
    assert svg_content.startswith('<svg'), "SVG content should start with an <svg> tag"
    assert svg_content.endswith('</svg>\n') or svg_content.endswith('</svg>'), "SVG content should end with a closing </svg> tag"
