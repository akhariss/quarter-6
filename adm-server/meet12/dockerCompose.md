# Deploy Multiple Container menggunakan Docker Compose

1. Start Instance EC2 di AWS
2. Patching OS
3. Uninstall semua Services manual sebelumnya
4. Repositori baru untuk web dinamis di docker hub
   ![1779372119411](image/dockerCompose/1779372119411.png)
5. Buka Projek Company himafor_nim
6. Bagi 2 Folder untuk projek Web App Statis dan Dinamis
7. Move file index dan Dcoker milik web statis ke Folder web-statis
8. Copy Folder Projek Next.JS (pertemuan9)ke folder web-dinamis
9. Lakukan Testing di Local Project Next.JS

   - Install Dependencies: `npm install`
   - Create user di DBMS : `sudo mysql -u root -p`
     - `CREATE USER '2388010004'@'localhost' IDENTIFIED BY 'P1kSD_W4uIQK)Y[x';`
     - `GRANT ALL PRIVILEGES ON *.* TO 'userwebdinamis_nim'@'localhost';`
     - `FLUSH PRIVILEGES;`
     - `exit;`
       ![1779372151409](image/dockerCompose/1779372151409.png)
   - Edit File .env di folder web-dinamis
   - `npm run build`
   - `npm start`
   - Pastikan web dapat diakses di http://localhost:3000 admin tanpa error
     ![1779372242485](image/dockerCompose/1779372242485.png)
10. Buat file Dockerfile
11. Buat file docker-compose.yml
12. Buat Workflows File -> deploy-dinamis.yml di folder .github/workflows/ dari Projek web-dinamis
13. Edit File -> deploy.yml di folder .github/workflows/ untuk
14. Update Host AWS di Github
15. Commit Changes ke GitHub dari lokal
16. Push Changes ke GitHub
17. Cek di Github, apakah actions jalan dan berhasil
    ![1779372751410](image/dockerCompose/1779372751410.png)Cek di AWS, apakah container berjalan dengan baik
18. ![1779372656146](image/dockerCompose/1779372656146.png)
19. Akses web melalui Browser login admin edit Layanan
    ![1779372477447](image/dockerCompose/1779372477447.png)
