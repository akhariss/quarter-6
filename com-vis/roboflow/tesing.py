from inference import InferencePipeline
from inference.core.interfaces.stream.sinks import render_boxes

# 1. Ganti pakai API Key lo
api_key = "gv9rQ7ZXLgnPVOfeEwvM"

# 2. Buat pipeline
pipeline = InferencePipeline.init(
    # Ganti model_id dengan ID project lo (cek di dashboard Roboflow)
    # Formatnya: "nama-project/versi"
    model_id="usb-cable-head-classifier/1", 
    
    # Ganti jadi 0 kalau mau pakai webcam laptop asli
    video_reference=0, 
    
    # Fungsi bawaan buat nampilin kotak deteksi di layar
    on_prediction=render_boxes, 
    
    api_key=api_key,
)

# Mulai deteksi
pipeline.start()
pipeline.join()