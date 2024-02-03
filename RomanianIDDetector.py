import cv2
import pytesseract
import PIL
from matplotlib import pyplot as plt
import numpy as np
import re

img_path = '/content/buletin1.jpeg'
image = cv2.imread(img_path)
image = cv2.resize(image, None, fx=5, fy=5, interpolation=cv2.INTER_CUBIC)

plt.figure(figsize=(10,15))
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

# Assuming 'image' is already defined and loaded
image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

# Check if the image is not grayscale (i.e., has 3 channels)
if len(image.shape) == 3 and image.shape[2] == 3:
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

_, image = cv2.threshold(image, 130, 255, cv2.THRESH_BINARY)
image = cv2.medianBlur(image, 3)

plt.figure(figsize=(10, 15))
plt.imshow(image, cmap='gray', vmin=0, vmax=255)
plt.show()

import re


text = pytesseract.image_to_string(image)

# Regular expressions to search for desired items
cnp_pattern = r'\b\d{13}\b'  # CNP has 13 numbers
serie_pattern = r'\b[A-Z]{2}\b'  # ID Serie has 2 uppercase letters
nr_pattern = r'\b\d{6}\b'
rou_pattern = r'\bROU\b'  #'ROU' Text

# Checking if all elements are present in the text
if (re.search(cnp_pattern, text) and
    re.search(serie_pattern, text) and
    re.search(nr_pattern, text) and
    re.search(rou_pattern, text)):
    print("It's a real Romanian ID")
else:
    print("It's a fake Romanian ID")