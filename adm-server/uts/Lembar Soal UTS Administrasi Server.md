# **UJIAN TENGAH SEMESTER (UTS)**

**Mata Kuliah:** Administrasi Server (Cloud Computing II)

**Tahun Akademik:** 2025/2026

**Dosen Pengampu:** Mohamad Firdaus, M.Kom

**Sifat Ujian:** Praktik Langsung (*Live Deployment Test*) \- *Open Book* 

**Waktu Pengerjaan:** 150 Menit (Dilanjutkan dengan *Live Checking*)

## **A. DESKRIPSI TUGAS (THE MISSION)**

Anda sedang melamar posisi *Cloud Engineer* di sebuah perusahaan teknologi multinasional. Sebagai ujian teknis sekaligus pembuktian *skill* Anda, Tim HRD dan Tim Infrastruktur memberikan tantangan:

**"Deploy Curriculum Vitae (CV) atau Portofolio Pribadi Anda dalam bentuk Website Statis ke server AWS dari nol, dalam waktu kurang dari 1,5 jam."**

Anda diwajibkan membangun infrastruktur servernya, mengamankannya sesuai standar industri, dan memastikan Web CV Anda dapat diakses secara global oleh tim penilai.

## **B. SPESIFIKASI INFRASTRUKTUR YANG DIMINTA**

1. **Region:** Wajib menggunakan region **Singapore (ap-southeast-1)**.  
2. **Compute:** \* Amazon EC2 Instance dengan OS **Ubuntu 22.04 LTS** atau **24.04 LTS**.  
   * Tipe Instance wajib **t2.micro** atau **t3.micro** (*Free Tier Eligible*).  
3. **Storage:** 8 GB General Purpose SSD (gp2/gp3).  
4. **Security & Access:**  
   * Wajib menggunakan **Key Pair** (Tidak boleh menggunakan password/EIC).  
   * **Security Group:** Hanya buka Port 80 (HTTP) dari *Anywhere* (0.0.0.0/0) dan Port 22 (SSH) **hanya dari IP Publik Anda sendiri** (*My IP*).  
5. **Web Server:** Menggunakan **Nginx** (Bukan Apache).  
6. **Monitoring:** Wajib mengaktifkan *Detailed CloudWatch Monitoring* dan membuat 1 buah Alarm jika penggunaan CPU menyentuh \>80%.

## **C. INSTRUKSI PENGERJAAN (STEP-BY-STEP)**

### **Tahap 1: Provisioning & Security (30 Poin)**

1. Buat instance EC2 sesuai spesifikasi di atas.  
2. Buat Elastic IP (EIP) dan *Attach* (hubungkan) EIP tersebut ke instance EC2 Anda secara permanen.  
3. Konfigurasi *Security Group* dengan ketat sesuai aturan di atas.

### **Tahap 2: Konfigurasi Web Server (30 Poin)**

1. Lakukan *remote login* (SSH) ke dalam server Anda menggunakan PuTTY atau Terminal.  
2. Lakukan instalasi web server Nginx.  
3. Pastikan *service* Nginx berstatus *running* dan *enabled*.

### **Tahap 3: Deployment Aplikasi Web CV (40 Poin)**

1. Siapkan *source code* **Web CV / Portofolio Pribadi** Anda (berbasis HTML/CSS/JS). Anda **diizinkan** menggunakan template gratis dari internet, namun wajib dimodifikasi dengan **Data Diri Asli Anda** (Foto, Riwayat Pendidikan, Skill, dll).  
2. Gunakan aplikasi SFTP (seperti FileZilla atau WinSCP) untuk memindahkan *source code* Web CV tersebut dari laptop Anda ke dalam server.  
3. Pindahkan *source code* tersebut ke *Document Root* Nginx/Apache (biasanya di /var/www/html).  
4. **PENTING:** Atur *Ownership* dan *Permissions* (chown & chmod) pada folder website tersebut secara benar agar Nginx (www-data) bisa membacanya tanpa terkena *Error 403 Forbidden*.  
5. **Validasi Ujian:** Pastikan di bagian paling bawah website CV Anda (footer) terdapat tulisan tebal: **"Dideploy oleh: \[Nama Lengkap Anda\] \- \[NIM Anda\]"**.

## **D. EVALUASI DAN PENGUMPULAN (LIVE CHECKING)**

Penilaian utama mata kuliah ini akan dilakukan secara **SERENTAK dan LIVE** di kelas pada Pertemuan 8 ini.

**1\. Live IP Check (Penilaian Utama):**

Saat waktu pengerjaan 150 menit habis, seluruh mahasiswa diwajibkan memasukkan alamat **Elastic IP** servernya ke dalam form/spreadsheet yang disediakan oleh Dosen. Dosen akan membuka IP tersebut satu per satu di layar proyektor kelas untuk memvalidasi keberhasilan deployment Web CV Anda.

**2\. Bukti Log & Keamanan (Wajib Dikumpulkan ke LMS):**

Sebagai bukti administratif dan verifikasi keamanan, jadikan 4 screenshot berikut ke dalam **1 file PDF** dan kumpulkan ke sistem E-Learning:

* Screenshot halaman utama AWS EC2 Console (menunjukkan Instance ID, status *Running*, dan Elastic IP).  
* Screenshot halaman Security Group Inbound Rules (menunjukkan Port 22 hanya diakses oleh *My IP*).  
* Screenshot halaman CloudWatch Alarms (menunjukkan alarm CPU berstatus *OK* atau hijau).  
* Screenshot Terminal/PuTTY saat Anda berhasil mengeksekusi perintah sudo systemctl status nginx.

## **E. RINCIAN RUBRIK PENILAIAN (SKALA 100 POIN)**

Penilaian dibagi menjadi dua tahap: **Pengecekan Live (40 Poin)** dan **Verifikasi Dokumen Keamanan (60 Poin)**.

### **1\. Pengecekan Live (Total 40 Poin)**

| Indikator Penilaian | Kriteria Detail & Poin | Poin Maksimal |
| :---- | :---- | :---- |
| **Aksesibilitas & Konten Web CV** | **\[30 Poin\]** Web CV dapat diakses dengan lancar, tidak ada *Error 403*, dan berisi foto serta data diri asli mahasiswa yang valid. **\[15 Poin\]** Web CV tampil, tapi belum diedit (masih menggunakan foto/data *template* fiktif bawaan internet). **\[10 Poin\]** Web dapat diakses tapi muncul pesan *Error 403 Forbidden* (gagal *Permission*) atau halaman *Welcome to Nginx*. **\[0 Poin\]** Web *Time Out* / *Site Can't Be Reached* (Instance mati, salah EIP, atau SG tertutup). | 30 |
| **Autentisitas Karya** | **\[10 Poin\]** Nama Lengkap dan NIM tercantum dengan jelas di bagian *footer* website. **\[0 Poin\]** Tidak ada pencantuman Nama/NIM. | 10 |

### **2\. Verifikasi Keamanan & Infrastruktur (Total 60 Poin)**

| Indikator Penilaian | Kriteria Detail & Poin | Poin Maksimal |
| :---- | :---- | :---- |
| **Kepatuhan Keamanan (Security Group)** | **\[25 Poin\]** Port 22 (SSH) dikunci secara ketat HANYA ke IP Spesifik (*My IP*), dan Port 80 dibuka ke *Anywhere* (0.0.0.0/0). **\[10 Poin\]** Port 22 (SSH) dibiarkan terbuka ke *Anywhere* (0.0.0.0/0) \- *Pelanggaran Keamanan Berat\!* **\[0 Poin\]** Tidak melampirkan screenshot Security Group. | 25 |
| **Ketahanan Infrastruktur (EIP & Alarm)** | **\[20 Poin\]** Menggunakan Elastic IP (permanen) dan melampirkan Alarm CloudWatch berstatus OK. **\[10 Poin\]** Hanya salah satu kondisi yang terpenuhi (Hanya EIP atau Hanya Alarm CloudWatch). **\[0 Poin\]** Tidak menggunakan Elastic IP dan tidak ada Alarm. | 20 |
| **Administrasi Laporan** | **\[15 Poin\]** Format PDF rapi, menampilkan 4 screenshot wajib (termasuk bukti log status service Nginx *active (running)*). **\[0 Poin\]** Screenshot berantakan, terpotong, tidak relevan, atau tidak ada PDF. | 15 |

### **⚠️ Pelanggaran & Penalti Khusus**

* **Plagiasi/Joki (-50 Poin):** Menggunakan Elastic IP yang sama persis dengan mahasiswa lain yang sudah diuji, atau isi CV terbukti *copy-paste* 100% milik teman.  
* **Pemborosan Biaya AWS (-10 Poin):** Tidak mematikan (*Stop*) Instance dan melepas (*Release*) Elastic IP setelah instruksi ujian selesai diberikan, yang dapat menyebabkan pemborosan saldo AWS Educate/Academy kampus.

**Peringatan FinOps:** Tunggu instruksi Dosen sebelum mematikan server. Setelah nilai Anda dicatat dan diverifikasi di kelas secara *live*, **SEGERA MATIKAN (STOP)** instance Anda dan **LEPAS (RELEASE)** Elastic IP Anda\!