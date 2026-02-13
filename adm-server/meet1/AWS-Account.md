# Cara Membuat Akun AWS dan Mengaktifkan Free Trial

## Pendahuluan

Amazon Web Services (AWS) adalah platform cloud computing yang menawarkan berbagai layanan mulai dari komputasi, penyimpanan, basis data, hingga machine learning. AWS menyediakan program **AWS Free Tier** yang memungkinkan pengguna baru untuk mencoba layanan AWS secara gratis selama 12 bulan pertama. Panduan ini akan memandu Anda langkah demi langkah dalam membuat akun AWS dan mengaktifkan free trial dengan benar.

## Daftar Isi

1. [Prasyarat](#prasyarat)
2. [Langkah-langkah Membuat Akun AWS](#langkah-langkah-membuat-akun-aws)
3. [Memahami AWS Free Tier](#memahami-aws-free-tier)
4. [Verifikasi Akun](#verifikasi-akun)
5. [Tips Menggunakan AWS Free Tier](#tips-menggunakan-aws-free-tier)
6. [Kesimpulan](#kesimpulan)

---

## Prasyarat

Sebelum memulai, pastikan Anda memiliki下列 persyaratan:

- **Alamat Email Valid** - Anda需要一个有效的电子邮件地址来创建AWS账户
- **Nomor Telepon** - AWS需要有效的电话号码进行验证
- **Kartu Kredit/Debit** - AWS需要对信用卡或借记卡进行验证，即使在免费套餐期间也是如此
- **Browser Terbaru** - 使用最新版本的浏览器，如Chrome、Firefox或Edge

---

## Langkah-langkah Membuat Akun AWS

### Langkah 1: Mengakses Halaman Pendaftaran AWS

1. Buka browser dan akses halaman resmi AWS: [https://aws.amazon.com](https://aws.amazon.com)
2. Klik tombol **"Create an AWS Account"** yang biasanya berada di pojok kanan atas halaman
3. Anda akan dialihkan ke halaman pendaftaran AWS

### Langkah 2:填写注册信息

在注册页面上，按照以下步骤操作：

1. **电子邮件地址**
   - 输入您想要用于AWS账户的电子邮件地址
   - 这将是您的主要登录凭据

2. **Nama Akun AWS**
   - 输入您想要的AWS账户名称
   - 示例：`MyCloudAccount` 或 `CompanyName`

3. **Kata Sandi (Password)**
   - 创建强密码：
     - 至少8个字符
     - 至少一个大写字母
     - 至少一个小写字母
     - 至少一个数字
     - 至少一个特殊字符

4. Klik tombol **"Verify email address"** untuk melanjutkan

### Langkah 3: Informasi Pribadi

1. **Pilih Jenis Akun**
   - Pilih **"Personal"** jika Anda membuat akun untuk penggunaan pribadi
   - Pilih **"Professional"** jika Anda代表公司或组织

2. **Isi Data Diri**
   - Nama lengkap (Nama depan dan nama belakang)
   - Nomor telepon
   - Negara/Wilayah
   - Alamat

3. Klik **"Continue"** untuk melanjutkan

### Langkah 4: Informasi Pembayaran

1. **Masukkan Informasi Kartu**
   - Masukkan nomor kartu kredit/debit
   - Masukkan tanggal kedaluwarsa kartu
   - Masukkan CVV (kode keamanan di belakang kartu)

2. **Catatan Penting:**
   - AWS akan melakukan **pra-otorisasi** sejumlah kecil biaya (biasanya sekitar $1-2) untuk memverifikasi kartu validity
   - Dana ini akan dikembalikan dalam beberapa hari kerja
   - **Tanpa kartu valid, Anda tidak dapat mengaktifkan akun AWS**

3. Klik **"Verify and Continue"** untuk melanjutkan

### Langkah 5: Verifikasi Identitas

1. **Verifikasi melalui SMS atau Telepon**
   - AWS akan mengirim kode verifikasi ke nomor telepon yang Anda masukkan
   - Masukkan kode yang diterima
   - Klik **"Continue"**

2. Jika Anda memilih verifikasi melalui telepon, tunggu panggilan masuk dan masukkan kode yang diberikan

### Langkah 6: Dukungan AWS

1. **Pilih Rencana Dukungan**
   - **Basic Support** - 免费，适合个人使用
   - **Developer Support** - 起价29美元/月
   - **Business Support** - 起价100美元/月
   - **Enterprise Support** - 起价15,000美元/月

2. Untuk memulai, pilih **"Basic Support"** (gratis)

3. Klik **"Complete Sign Up"**

---

## Memahami AWS Free Tier

AWS Free Tier分为三种类型：

### 1. 永久免费服务（Always Free）
这些服务在12个月后仍然免费：
- **AWS Lambda** - 每月1,000,000次请求
- **Amazon DynamoDB** - 每月25 GB存储
- **Amazon CloudFront** - 每月1 TB数据传输
- **AWS IoT Core** - 每月250,000条消息

### 2. 12个月免费套餐（Free for 12 Months）
以下服务在注册后12个月内免费：
- **Amazon EC2** - 每月750小时
- **Amazon S3** - 每月5 GB标准存储
- **Amazon RDS** - 每月750小时
- **Amazon EBS** - 每月30 GB
- **Amazon CloudWatch** - 每月10个指标

### 3. 短期优惠（Short-Term Trials）
一些服务提供短期试用：
- **Amazon SageMaker** - 2个月免费
- **Amazon Lightsail** - 3个月免费（价值约$250）

---

## Verifikasi Akun

### 检查账户状态

1. 登录AWS管理控制台：https://console.aws.amazon.com
2. 查看账户状态指示器
3. 确保显示"Active"或"Verified"

### 确认免费套餐限额

1. 转到**AWS Billing Console**
2. 点击**"Cost Explorer"**查看使用情况
3. 监控您的免费套餐使用情况

---

## Tips Menggunakan AWS Free Tier

### 1. 监控使用情况
- 定期检查**AWS Budgets**设置预算警报
- 使用**CloudWatch**监控资源使用
- 查看**AWS Cost Explorer**分析支出

### 2. 最佳实践
- **立即设置预算**：在AWS Billing控制台中创建预算
- **启用警报**：当使用量达到80%时接收通知
- **使用标记**：标记资源以便更好地跟踪成本

### 3. 应避免的错误
- **不要超额使用**：超出免费套餐的服务将收费
- **不要忘记删除未使用的资源**：运行实例即使不使用也会产生成本
- **不要共享账户**：每个账户都有独立的免费套餐限额

### 4. 推荐的服务组合
对于初学者，建议从以下服务开始：
- **EC2 + S3** - 了解基本云计算
- **RDS** - 学习数据库管理
- **Lambda** - 体验无服务器计算

---

## Kesimpulan

Membuat akun AWS dan mengaktifkan free trial adalah langkah pertama yang excellent untuk memulai perjalanan cloud computing Anda. Dengan mengikuti panduan ini, Anda dapat:

✅ Membuat akun AWS dengan benar
✅ Memahami berbagai类型的免费套餐
✅ Menghindari biaya tak terduga
✅ Memaksimalkan penggunaan layanan gratis

**Catatan Penting:**
- Selalu pantau penggunaan layanan Anda
- Hapus sumber daya yang tidak digunakan
- Manfaatkan dokumentasi AWS untuk pembelajaran lebih lanjut

Untuk informasi lebih lanjut, silakan visite:
- Dokumentasi AWS: https://docs.aws.amazon.com
- AWS Free Tier: https://aws.amazon.com/free

---

**Last Updated:** 2024
**Version:** 1.0
