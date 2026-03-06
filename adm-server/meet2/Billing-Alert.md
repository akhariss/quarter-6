# Panduan Lengkap: Membuat Billing Alert di AWS

**Tujuan:** Menghindari pembengkakan biaya (over-budget) dengan mengatur notifikasi otomatis jika penggunaan saldo melebihi ambang batas yang ditentukan.

---

## 1. Konfigurasi Billing Preferences

Sebelum membuat alarm, Anda harus mengaktifkan izin agar AWS dapat memantau dan mengirimkan data tagihan ke layanan monitoring.

1. **Masuk ke Billing Dashboard:**
   - Buka **AWS Management Console**.
   - Cari dan pilih menu **Billing and Cost Management**.
2. **Atur Alert Preference:**
   - Di panel navigasi kiri, klik **Alert Preference** (atau *Billing Preferences*).
   - Klik tombol **Edit**.
3. **Aktivasi Notifikasi:**
   - **Email:** Masukkan alamat email aktif Anda.
   - **Ceklis:** Pastikan opsi **Receive Billing Alerts** dicentang.
   - (Opsional) Centang **Receive Free Tier Usage Alerts** untuk mengetahui jika kuota gratis hampir habis.
4. **Simpan:** Klik **Update**.

---

## 2. Membuat CloudWatch Billing Alarm

CloudWatch adalah layanan yang akan memicu peringatan berdasarkan nominal uang yang Anda tentukan.

1. **Pindah Region:**
   - **PENTING:** Pastikan Region di pojok kanan atas diatur ke **US East (N. Virginia)** atau `us-east-1`. Metrik penagihan hanya tersedia di region ini.
2. **Buka CloudWatch:**
   - Cari dan pilih layanan **CloudWatch** dari menu *All Services*.
3. **Konfigurasi Metric:**
   - Klik menu **Create Alarm**.
   - Klik tombol **Select Metric**.
   - Pilih kategori **Billing** > **Total Estimated Charge**.
   - Ceklis mata uang **USD** dan klik **Select Metric**.
4. **Menentukan Ambang Batas (Conditions):**
   - **Type:** Pilih **Static**.
   - **Whenever... is:** Pilih **Greater than (>)**.
   - **Threshold:** Masukkan angka nominal (Contoh: `1` untuk alert jika biaya mencapai $1).
5. **Konfigurasi Notifikasi (SNS):**
   - Pilih **Create new topic**.
   - Beri nama topik: `NIM_BillingAlert`.
   - Klik **Create Topic**.
     ![1772766489677](image/Billing-Allert/1772766489677.png)
6. **Finalisasi:**
   - Klik **Next**, masukkan Alarm Name: `NIM_BillingAlert`.
   - Klik **Create Alarm**.

---

## 3. Verifikasi Keamanan (Langkah Wajib)

Alarm tidak akan aktif mengirim email jika langkah ini dilewati:

1. Buka **Inbox** atau **Spam** pada email yang didaftarkan.

   ![1772768788446](image/Billing-Alert/1772768788446.png)
2. Cari email dari AWS (Simple Notification Service).
3. Klik tautan **Confirm Subscription**.
4. Status alarm di CloudWatch akan berubah dari *Pending* menjadi *OK* atau *In Alarm*.

---

*Dokumentasi ini dibuat untuk keperluan monitoring tugas kuliah Informatika Semester 6.*
