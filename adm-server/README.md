# Administrasi Server (Adm-Server)

**Praktikum Administrasi Server - Semester 6**

---

## 📚 Deskripsi

Mata kuliah ini membahas administrasi server menggunakan cloud computing AWS (Amazon Web Services). Fokus pada deployment, monitoring, dan maintenance server virtual di cloud.

---

## 📁 Struktur Folder

```
adm-server/
├── meet1/                      # AWS Account Setup
│   └── AWS-Account.md          # Panduan membuat akun AWS
├── meet2/                      # EC2 Instance & Billing
│   ├── create_ec2.md           # Launch EC2 instance
│   ├── Billing-Alert.md        # Setup monitoring biaya
│   └── image/                  # Asset gambar dokumentasi
├── meet3/                      # SSH & Web Server
│   ├── Remote-SSH&web-server.md  # Remote access & Nginx
│   └── image/                  # Asset gambar dokumentasi
├── meet4/                      # SFTP & Web Deployment
│   ├── sftp.md                 # Migrasi data dengan FileZilla
│   └── image/                  # Asset gambar dokumentasi
└── meet5/                      # Database Server
    ├── mariadb.md              # Instalasi & konfigurasi MariaDB
    └── image/                  # Asset gambar dokumentasi
```

---

## 📋 Daftar Praktikum

| Pertemuan | Topik | File |
|-----------|-------|------|
| Meet 1 | AWS Account & Free Tier | `meet1/AWS-Account.md` |
| Meet 2 | EC2 Instance Creation | `meet2/create_ec2.md` |
| Meet 2 | Billing Alert Setup | `meet2/Billing-Alert.md` |
| Meet 3 | Remote SSH & Web Server | `meet3/Remote-SSH&web-server.md` |
| Meet 4 | SFTP & Web Deployment | `meet4/sftp.md` |
| Meet 5 | Database Server (MariaDB) | `meet5/mariadb.md` |

---

## 🚀 Quick Start

### 1. Persiapan AWS Account

Ikuti panduan lengkap di:
```
meet1/AWS-Account.md
```

**Yang perlu disiapkan:**
- Email aktif
- Kartu kredit/debit (Visa/Mastercard)
- Nomor telepon untuk verifikasi

### 2. Membuat EC2 Instance

Setelah akun AWS aktif, lanjut ke:
```
meet2/create_ec2.md
```

**Resource yang dibuat:**
- 1x EC2 Instance (t3.micro, Free Tier)
- 1x Key Pair (.pem file)
- Security Group dengan port 22, 80, 443

### 3. Setup Billing Alert

Lindungi dari tagihan tak terduga:
```
meet2/Billing-Alert.md
```

**Recommended threshold:** $1 - $5 untuk early warning

### 4. Remote SSH & Web Server

Akses server dan instal Nginx:
```
meet3/Remote-SSH&web-server.md
```

**Tools yang dibutuhkan:**
- PuTTY (Windows) atau terminal SSH (Mac/Linux)
- File .ppk (konversi dari .pem)

### 5. SFTP & Web Deployment

Transfer file dan deploy website:
```
meet4/sftp.md
```

**Tools yang dibutuhkan:**
- FileZilla Client
- SSH access untuk ubah hak akses folder

### 6. Database Server (MariaDB)

Instalasi dan konfigurasi database server:
```
meet5/mariadb.md
```

**Yang dilakukan:**
- Instalasi MariaDB
- Hardening database server
- Membuat database dan user
- Mengatur hak akses (privileges)

---

## 🔑 Konsep Penting

### EC2 (Elastic Compute Cloud)
Virtual server di cloud AWS. Bisa pilih OS, spesifikasi, dan bayar sesuai pemakaian.

### Security Group
Firewall virtual yang mengatur lalu lintas masuk/keluar instance EC2.

### Key Pair
Kunci SSH untuk autentikasi (public key di server, private key di komputer kamu).

### CloudWatch
Layanan monitoring AWS untuk metrics dan alarm.

### SNS (Simple Notification Service)
Layanan untuk mengirim notifikasi (email/SMS) saat alarm trigger.

### SFTP (SSH File Transfer Protocol)
Protokol transfer file yang aman dengan enkripsi SSH.

### File Permissions
Hak akses file/folder di Linux (owner, group, others).

---

## ⚠️ Tips Menghindari Tagihan

1. **Stop instance** setelah selesai praktikum
2. **Set billing alert** di threshold $1
3. **Monitor Free Tier usage** di Billing Dashboard
4. **Terminate resource** yang tidak dipakai
5. **Gunakan region** yang sesuai (Singapore untuk latency rendah)

---

## 🛠️ Tools & Services AWS

| Service | Fungsi |
|---------|--------|
| EC2 | Virtual server/cloud computing |
| CloudWatch | Monitoring & alarm |
| SNS | Notifikasi email/SMS |
| VPC | Virtual network |
| Security Group | Firewall instance |
| Key Pair | SSH authentication |

## 🛠️ Tools Client

| Tool | Fungsi |
|------|--------|
| PuTTY | SSH client untuk Windows |
| FileZilla | SFTP/FTP client untuk transfer file |
| PowerShell | Terminal untuk SSH di Windows |
| nano/vim | Text editor di Linux terminal |
| MariaDB | Database server open-source |

---

## 📝 Checklist Praktikum

- [ ] AWS Account aktif dengan Basic Support (Free)
- [ ] MFA diaktifkan untuk keamanan
- [ ] EC2 Instance running (t3.micro)
- [ ] Key Pair tersimpan aman
- [ ] Billing Alert aktif dengan threshold $1
- [ ] Bisa remote SSH ke instance
- [ ] Nginx terinstall dan accessible via browser
- [ ] FileZilla terinstall dan bisa koneksi SFTP
- [ ] Paham cara ubah hak akses folder di Linux
- [ ] Berhasil deploy file website ke `/var/www/html`
- [ ] MariaDB terinstall dan status active (running)
- [ ] Database sudah di-hardening
- [ ] Berhasil membuat database dan user dengan hak akses yang benar

---

## 🔗 Referensi

- **AWS Free Tier:** https://aws.amazon.com/free/
- **EC2 Documentation:** https://docs.aws.amazon.com/ec2/
- **CloudWatch:** https://docs.aws.amazon.com/cloudwatch/
- **AWS Pricing Calculator:** https://calculator.aws/
- **FileZilla:** https://filezilla-project.org/
- **Linux File Permissions:** https://www.linux.com/training-tutorials/understanding-linux-file-permissions/
- **MariaDB Documentation:** https://mariadb.com/kb/en/documentation/

---

## 👨‍💻 Author

**Abdul Kharis**  
NIM: 2388010004  
Semester 6 - Informatics Engineering

---

*Last Updated: April 2026*
