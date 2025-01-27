'''
File: start.py
Author: TarnaWijaya 
Description: Cracker Beta
'''
import pyautogui
import time
import webbrowser

# Nomor tujuan dan pesan
phone_number = '+6285135530429'  # Ganti dengan nomor WhatsApp penerima
message = 'Halo, ini pesan otomatis dari Python!'

# Buka WhatsApp Web
webbrowser.open(f'https://web.whatsapp.com/send?phone={phone_number}&text={message}')
time.sleep(10)  # Tunggu beberapa detik agar WhatsApp Web terbuka dan siap

while True:
    pyautogui.write(message)  # Ketik pesan
    pyautogui.press('enter')  # Tekan tombol Enter untuk mengirim pesan
    time.sleep(1)  # Tunggu 1 detik sebelum mengirim pesan lagi
