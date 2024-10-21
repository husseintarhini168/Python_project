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

"""
This module contains tests for image conversion functions using PIL and SVG generation.
"""

@pytest.fixture
def sample_image():
    """Create a red sample image for testing."""
    return Image.new('RGB', (100, 100), (255, 0, 0))

# Test Load Image
def test_load_image():
    """Test that an image is loaded correctly using load_image function."""
    image = load_image('screenshot.png')
    assert isinstance(image, Image.Image), "Expected a PIL Image object"

# Test Average Color
def test_average_color(sample_image):
    """Test that the average color function returns the correct color."""
    color = average_color(sample_image, 0, 0, 10, 10)
    assert color == (255, 0, 0), "Expected red color (255, 0, 0) in the selected region"

def test_average_color_empty_region(sample_image):
    """Test that out-of-bounds regions return a default white color."""
    color = average_color(sample_image, 110, 110, 120, 120)
    assert color == (255, 255, 255), \
        "Expected default white color for out-of-bounds region"

# Test Create Hexagon Points
def test_create_hexagon_points():
    """Test that the function creates 6 points for a hexagon."""
    points = create_hexagon_points(100, 100, 15)
    assert len(points) == 6, "Expected 6 points for a hexagon"

# Test Hexagon to SVG
def test_hexagon_to_svg():
    """Test that hexagon SVG is generated with correct color."""
    points = create_hexagon_points(100, 100, 15)
    svg_hex = hexagon_to_svg(points, (255, 255, 255))
    assert 'rgb(255,255,255)' in svg_hex, "Expected white fill color in the SVG hexagon"
    assert '<polygon' in svg_hex, "Expected the SVG element to be a polygon"

# Test Generate SVG Hexagon
def test_generate_svg_hexagon(image_sample):
    """Test that SVG hexagon is generated with red fill color from the sample image."""
    svg_hex = generate_svg_hexagon(image_sample, 50, 50, 15)
    assert 'rgb(255,0,0)' in svg_hex, "Expected the SVG hexagon to have red fill color from the sample image"

# Test Generate SVG Aligned Hexagons
def test_generate_svg_aligned(image_sample):
    """Test that SVG content is generated correctly with aligned hexagons."""
    width, height = image_sample.width, image_sample.height
    svg_content = generate_svg_aligned(image_sample, 15, width, height)
    assert svg_content.startswith('<svg'), "SVG content should start with an <svg> tag"
    assert svg_content.endswith('</svg>\n') or \
        svg_content.endswith('</svg>'), \
        "SVG content should end with a closing </svg> tag"
