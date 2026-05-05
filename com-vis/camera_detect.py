from ultralytics import YOLO
import cv2

# Memuat model YOLO yang sudah dilatih
model = YOLO("my_model.pt")

# Membuka kamera bawaan laptop/komputer (indeks 0)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Melakukan deteksi objek pada frame kamera
    results = model(frame, imgsz=640)

    # PERBAIKAN DI SINI: Tambahkan [0] sebelum .plot()
    frame = results[0].plot()

    # Menampilkan window video
    cv2.imshow("Detection", frame)

    # Tekan 'q' pada keyboard untuk keluar dari program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()