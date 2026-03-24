# Praktikum 1: Membuat Akun AWS & Klaim Free Tier

**Administrasi Server - Pertemuan 1**

---

## 🎯 Tujuan Praktikum

Setelah mengikuti praktikum ini, kamu akan:
- Memahami cara mendaftar akun AWS dengan benar
- Mengerti program Free Tier dan batasannya
- Mampu menghindari tagihan tak terduga saat belajar AWS

---

## 📋 Persiapan

Sebelum mendaftar, siapkan hal-hal berikut:

| Item | Keterangan |
|------|-----------|
| Email aktif | Belum pernah digunakan untuk daftar AWS |
| Kartu Kredit/Debit | Visa/Mastercard/Amex dengan saldo minimal ~Rp 20.000 |
| Nomor telepon aktif | Untuk verifikasi SMS/call |
| Alamat lengkap | Sesuai data penagihan kartu |

> 💡 **Catatan:** AWS akan melakukan temporary hold ~$1 USD untuk verifikasi kartu. Dana akan dikembalikan dalam beberapa hari.

---

## Langkah Kerja

### 1. Buka Halaman Pendaftaran

1. Buka browser, akses:
   ```
   https://portal.aws.amazon.com/billing/signup
   ```
2. Klik **Create a new AWS account**

---

### 2. Verifikasi Email

1. Masukkan **Email Address** dan **AWS Account Name**
2. Klik **Verify email address**
3. Masukkan kode verifikasi dari email
4. Buat **Root User Password** yang kuat:
   - Minimal 8 karakter
   - Kombinasi huruf besar, kecil, angka, simbol

---

### 3. Informasi Kontak

1. Pilih **Account Type**:
   - **Personal** — untuk belajar/proyek pribadi
   - **Business** — untuk keperluan perusahaan

2. Isi data berikut:
   - Nama Lengkap
   - Nomor Telepon
   - Alamat sesuai identitas

3. Centang persetujuan **AWS Customer Agreement**

---

### 4. Informasi Pembayaran

1. Masukkan detail kartu kredit/debit kamu
2. Pastikan kartu mendukung transaksi internasional

---

### 5. Verifikasi Identitas

1. Masukkan nomor ponsel
2. Pilih metode verifikasi: **SMS** atau **Voice Call**
3. Masukkan kode PIN yang diterima

---

### 6. Pilih Support Plan (Klaim Free Tier)

> ⚠️ **PENTING:** Pilih yang benar agar tidak kena biaya bulanan!

1. Pilih **Basic Support – Free**
2. **JANGAN** pilih Developer atau Business Support (mulai dari $29/bulan)

<img width="1722" height="817" alt="image" src="https://github.com/user-attachments/assets/415adf5b-2a15-4d45-82c1-5ff5f92a14c7" />

---

### 7. Aktivasi Akun

1. Klik **Complete Sign Up**
2. Tunggu proses aktivasi (beberapa menit - 24 jam)
3. Cek email untuk konfirmasi akun aktif

---

## 💡 Memahami Free Tier

AWS Free Tier terdiri dari 3 jenis:

| Jenis | Keterangan | Contoh |
|-------|-----------|--------|
| **Always Free** | Gratis selamanya (selama tidak melebihi batas) | Lambda 1 juta request/bulan |
| **12 Months Free** | Gratis selama 1 tahun sejak pendaftaran | EC2 750 jam/bulan |
| **Trials** | Uji coba jangka pendek (1-2 bulan) | SageMaker 2 bulan |

### Layanan Utama Free Tier

| Layanan | Kuota Free Tier |
|---------|-----------------|
| EC2 | 750 jam/bulan (t2.micro atau t3.micro) |
| S3 | 5 GB Storage |
| RDS | 750 jam/bulan (MySQL/PostgreSQL) |
| Lambda | 1 juta request/bulan |
| DynamoDB | 25 GB Storage |

---

## ⚠️ Tips Menghindari Tagihan Tak Terduga

1. **Set Up Billing Alarms**
   - Gunakan CloudWatch atau AWS Budgets
   - Set alert saat biaya mendekati $1

2. **Hapus Resource Tidak Dipakai**
   - Terminate EC2 instance setelah selesai praktikum
   - Hapus S3 bucket yang tidak diperlukan

3. **Cek Free Tier Dashboard**
   - Menu: **Billing & Cost Management** → **Free Tier**
   - Pantau penggunaan secara berkala

4. **Gunakan Region yang Tepat**
   - Beberapa region punya harga berbeda
   - Free Tier berlaku global

---

## 📝 Checklist Hasil Praktikum

- [ ] Akun AWS berhasil dibuat
- [ ] Support Plan = Basic (Free)
- [ ] Email konfirmasi diterima
- [ ] Paham batas Free Tier untuk EC2, S3, RDS
- [ ] Tahu cara monitoring biaya di Billing Dashboard

---

## 🏁 Langkah Selanjutnya

Setelah akun aktif:

1. **Aktifkan MFA (Multi-Factor Authentication)** untuk keamanan akun Root
2. Lanjut ke praktikum berikutnya: **Membuat EC2 Instance**

---

## ❓ FAQ

**Q: Apakah kartu debit bisa untuk daftar AWS?**  
A: Ya, asalkan ada logo Visa/Mastercard dan mendukung transaksi internasional.

**Q: Berapa lama proses aktivasi akun?**  
A: Biasanya beberapa menit, tapi bisa sampai 24 jam dalam beberapa kasus.

**Q: Apa yang terjadi jika melebihi kuota Free Tier?**  
A: Kamu akan dikenakan biaya sesuai harga on-demand. Makanya penting set billing alert!

**Q: Apakah Free Tier otomatis aktif?**  
A: Ya, begitu akun dibuat, Free Tier langsung aktif selama 12 bulan.

---

*Dokumentasi praktikum Administrasi Server Semester 6*
