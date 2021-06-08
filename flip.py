#指定したディレクトリ下の画像の上下左右反転

import glob
import os
import cv2

path = 't' + '/*'
flist = glob.glob(path)

for file in flist:
    img = cv2.imread(file)
    print(file)
    x = cv2.flip(img, 0)
    y = cv2.flip(img, 1)
    xy = cv2.flip(img, -1)

    cv2.imwrite(file+'x'+'.jpg', x)
    cv2.imwrite(file+'y'+'.jpg', y)
    cv2.imwrite(file+'xy'+'.jpg', xy)