'''
File: start.py
Author: TarnaWijaya 
Description: Cracker Beta
'''

import sys

def fungsi_1():
    print("Anda memilih fungsi 1. Ini adalah fungsi pertama.")
    # Tambahkan logika lain di sini jika diperlukan

def fungsi_2():
    print("Anda memilih fungsi 2. Ini adalah fungsi kedua.")
    # Tambahkan logika lain di sini jika diperlukan

def menu():
    while True:
        print("\nPilih menu:")
        print("1. Fungsi 1")
        print("2. Fungsi 2")
        print("0. Keluar")
        pilihan = input("Masukkan pilihan Anda: ")
        
        if pilihan == "1":
            fungsi_1()
        elif pilihan == "2":
            fungsi_2()
        elif pilihan == "0":
            print("Keluar dari program. Sampai jumpa!")
            sys.exit()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    menu()