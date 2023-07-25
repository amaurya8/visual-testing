from PIL import Image, ImageChops, ImageDraw

def compare_images(actual_image_path, baseline_image_path, diff_image_path):
    actual_image = Image.open(actual_image_path)
    baseline_image = Image.open(baseline_image_path)

    # Convert images to RGB mode (in case they are in different modes)
    actual_image = actual_image.convert("RGB")
    baseline_image = baseline_image.convert("RGB")

    # Perform pixel-by-pixel comparison
    diff = ImageChops.difference(actual_image, baseline_image).convert("RGB")

    differences = Image.new("RGB", diff.size, color="white")
    draw = ImageDraw.Draw(differences)

    for x in range(diff.width):
        for y in range(diff.height):
            pixel_diff = diff.getpixel((x, y))
            if pixel_diff != (0, 0, 0):  # If the pixel differs, add a red contour
                draw.rectangle((x, y, x + 1, y + 1), outline="red")

    # Save the diff image with discrepancies highlighted
    differences.save(diff_image_path)

    return diff.getbbox() is None

# Example usage
actual_image_path = "/Users/ashok/Desktop/Report_Explorer/actual.png"
baseline_image_path = "/Users/ashok/Desktop/Report_Explorer/baseline.png"
diff_image_path = "/Users/ashok/Desktop/Report_Explorer/diff.png"

result = compare_images(actual_image_path, baseline_image_path, diff_image_path)

if not result:
    print("Visual discrepancies found! Check the 'diff.png' image for highlights.")
else:
    print("No visual discrepancies found.")
