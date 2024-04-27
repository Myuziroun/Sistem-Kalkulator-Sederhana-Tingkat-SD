from operasiAritmatika import penjumlahan, pengurangan, pembagian, perkalian;
from rumusBangunDatarRuang import *;
from satuanJarak import centimeter_ke_kilomter, centimeter_ke_meter, centimeter_ke_mil, meter_ke_centimeter, meter_ke_kilometer, meter_ke_mil, mil_ke_centimeter, mil_ke_kilometer, mil_ke_meter, kilometer_ke_centimeter, kilometer_ke_meter, kilometer_ke_mil;
from satuanWaktu import second_to_minute, second_to_hour,  minute_to_hour, minute_to_second, hour_to_minute, hour_to_second;


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
            print("Menu Perhitungan Aritmatika")
            print("1. Perhitungan Penjumlahan (+)")
            print("2. Perhitungan Pengurangan (-)")
            print("3. Perhitungan Pembagian   (:)")
            print("4. Perhitungan Perkalian   (x)")
            arit_menu = input("Masukan pilihan untuk melakukan perhitungan: ")
            if arit_menu.isdigit():
                arit_menu = int(arit_menu)
                if arit_menu == 1:
                    a = float(input("Masukan angka a: "))
                    b = float(input("Masukan angka b: "))
                    print("Hasil penjumlahan a dan b adalah {}" .format(penjumlahan(a,b)))
                elif arit_menu == 2:
                    a = float(input("Masukan angka a: "))
                    b = float(input("Masukan angka b: "))
                    print("Hasil pengurangan a dan b adalah {}" .format(pengurangan(a,b)))
                elif arit_menu == 3:
                    a = float(input("Masukan angka a: "))
                    b = float(input("Masukan angka b: "))
                    print("Hasil pembagian a dan b adalah {}" .format(pembagian(a,b)))
                elif arit_menu == 4:
                    a = float(input("Masukan angka a: "))
                    b = float(input("Masukan angka b: "))
                    print("Hasil perkalian a dan b adalah {}" .format(perkalian(a,b)))
                else:
                    print("Mohon maaf, hanya bisa memilih dengan pilihan yang ada")
            elif arit_menu.strip() == "":
                print("Mohon maaf, wajib untuk diisi")
            else :
                print("Mohon maaf hanya bisa menggunakan angka")
        elif choice == 2:
            print("Menu Perhitungan Bangun Datar")
            print("1. Perhitungan Keliling Bangun Datar")
            print("2. Perhitungan Luas Bangun Datar")
            bangun_datar_menu = input("Masukan pilihan untuk melakukan perhitungan: ")
            if  bangun_datar_menu.isdigit() :
                bangun_datar_menu = int(bangun_datar_menu)
                if bangun_datar_menu == 1:
                    print("Menu Perhitungan Keliling Bangun datar")
                    print("1. Keliling Persegi")
                    print("2. Keliling Persegi Panjang")
                    print("3. Keliling Belah Ketupat")
                    print("4. Keliling Jajar Genjang")
                    print("5. Keliling Trapesium")
                    print("6. Keliling Layang - Layang")
                    print("7. Keliling Segitiga")
                    print("8. Keliling Lingkaran")
                elif bangun_datar_menu == 2:
                    print("Menu Perhitungan Luas Bangun datar")
                    print("1. Luas Persegi")
                    print("2. Luas Persegi Panjang")
                    print("3. Luas Belah Ketupat")
                    print("4. Luas Jajar Genjang")
                    print("5. Luas Trapesium")
                    print("6. Luas Layang - Layang")
                    print("7. Luas Segitiga")
                    print("8. Luas Lingkaran")
            elif bangun_datar_menu.strip() == "":
                print("Mohon maaf, wajib untuk diisi")
            else:
                print("Mohon maaf hanya bisa menggunakan angka")
        elif choice == 3:
             print("Menu Perhitungan Bangun Ruang")
             print("1. Perhitungan Luas Bangun Ruang")
             print("2. Perhitungan Volume Bangun Ruang")
             
        elif choice == 4:
        elif choice == 5:
        elif choice == 6:
            break
        else :
            print("Mohon maaf, hanya bisa memilih dengan pilihan yang ada")
    elif choice.strip() == "":
        print("Mohon maaf, wajib untuk diisi")
    else:
        print("Mohon maaf hanya bisa menggunakan angka")
