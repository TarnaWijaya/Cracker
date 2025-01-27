'''
File: start.py
Author: TarnaWijaya 
Description: Cracker Beta
'''

import requests
from bs4 import BeautifulSoup

# URL situs web target (ganti dengan situs web yang diizinkan untuk di-scrape)
url = "https://example.com"

# Mengirim permintaan HTTP ke situs web
response = requests.get(url)

# Memeriksa apakah permintaan berhasil
if response.status_code == 200:
    # Parsing HTML dengan BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Contoh: Mengambil semua teks dari elemen tertentu (misalnya, judul)
    titles = soup.find_all('h1')
    for i, title in enumerate(titles, 1):
        print(f"{i}. {title.text}")
else:
    print(f"Gagal mengakses situs web. Status code: {response.status_code}")