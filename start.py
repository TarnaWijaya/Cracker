'''
File: start.py
Author: TarnaWijaya 
Description: Cracker Beta
'''

import os
import sys

def run_script(script_path):
    os.system(f"sh {script_path}")

def show_notification(message, emoji):
    os.system(f"cmd notification post -S bigtext -t 'TarzAI' 'Tag' '{emoji}' > /dev/null 2>&1")

def main():
    print("""
____  ______________                        _____  .___ 
\   \/  /\__    ___/____ _______________   /  _  \ |   |
 \     /   |    |  \__  \\_  __ \___   /  /  /_\  \|   |
 /     \   |    |   / __ \|  | \//    /  /    |    \   |
/___/\  \  |____|  (____  /__|  /_____ \ \____|__  /___|
      \_/               \/            \/         \/     

[ ☞⁠￣⁠ᴥ⁠￣⁠☞ Selamat Datang di module Tarz AI ]

☞ Developer            | @axs_tarna
☞ My Name Developer    | Tarna
☞ Version Module       | 5.8
☞ Type Module          | Non Root
☞ Status               | Home
☞ All my media         | https://tarna-wijaya.vercel.app

☞ Description: untuk mengoptimalkan saja, tergantung pada hp saja apakah mendukung atau tidak

Pilih option value:[ Rawrrrrrrrr🦖 ]
contoh: python main.py <0/1>
1. Memasang
0. Mengembalikan
""")
    
    pilihan = input("Masukkan pilihan Anda (1/0): ")
    
    if pilihan == "1":
        run_script("/sdcard/Tarz/service/run.sh")
        show_notification("Memasang", "🗿👍")
    elif pilihan == "0":
        run_script("/sdcard/Tarz/service/rm.sh")
        show_notification("Mengembalikan", "🗿👎")
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()