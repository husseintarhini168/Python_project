from PIL import Image
import math

HEX_SIZE = 15  

def load_image(file_path: str) -> Image.Image:
    """Load an image from a given file path."""
    return Image.open(file_path)

def average_color(image, x_start, y_start, x_end, y_end):
    """Calculate the average color of a region in the image."""
    pixels = []
    for x in range(x_start, x_end):
        for y in range(y_start, y_end):
            if x < image.width and y < image.height:
                pixels.append(image.getpixel((x, y)))
    
    if not pixels:
        return (255, 255, 255) 
    
    r_avg = sum([p[0] for p in pixels]) // len(pixels)
    g_avg = sum([p[1] for p in pixels]) // len(pixels)
    b_avg = sum([p[2] for p in pixels]) // len(pixels)
    
    return (r_avg, g_avg, b_avg)

def create_hexagon_points(x, y, size):
    """Create points for a hexagon at a given x, y coordinate and size."""
    points = []
    for i in range(6):
        angle_deg = 60 * i  # Adjust for flat-topped hexagons
        angle_rad = math.radians(angle_deg)
        points.append((x + size * math.cos(angle_rad), y + size * math.sin(angle_rad)))
    return points

def hexagon_to_svg(points, color):
    """Convert hexagon points and color to an SVG polygon element."""
    points_str = ' '.join([f'{p[0]},{p[1]}' for p in points])
    hex_color = f'rgb({color[0]},{color[1]},{color[2]})'
    return f'<polygon points="{points_str}" fill="{hex_color}" stroke="none" stroke-width="0" />\n'

def generate_svg_hexagon(image, x_hex_start, y_hex_start, hex_size):
    """Generate an SVG hexagon for a given image region."""
    avg_color = average_color(image, int(x_hex_start), int(y_hex_start),
                              int(x_hex_start + hex_size), int(y_hex_start + hex_size))
    hex_points = create_hexagon_points(x_hex_start, y_hex_start, hex_size)
    return hexagon_to_svg(hex_points, avg_color)

def generate_svg_aligned(image, hex_size, width, height):
    """Generate the entire SVG content based on hexagon patterns."""
    svg_content = f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">\n'
    
    x_offset = hex_size * 1.5  # Horizontal step between hexagons
    y_offset = math.sqrt(3) * hex_size  # Vertical step between hexagons

    # Loop through the image with the adjusted hex grid
    for y in range(0, image.height, int(y_offset)):
        for x in range(0, image.width, int(x_offset)):
            
            x_shift = hex_size * 0.75 if (x // int(x_offset)) % 2 == 1 else 0

            x_hex_start = x 
            y_hex_start = y + x_shift

            # Generate SVG hexagon and append to the content
            svg_content += generate_svg_hexagon(image, x_hex_start, y_hex_start, hex_size)
    
    svg_content += '</svg>'
    return svg_content

def save_svg_to_file(svg_content, output_filename):
    """Save the SVG content to a file."""
    with open(output_filename, 'w') as f:
        f.write(svg_content)
    print(f"SVG saved to {output_filename}")

# Main execution
if __name__ == '__main__':
    input_filename = 'screenshot.png'
    output_filename = 'output.svg'
    
    image = load_image(input_filename)
    width, height = image.width, image.height

    # Generate SVG content
    svg_content = generate_svg_aligned(image, HEX_SIZE, width, height)

    # Save SVG content to a file
    save_svg_to_file(svg_content, output_filename)