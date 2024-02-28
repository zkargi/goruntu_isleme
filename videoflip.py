
import cv2
import numpy as np

def yatay_ayna(goruntu):
    yukseklik, genislik = goruntu.shape[:2]
    aynalanmis_goruntu = np.zeros_like(goruntu, dtype=np.uint8)

    for y in range(yukseklik):
        for x in range(genislik):
            aynalanmis_goruntu[y, x] = goruntu[y, genislik - 1 - x]

    return aynalanmis_goruntu

# Örnek kullanım
original_goruntu = cv2.imread('resim.png')
aynalanmis_goruntu = yatay_ayna(original_goruntu)

cv2.imshow('Original Görüntü', original_goruntu)
cv2.imshow('Yatayda Aynalanmış Görüntü', aynalanmis_goruntu)
cv2.waitKey(0)
cv2.destroyAllWindows()
