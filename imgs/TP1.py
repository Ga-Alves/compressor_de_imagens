import cv2
import sys
import matplotlib.pyplot as plt

inptFile = sys.argv[1]

img = cv2.imread(inptFile, cv2.IMREAD_GRAYSCALE)

plt.imshow(img, cmap='gray')
