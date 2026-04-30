# Facebook Auto Post - Playwright Edition 🚀

Developed with ❤️ by **ZII DEV** (Roji Rohmatillah)

[![YouTube](https://img.shields.io/badge/YouTube-ZII%20DEV-red?style=for-the-badge&logo=youtube)](https://www.youtube.com/@ziideveloper)

## 📋 Deskripsi
Bot automasi untuk posting ke grup Facebook menggunakan Python dan Playwright. Dibuat khusus untuk membantu promosi.

## ⚖️ License
Distributed under the MIT License. See `LICENSE` for more information.

# Facebook Auto Post - Playwright Edition 🚀

Developed with ❤️ by **ZII DEV** (Roji Rohmatillah)

[![YouTube](https://img.shields.io/badge/YouTube-ZII%20DEV-red?style=for-the-badge&logo=youtube)](https://www.youtube.com/@ziideveloper)

## 📋 Deskripsi
Bot automasi untuk posting ke grup Facebook menggunakan Python dan Playwright. Dibuat khusus untuk membantu promosi karya atau project (seperti game development devlogs).

---

## 🛠️ Persiapan & Instalasi

### 1. Persyaratan Sistem
*   Python 3.8 atau versi lebih baru.
*   Google Chrome terinstal (untuk mode `persistent_context`).

### 2. Instalasi Library
Buka terminal atau CMD, lalu jalankan perintah berikut:
```bash
# Install library Playwright
pip install playwright

# Install browser driver
playwright install chromium

⚙️ Konfigurasi
1. Mengatur Cookies (fb_cookies.json)
Agar bot tidak perlu login manual terus-menerus dan menghindari checkpoint:

Buka Chrome dan install ekstensi Cookie-Editor.

Login ke akun Facebook Anda.

Klik ikon Cookie-Editor > Klik Export > Pilih JSON.

Buat file bernama fb_cookies.json di folder bot ini, lalu paste isinya ke sana.

2. Mengatur Daftar Grup (groups.json)
Buat file groups.json untuk menampung link grup tujuan:

JSON
[
  { "url": "[https://web.facebook.com/groups/link_grup_1](https://web.facebook.com/groups/link_grup_1)" },
  { "url": "[https://web.facebook.com/groups/link_grup_2](https://web.facebook.com/groups/link_grup_2)" }
]
3. Penyesuaian Path Chrome
Buka file script Python Anda, cari bagian executable_path dan pastikan lokasinya sudah benar sesuai PC Anda:

Default: C:\Program Files (x86)\Google\Chrome\Application\chrome.exe

🚀 Cara Menjalankan
Pastikan semua file (script.py, fb_cookies.json, dan groups.json) berada dalam satu folder. Jalankan dengan:

Bash
python nama_file_anda.py
