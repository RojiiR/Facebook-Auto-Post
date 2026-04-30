# Facebook Auto Post - Playwright Edition 🚀

Developed with ❤️ by **ZII DEV** (Roji Rohmatillah)

[![YouTube](https://img.shields.io/badge/YouTube-ZII%20DEV-red?style=for-the-badge&logo=youtube)](https://www.youtube.com/@ziideveloper)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)

## 📋 Deskripsi
Bot automasi untuk posting ke grup Facebook menggunakan **Python** dan **Playwright**. Alat ini dirancang untuk membantu para *indie developer* atau *content creator* mempromosikan karya mereka (seperti devlog game) secara efisien tanpa perlu posting manual satu per satu.

---

## 🛠️ Persiapan & Instalasi

### 1. Prasyarat Sistem
Pastikan perangkat Anda sudah memenuhi kriteria berikut:
*   **Python 3.8+** terinstal.
*   **Google Chrome** terinstal (untuk sinkronisasi browser).

### 2. Instalasi Library
Jalankan perintah berikut di Terminal/CMD untuk menginstal dependensi yang diperlukan:
```bash
# Install library Playwright
pip install playwright

# Install browser driver khusus Chromium
playwright install chromium

```
---
## ⚙️ Konfigurasi

### 1. Setup Sesi Login (`fb_cookies.json`)

Bot ini menggunakan cookies agar tidak perlu login berulang dan mengurangi risiko checkpoint.

```bash
**Langkah-langkah:**

1. Install ekstensi **Cookie-Editor** di Chrome  
2. Login ke akun Facebook Anda  
3. Klik ikon Cookie-Editor → **Export** → pilih **JSON**  
4. Buat file `fb_cookies.json` di folder project  
5. Paste hasil export ke dalam file tersebut  

---
```
### 2. Daftar Grup (`groups.json`)

Buat file `groups.json` dan isi dengan format berikut:


```bash
[
  { "url": "https://web.facebook.com/groups/link_grup_1" },
  { "url": "https://web.facebook.com/groups/link_grup_2" }
]

```
### 3. Konfigurasi Path Chrome

Buka file `.py` dan sesuaikan `executable_path` dengan lokasi Chrome di perangkat Anda.

Contoh default di Windows:

```bash
C:\Program Files (x86)\Google\Chrome\Application\chrome.exe
```
## 🚀 Cara Menjalankan

Jalankan bot dengan perintah berikut:

```bash
python bot_fb.py
```
