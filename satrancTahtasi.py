import cv2
import numpy as np

rows, cols = 8, 8

# Kare boyutu
square_size = 50

# Satranç tahtasını oluştur
chessboard = np.zeros((rows * square_size, cols * square_size), dtype=np.uint8)

# Satranç tahtasını doldur
for i in range(rows):
    for j in range(cols):
        if (i + j) % 2 == 0:
            chessboard[i * square_size:(i + 1) * square_size, j * square_size:(j + 1) * square_size] = 255

# Pencereyi oluştur
cv2.namedWindow("Chessboard", cv2.WINDOW_NORMAL)

# Satranç tahtasını ekrana göster
cv2.imshow("Chessboard", chessboard)

# Bekle
cv2.waitKey(0)

# Pencereyi kapat
cv2.destroyAllWindows()
