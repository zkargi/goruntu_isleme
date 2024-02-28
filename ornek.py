"""
fare ile tıklanılan pikselin sahip olduğu rengin 10 yaklaşığını
seffaf yaparak png olarak akydeden program
"""

import cv2 as cv
import time

bas_x = bas_y = 0
def fare_tiklama_olayi(event, x, y, flags, param):
    global bas_x, bas_y
    if event == cv.EVENT_LBUTTONDOWN:
        bas_x = x
        bas_y = y
        #print("basıldı :", x, "-", y)

    if event == cv.EVENT_LBUTTONUP:
        #print("bırakıldı :", x, "-", y)
        cv.imwrite("resim/kirpilmis_manzara_fare_ile.jpg", resim[bas_y:y, bas_x:x])
        cv.imshow("Kirpilmis Resim", resim[bas_y:y, bas_x:x])
        #cv.waitKey(0)
        #cv.destroyWindow("Kirpilmis Resim")

resim = cv.imread("manzara.jpg")

cv.imshow("Fare", resim)
cv.setMouseCallback("Fare", fare_tiklama_olayi)
cv.waitKey(0)

""""""
import cv2 as cv

resim = cv.imread("manzara.jpg")
cv.imshow("a", resim)
cv.waitKey(0)
resim[10, 10] = [0, 0, 0]

print(resim[0, 0])

cv.imshow("a", resim)
cv.waitKey(0)

cv.imwrite("resim/manzara_benekli.jpg", resim)

resim[10:50, 10:50] = [0, 0, 0]

print(resim[0, 0])

cv.imshow("a", resim)
cv.waitKey(0)

cv.imwrite("resim/ad_soyad_benekli_2.jpg", resim)


