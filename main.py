from pageAritmatika import *;
from pageBangunRuangDatar import page_bangun_Datar, page_bangun_ruang;
from pagePerhitunganJarak import *;
from pagePerhitunganWaktu import page_perubahan_waktu;


while True:
    print("Menu Utama")
    print("1. Perhitungan Aritmatika ( + , - ,  : ,  x ) ")
    print("2. Perhitungan Bangun Datar ")
    print("3. Perhitungan Bangun Ruang ")
    print("4. Perhitungan Perubahan Waktu ")
    print("5. Perhitungan Perubahan Jarak ")
    print("6. Keluar ")
    choice = input("Masukan pilihan untuk melakukan perhitungan: ")
    if choice.isdigit() :
        choice = int(choice)
        if choice == 1:
            page_Aritamtika()
        elif choice == 2:
            page_bangun_Datar()
        elif choice == 3:
             page_bangun_ruang()
        elif choice == 4:
            page_perubahan_waktu()
        elif choice == 5:
            page_perubahan_jarak()
        elif choice == 6:
            break
        else :
            print("Mohon maaf, hanya bisa memilih dengan pilihan yang ada")
    elif choice.strip() == "":
        print("Mohon maaf, wajib untuk diisi")
    else:
        print("Mohon maaf hanya bisa menggunakan angka")
