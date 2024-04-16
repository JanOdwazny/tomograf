import cv2
import tkinter as tk
from tkinter import filedialog

# import datetime
# import os

from math import degrees, radians
from pprint import pprint

import sys
import numpy as np
np.set_printoptions(threshold=sys.maxsize)
# import pydicom

# from skimage.io import imread
# from skimage.draw import circle, line
# from skimage.color import gray2rgb, rgb2gray

from scipy.fftpack import fft, ifft, fftfreq
import matplotlib.pyplot as plt


def choose_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    return tk.filedialog.askopenfilename()
    # if file_path:
    #     print("Selected file:", file_path)
    #     # Do something with the selected file path
    # else:
    #     print("No file selected.")


filename = choose_file()
# filename = "tomograf-obrazy/kolo.jpg"
img = cv2.imread(filename, 0)
img = cv2.resize(img,(512,512))
img = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)
print(img)
R = img.shape[0]/2
print(R)