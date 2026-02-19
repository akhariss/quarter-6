import cv2
import numpy as np

# Langkah 2 – Membaca Citra
img = cv2.imread('meet1/cctv.jpg')

print("Tipe data img:", type(img))
print("Shape img:", img.shape)

# Langkah 3 – Menampilkan Citra
cv2.imshow('CCTV Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Langkah 4 – Akses Nilai Piksel
pixel = img[100, 150]
print("Nilai piksel (BGR):", pixel)

blue = img[100, 150, 0]
print("Channel Biru:", blue)
