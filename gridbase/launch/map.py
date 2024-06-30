import cv2
import numpy as np

# PGMファイルの読み込み
map_image = cv2.imread('/home/morita/ros2_ws/result/map.pgm', cv2.IMREAD_GRAYSCALE)

# 占有グリッドマップの二値化
threshold = 127
_, binary_map = cv2.threshold(map_image, threshold, 255, cv2.THRESH_BINARY)
