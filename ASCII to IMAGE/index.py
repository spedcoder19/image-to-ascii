from PIL import Image

# Define ASCII characters from dark to light.
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width=100):
    """
    Resizes the image preserving the aspect ratio.
    The factor 0.55 is used to adjust for the typical height/width ratio of characters.
    """
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.55)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayify(image):
    """
    Converts the image to grayscale.
    """
    return image.convert("L")

def pixels_to_ascii(image):
    """
    Maps each pixel to an ASCII character based on its intensity.
    """
    pixels = image.getdata()
    # Divide by 25 to map 0-255 range to 11 characters in ASCII_CHARS
    ascii_str = "".join(ASCII_CHARS[pixel // 25] for pixel in pixels)
    return ascii_str

def convert_image_to_ascii(path, new_width=100):
    """
    Open image, convert to ASCII art and return the string.
    """
    try:
        image = Image.open(path)
    except Exception as e:
        print(f"Unable to open image file {path}.")
        print(e)
        return ""

    # Process image
    image = resize_image(image, new_width)
    image = grayify(image)

    ascii_str = pixels_to_ascii(image)
    img_width = image.width
    ascii_art = ""
    # Split the string based on image width
    for i in range(0, len(ascii_str), img_width):
        ascii_art += ascii_str[i:i+img_width] + "\n"
    return ascii_art

if __name__ == '__main__':
    # Ask user for the path to an image file and desired width
    image_path = input("Enter the path to the image file: ")
    width_input = input("Enter desired width (default is 100): ")
    new_width = int(width_input) if width_input.isdigit() else 100

    ascii_art = convert_image_to_ascii(image_path, new_width)
    if ascii_art:
        print(ascii_art)
        # Optionally save the ASCII art to a file
        with open("ascii_image.txt", "w") as f:
            f.write(ascii_art)
        print("ASCII art written to ascii_image.txt")
