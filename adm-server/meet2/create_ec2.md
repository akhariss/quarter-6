# Panduan Praktikum: Membuat VM / Instance di AWS EC2 dgn AMI

**Materi:** Administrasi Server - Pertemuan 2
**Semester:** 6

---

## Langkah-Langkah Konfigurasi

### 1. Navigasi Ke Dashboard EC2

* Buka menu **EC2** melalui kolom pencarian di AWS Management Console Dashboard.
* Pilih tombol **Launch Instance** untuk memulai proses pembuatan Virtual Machine baru.

### 2. Penentuan Lokasi (Region)

* **Pastikan Region memilih terdekat:** Klik pada menu dropdown di pojok kanan atas layar dan pilih region yang paling dekat dengan lokasi kamu (disarankan **Singapore / ap-southeast-1**) untuk mendapatkan performa terbaik.

### 3. Identitas & Sistem Operasi

* **Isi Nama Instance:** Masukkan nama dengan format `NIM_Server6A`.
* **Application and OS Images (AMI):** Pada kolom pilihan OS, pilih **Linux Ubuntu**. Gunakan versi LTS (Long Term Support) yang tersedia di *Free Tier*.

### 4. Tipe Instance & Akses (Key Pair)

* **Instance Type:** Pilih **T3.Micro**. Ini adalah tipe instance yang efisien untuk keperluan praktikum.
* **Membuat Key Pair:**
  * Klik **Create new Key Pair**.
  * Masukkan nama Key Pair (misal: `Key_Server_6A`).
  * Pilih format file **.pem**.
  * Klik **Create** dan simpan file tersebut di komputer kamu (file ini digunakan untuk login via SSH).

![1772768739826](image/create_ec2/1772768739826.png)

### 5. Pengaturan Keamanan Jaringan (Network Security)

Konfigurasi firewall pada bagian **Network Settings** dengan mengizinkan (Allow) lalu lintas berikut:

* [X] **Allow SSH Traffic:** Untuk akses terminal remote.
* [X] **Allow HTTPS:** Untuk akses web melalui protokol aman (Port 443).
* [X] **Allow HTTP:** Untuk akses web standar (Port 80).

### 6. Konfigurasi Penyimpanan (Storage)

* **Storage Setting:** Ubah kapasitas penyimpanan menjadi **30Gb**. Ini adalah batas maksimal untuk penggunaan *Free Tier* agar tidak terkena biaya tambahan.

### 7. Finalisasi & Verifikasi

* **Klik Launch Instance:** Periksa ringkasan di panel kanan, lalu tekan tombol Launch.
* **Pastikan Alert Success:** Tunggu hingga muncul notifikasi hijau yang menyatakan instance berhasil dibuat.
* **Pastikan nama sesuai:** Kembali ke daftar instance, klik pada instance tersebut, dan pastikan namanya sudah benar (`NIM_Server6A`).

![1772768692137](image/create_ec2/1772768692137.png)
---

## Catatan Tambahan (Akses SSH)

Setelah status instance menjadi **Running**, kamu bisa mengaksesnya menggunakan file `.pem` yang sudah diunduh tadi melalui terminal:

```bash
ssh -i "nama_file_kamu.pem" ubuntu@<Public_IP_Address>
```


