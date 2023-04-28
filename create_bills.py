import os
import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

# Set the path to the certificate template image
CERTIFICATE_TEMPLATE_PATH = "certificate-template.jpg"

# Set the path to the text file containing names
NAMES_FILE_PATH = "name-data.txt"

# Set the path where the generated certificates will be saved
CERTIFICATES_DIR = "sample_data"

# Create the certificates directory if it doesn't already exist
os.makedirs(CERTIFICATES_DIR, exist_ok=True)

# Load the certificate template image
certificate_template_image = cv2.imread(CERTIFICATE_TEMPLATE_PATH)

# Set the font parameters
#font_path = "/home/abc/Downloads/MaiyaRegular.ttf"
font_path = "/home/abc/Downloads/MangalRegular.ttf"
font_size = 50
font_color = (0, 0, 150)
font = ImageFont.truetype(font_path, font_size)

# Read the names from the text file
with open(NAMES_FILE_PATH) as f:
    names = [line.strip() for line in f]

# Add the names to the certificate template image and save as a new image
for name in names:
    certificate_image = certificate_template_image.copy()

    # Create a PIL ImageDraw object to draw the name on the certificate image
    pil_image = Image.fromarray(cv2.cvtColor(certificate_image, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(pil_image)

    # Calculate the position of the name based on the font size and the size of the image
    name_width, name_height = draw.textsize(name, font=font)
    x = 659
    y = 395
    #x = int((certificate_image.shape[1] - name_width) / 2)
    #y = int((certificate_image.shape[0] - name_height) / 2)

    # Draw the name on the certificate image using the PIL ImageDraw object
    draw.text((x, y), name, font=font, fill=font_color)

    # Convert the PIL image back to a NumPy array and save the certificate image
    certificate_image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
    certificate_path = os.path.join(CERTIFICATES_DIR, f"{name}.jpg")
    cv2.imwrite(certificate_path, certificate_image)
    print(f"Generated certificate for {name}: {certificate_path}")