'''
File: start.py
Author: TarnaWijaya 
Description: Cracker Beta
'''

import pywhatkit as kit

# Format: 'phone_number', 'message', hour, minute
phone_number = '+6285135530429'  # Ganti dengan nomor WhatsApp penerima
message = 'Halo, ini pesan otomatis dari Python!'
hour = 15  # Jam (format 24 jam)
minute = 30  # Menit

# Mengirim pesan ke WhatsApp
kit.sendwhatmsg(phone_number, message, hour, minute)