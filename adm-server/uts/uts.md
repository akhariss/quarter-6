# hecklist Lengkap

### 📦 Yang Harus Disiapkan SEBELUM UTS

- [X] **File website CV/Portfolio** (HTML/CSS/JS static)
  - [X] Ada **foto profil asli** kamu
  - [X] Ada **data diri asli** (nama, pendidikan, skill, dll)
  - [X] Ada **footer** dengan teks: **"Dideploy oleh: [Nama Lengkap] - [NIM]"**
- [X] **AWS Account** sudah aktif
- [X] **PuTTY** sudah terinstall (Windows)
- [X] **FileZilla** sudah terinstall
- [X] **Siapkan text editor** (VS Code, Notepad++, dll) untuk edit footer

### 🎯 Spesifikasi UTS yang Wajib Dipenuhi

#### Infrastructure (EC2)

- [X] Region: **Singapore (ap-southeast-1)**
- [X] AMI: **Ubuntu 22.04 LTS** atau **24.04 LTS**
- [X] Instance Type: **t2.micro** atau **t3.micro** (Free Tier)
- [X] Storage: **8 GB** gp2/gp3
- [X] Login: **Key Pair** (bukan password)
- [X] **Elastic IP** allocated & attached
- [X] Security Group:

  - [X] Port **80** (HTTP) → **0.0.0.0/0** (Anywhere)
  - [X] Port **22** (SSH) → **My IP** saja!

#### Web Server

- [X] **Nginx** installed
- [X] Status: **active (running)** dan **enabled**

<pre class="vditor-reset" placeholder="" contenteditable="true" spellcheck="false"><p data-block="0"><img src="https://file+.vscode-resource.vscode-cdn.net/c%3A/quarter-6/adm-server/uts/image/uts/1776392127432.png" alt="1776392127432"/></p></pre>

#### Monitoring

- [X] **Detailed CloudWatch Monitoring** enabled (1-minute interval)
- [X] **CPU Alarm >80%** created & status **OK** (hijau)

  ![1776392013903](https://file+.vscode-resource.vscode-cdn.net/c%3A/quarter-6/adm-server/uts/image/uts/1776392013903.png)

#### Deployment

- [X] Website uploaded via **SFTP** ke `/var/www/html`

  ![1775929243196](../image/TUTORIAL-UTS-LENGKAP/1775929243196.png)
- [X] Ownership: **www-data:www-data** (bukan ubuntu:ubuntu!)

  Permissions: **755** untuk folder, **644** untuk file

  ![1775928584439](../image/TUTORIAL-UTS-LENGKAP/1775928584439.png)
- [X] Footer: **"Dideploy oleh: [Nama Lengkap] - [NIM]"**
- [X] Website accessible via `http://<ELASTIC_IP>` tanpa error 403
  ![1775928912569](../image/TUTORIAL-UTS-LENGKAP/1775928912569.png)

#### 4 Screenshot Wajib (PDF)

- [X] EC2 Console (Instance running + Elastic IP)

  ![1775922028052](../image/TUTORIAL-UTS-LENGKAP/1775922028052.png)
- [X] Security Group Inbound Rules (Port 22 → My IP)![1775928706827](../image/TUTORIAL-UTS-LENGKAP/1775928706827.png)
- [X] CloudWatch Alarms (status OK/hijau)

  ![1775922134383](../image/TUTORIAL-UTS-LENGKAP/1775922134383.png)
- [X] Terminal: `sudo systemctl status nginx` (active running)

  ![1775922165297](../image/TUTORIAL-UTS-LENGKAP/1775922165297.png)
