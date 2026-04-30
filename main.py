# ---------------------------------------------------------
# Project: Facebook Auto Post Bot
# Author: Roji Rohmatillah
# License: MIT License
# GitHub: https://github.com/RojiiR
# ---------------------------------------------------------

import json
import time
import os
import random
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout
from datetime import datetime

# ================= KONFIGURASI =================
POST_CONTENT = """
HAII GAISS AKU LAGI BIKIN GAME BEN 10 NIHH
BANTU KOMEN LIKE DAN SUBSCRIBE YAA JANGAN LUPA SHARE JUGAA
https://youtu.be/EoCiA2VaYXI!

""".format(time=datetime.now().strftime("%H:%M:%S"))

GROUPS_FILE = "groups.json"
COOKIES_FILE = "fb_cookies.json"
LOOP_POSTING = True
BATCH_DELAY_SECONDS = 600
PER_POST_DELAY_RANGE = (30, 60)
# ===============================================

class FacebookTextBot:
    def __init__(self) -> None:
        print("[*] Membuka Browser...")
        self.playwright = sync_playwright().start()

        os.system("taskkill /F /IM chrome.exe /T 2>nul")
        time.sleep(2)

        self.context = self.playwright.chromium.launch_persistent_context(
            user_data_dir=r"C:\ChromeBot29",
            executable_path=r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
            headless=False,
            args=[
                '--disable-notifications',
                '--no-sandbox',
            ]
        )

        self.page = self.context.pages[0] if self.context.pages else self.context.new_page()

        print("[*] Membuka Facebook...")
        self.page.goto("https://web.facebook.com", wait_until="domcontentloaded", timeout=60000)

        # Inject cookies kalau ada
        if os.path.exists(COOKIES_FILE):
            print("[*] Menginjek cookies...")
            with open(COOKIES_FILE, 'r') as f:
                cookies = json.load(f)

            for cookie in cookies:
                cookie.pop('hostOnly', None)
                cookie.pop('session', None)
                cookie.pop('storeId', None)
                cookie.pop('id', None)
                if 'sameSite' not in cookie or cookie['sameSite'] not in ['Strict', 'Lax', 'None']:
                    cookie['sameSite'] = 'None'

            self.context.add_cookies(cookies)
            print("[+] Cookies berhasil diinjek, reload halaman...")
            self.page.reload(wait_until="domcontentloaded", timeout=60000)
        else:
            print("[!] File fb_cookies.json tidak ditemukan, lanjut tanpa cookies...")

        # Cek apakah sudah login
        try:
            self.page.wait_for_selector("div[role='feed'], div[role='main']", timeout=10000)
            print("[+] Berhasil login!")
        except PlaywrightTimeout:
            print("[!] Belum login. Silakan login manual di browser yang terbuka...")
            print("[!] Setelah berhasil masuk Facebook, tekan Enter di sini...")
            input()

    def _click_post_box(self) -> bool:
        selectors = [
            "div[aria-label='Buat postingan']",
            "div[aria-label='Create a post']",
            "//span[contains(text(),'Tulis sesuatu')]/..",
            "//span[contains(text(),'Write something')]/..",
            "//div[@role='button'][.//span[contains(text(),'Apa yang')]]",
            "div[data-pagelet='GroupComposer'] div[role='button']",
        ]

        for sel in selectors:
            try:
                locator = self.page.locator(sel).first
                if locator.is_visible(timeout=3000):
                    locator.click()
                    print("\t[+] Kotak post ditemukan dan diklik.")
                    time.sleep(2)
                    return True
            except Exception:
                continue

        # Fallback: scroll ke atas dulu lalu coba lagi
        try:
            self.page.keyboard.press("Home")
            self.page.evaluate("window.scrollTo(0, 0)")
            time.sleep(2)
            for sel in selectors:
                try:
                    locator = self.page.locator(sel).first
                    if locator.is_visible(timeout=3000):
                        locator.click()
                        print("\t[+] Kotak post ditemukan setelah scroll.")
                        time.sleep(2)
                        return True
                except Exception:
                    continue
        except Exception:
            pass

        return False

    def _type_and_post(self) -> bool:
        # Tunggu dialog composer muncul (bukan komentar)
        composer_selectors = [
            "div[aria-label='Buat postingan']",
            "div[aria-label='Create a post']",
            "form[method='POST']",
            "div[data-testid='status-attachment-mentions-input']",
        ]

        composer = None
        for sel in composer_selectors:
            try:
                el = self.page.locator(sel).first
                if el.is_visible(timeout=3000):
                    composer = el
                    break
            except Exception:
                continue

        # Cari textbox khusus di dalam composer, bukan sembarang contenteditable
        try:
            if composer:
                editor = composer.locator("div[contenteditable='true']").first
            else:
                # Filter: ambil yang aria-label bukan komentar
                editor = self.page.locator(
                    "div[contenteditable='true'][role='textbox']:not([aria-label*='komentar']):not([aria-label*='comment']):not([aria-label*='jawaban']):not([aria-label*='answer'])"
                ).first

            editor.wait_for(timeout=10000)
        except PlaywrightTimeout:
            print("\t[-] Area ketik tidak muncul.")
            return False

        # Klik dan fokus pakai JS
        #self.page.keyboard.press("Escape")
        time.sleep(1)
        editor.evaluate("el => el.click()")
        time.sleep(1)
        editor.evaluate("el => el.focus()")
        time.sleep(1)

        # Pastikan masih di composer (belum tertutup)
        try:
            editor.wait_for(state="visible", timeout=5000)
        except PlaywrightTimeout:
            print("\t[-] Dialog composer tertutup sebelum mengetik.")
            return False

        self.page.keyboard.type(POST_CONTENT, delay=40)
        print("\t[+] Teks berhasil diketik.")
        time.sleep(4)

        # Tombol Post harus di dalam dialog composer
        post_btn_selectors = [
            "div[aria-label='Posting']",
            "div[aria-label='Post']",
            "//div[@role='dialog']//div[@role='button'][.//span[text()='Posting']]",
            "//div[@role='dialog']//div[@role='button'][.//span[text()='Post']]",
            "//div[@role='button'][.//span[text()='Posting']]",
            "//div[@role='button'][.//span[text()='Post']]",
        ]

        for sel in post_btn_selectors:
            try:
                btn = self.page.locator(sel).first
                if btn.is_enabled(timeout=3000):
                    btn.evaluate("el => el.click()")
                    print("\t[+] SUKSES: Post terkirim!")
                    time.sleep(3)
                    return True
            except Exception:
                continue

        print("\t[-] GAGAL: Tombol Post tidak ditemukan.")
        return False

    def post_to_group(self, url: str):
        print(f"\n[*] Menuju grup: {url}")

        try:
            self.page.goto(url, wait_until="domcontentloaded", timeout=60000)
        except PlaywrightTimeout:
            print("\t[-] Timeout saat buka grup, skip...")
            return

        try:
            self.page.wait_for_selector(
                "div[data-pagelet='GroupFeed'], div[role='feed']",
                timeout=15000
            )
        except PlaywrightTimeout:
            print("\t[-] Feed grup tidak muncul, skip...")
            return

        time.sleep(random.uniform(3, 5))

        if not self._click_post_box():
            print("\t[-] Tidak bisa klik kotak post, skip...")
            return

        self._type_and_post()

    def run(self):
        if not os.path.exists(GROUPS_FILE):
            print(f"[-] Error: File '{GROUPS_FILE}' tidak ditemukan.")
            return

        with open(GROUPS_FILE, 'r') as f:
            groups = json.load(f)

        if not groups:
            print("[-] File groups.json kosong.")
            return

        print(f"[+] {len(groups)} grup ditemukan.")

        try:
            while True:
                print(f"\n🚀 Memulai siklus posting: {datetime.now().strftime('%H:%M:%S')}")

                for group in groups:
                    url = group.get('url', '').strip()
                    if not url:
                        print("[!] Lewat entri tanpa URL.")
                        continue

                    self.post_to_group(url)

                    wait = random.uniform(*PER_POST_DELAY_RANGE)
                    print(f"\t[*] Jeda {wait:.1f} detik sebelum grup berikutnya...")
                    time.sleep(wait)

                if not LOOP_POSTING:
                    break

                print(f"\n[✓] Semua grup selesai. Istirahat {BATCH_DELAY_SECONDS} detik...")
                time.sleep(BATCH_DELAY_SECONDS)

        except KeyboardInterrupt:
            print("\n[!] Bot dihentikan manual.")
        finally:
            self.context.close()
            self.playwright.stop()

if __name__ == "__main__":
    FacebookTextBot().run()