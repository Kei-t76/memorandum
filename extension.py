import os
import cv2
import numpy as np
import glob

file_name = "8K_NG_div_png"
new_extension = ".png"

files = glob.glob(file_name + "/*")
print(files)

for file in files:
    pre, ext = os.path.splitext(file)
    print(pre, ext)
    os.rename(file, pre + new_extension)
