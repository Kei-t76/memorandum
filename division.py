import os
import cv2
import numpy as np
import glob

original_file_path = "8K_NG_nondiv"
output_file_path = "8KOK_dataset"

file_path = glob.glob(original_file_path + "/*")
div_num_h = 2
div_num_w = 3

for file in file_path:
    # 拡張子抜きのファイル名取得
    dirname, basename = os.path.split(file)
    filename = os.path.splitext(basename)[0]

    # ファイル読み込み
    img = cv2.imread(file)
    # 縦横比取得
    height, width = img.shape[:2]
    # 分割時のサイズ
    h_n = int(height / div_num_h)
    w_n = int(width / div_num_w)

    for h in range(div_num_h):
        for w in range(div_num_w):
            h_div = h * h_n
            w_div = w * w_n
            crop_img = img[h_div: h_div + h_n, w_div: w_n + w_div]
            cv2.imwrite(output_file_path + "/" + filename + '_' + str(h) + '_' + str(w) +
                        '.jpg', crop_img)
