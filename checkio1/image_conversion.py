from PIL import Image
import math

HEX_SIZE = 15  
# Load the image
input_filename = 'screenshot.png'  
image = Image.open(input_filename)

def average_color(image, x_start, y_start, x_end, y_end):
    """Calculate the average color of a region."""
    pixels = []
    for x in range(x_start, x_end):
        for y in range(y_start, y_end):
            if x < image.width and y < image.height:
                pixels.append(image.getpixel((x, y)))
    
    if not pixels:
        # Default to white if no pixels
        return (255, 255, 255)  
    
    r_avg = sum([p[0] for p in pixels]) // len(pixels)
    g_avg = sum([p[1] for p in pixels]) // len(pixels)
    b_avg = sum([p[2] for p in pixels]) // len(pixels)
    
    return (r_avg, g_avg, b_avg)

def hexagon_to_svg(x, y, size, color):
    points = []
    for i in range(6):
        angle_deg = 60 * i  # Adjust for flat-topped hexagons
        angle_rad = math.radians(angle_deg)
        points.append((x + size * math.cos(angle_rad), y + size * math.sin(angle_rad)))

    points_str = ' '.join([f'{p[0]},{p[1]}' for p in points])
    hex_color = f'rgb({color[0]},{color[1]},{color[2]})'
    
    return f'<polygon points="{points_str}" fill="{hex_color}" stroke="none" stroke-width="0" />\n'

def generate_svg_aligned(image, hex_size, width, height):
    svg_content = f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">\n'
    
    
    x_offset = hex_size * 1.5  # Horizontal step between hexagons
    y_offset = math.sqrt(3) * hex_size  # Vertical step between hexagons

    # Loop through the image with the adjusted hex grid
    for y in range(0, image.height, int(y_offset)):
        for x in range(0, image.width, int(x_offset)):
            
            if (x // int(x_offset)) % 2 == 1:
                x_shift = hex_size * 0.75  # Shifting rows
            else:
                x_shift = 0

            x_hex_start = x 
            y_hex_start = y + x_shift

            # Sample the color for this hexagon
            avg_color = average_color(image, int(x_hex_start), int(y_hex_start),
                                      int(x_hex_start + hex_size), int(y_hex_start + hex_size))
            
            # Create the hexagon in SVG
            svg_content += hexagon_to_svg(x_hex_start, y_hex_start, hex_size, avg_color)
    
    svg_content += '</svg>'
    return svg_content

# Get dimensions of the image
width, height = image.width, image.height

# Generate SVG content with the adjusted hexagon alignment
svg_content_aligned = generate_svg_aligned(image, HEX_SIZE, width, height)

# Define output file path
output_filename = 'output.svg' 

with open(output_filename, 'w') as f:
    f.write(svg_content_aligned)
print(f"SVG saved to {output_filename}")
