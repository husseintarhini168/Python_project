from PIL import Image
import math

# Define the hexagon properties
HEX_SIZE = 10  # Reduced radius for better detail

def average_color(image, x_start, y_start, hex_size):
    """
    Calculate the average color of a hexagonal region.
    """
    pixels = []
    for x in range(x_start, x_start + hex_size):
        for y in range(y_start, y_start + hex_size):
            if x < image.width and y < image.height:
                pixels.append(image.getpixel((x, y)))
    
    # Calculate the average color
    if not pixels:
        return (255, 255, 255)  # Default white if no pixels are found
    
    r_avg = sum([p[0] for p in pixels]) // len(pixels)
    g_avg = sum([p[1] for p in pixels]) // len(pixels)
    b_avg = sum([p[2] for p in pixels]) // len(pixels)
    
    return (r_avg, g_avg, b_avg)

def hex_to_svg(x, y, size, color):
    """
    Convert hex coordinates to SVG path for a regular hexagon.
    """
    angle_deg = 60
    angle_rad = math.pi / 180 * angle_deg
    points = [
        (x + size * math.cos(angle_rad * i), y + size * math.sin(angle_rad * i)) 
        for i in range(6)
    ]
    
    points_str = ' '.join([f'{p[0]},{p[1]}' for p in points])
    hex_color = f'rgb({color[0]},{color[1]},{color[2]})'
    
    return f'<polygon points="{points_str}" fill="{hex_color}" stroke="none" />\n'

def generate_svg(image, hex_size, width, height):
    """
    Generate the SVG content by sampling hexagons from the image.
    """
    svg_content = f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">\n'
    
    # Define hexagonal grid steps
    x_offset = hex_size * 1.5
    y_offset = math.sqrt(3) * hex_size
    
    # Loop through the image using the hex grid
    for y in range(0, image.height, int(y_offset)):
        for x in range(0, image.width, int(x_offset)):
            # Shift alternate rows to form the hexagon grid
            if (y // int(y_offset)) % 2 == 1:
                x_shift = hex_size * 0.75  # Shift for alternate rows
            else:
                x_shift = 0

            # Sample the average color for the hexagon
            avg_color = average_color(image, int(x + x_shift), y, hex_size)
            # Create the hexagon in SVG
            svg_content += hex_to_svg(x + x_shift, y, hex_size, avg_color)
    
    svg_content += '</svg>'
    return svg_content

def main():
    INPUT_FILENAME = 'screenshot.png'
    OUTPUT_FILENAME = 'final_output.svg'
    
    # Load the image
    image = Image.open(INPUT_FILENAME)
    
    # Get the dimensions of the image
    width, height = image.width, image.height
    
    # Generate SVG content
    svg_content = generate_svg(image, HEX_SIZE, width, height)
    
    # Write to the output SVG file
    with open(OUTPUT_FILENAME, 'w') as f:
        f.write(svg_content)

    return OUTPUT_FILENAME

# Run the main function to generate the final SVG
if __name__ == "__main__":
    main()
