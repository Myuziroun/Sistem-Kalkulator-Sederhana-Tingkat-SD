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
            aritmatika_valid = False
            while not aritmatika_valid :
                print("Menu Perhitungan Aritmatika")
                print("1. Perhitungan Penjumlahan (+)")
                print("2. Perhitungan Pengurangan (-)")
                print("3. Perhitungan Pembagian   (:)")
                print("4. Perhitungan Perkalian   (x)")
                print("5. Kembali ke Menu Utama      ")
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
                    elif arit_menu == 5 :
                        aritmatika_valid = True
                    else:
                        print("Mohon maaf, hanya bisa memilih dengan pilihan yang ada")
                elif arit_menu.strip() == "":
                    print("Mohon maaf, wajib untuk diisi")
                else :
                    print("Mohon maaf hanya bisa menggunakan angka")
        elif choice == 2:
            bangun_datar_valid = False
            while not bangun_datar_valid :
                print("Menu Perhitungan Bangun Datar")
                print("1. Perhitungan Keliling Bangun Datar")
                print("2. Perhitungan Luas Bangun Datar")
                print("3. Kembali ke Menu Utama")
                bangun_datar_menu = input("Masukan pilihan untuk melakukan perhitungan: ")
                if  bangun_datar_menu.isdigit() :
                    bangun_datar_menu = int(bangun_datar_menu)
                    if bangun_datar_menu == 1:
                        keliling_valid = False
                        while not keliling_valid :
                            print("Menu Perhitungan Keliling Bangun datar")
                            print("1. Keliling Persegi")
                            print("2. Keliling Persegi Panjang")
                            print("3. Keliling Belah Ketupat")
                            print("4. Keliling Jajar Genjang")
                            print("5. Keliling Trapesium")
                            print("6. Keliling Layang - Layang")
                            print("7. Keliling Segitiga")
                            print("8. Keliling Lingkaran")
                            print("9. Kembali")
                            keliling_menu = input("Masukan pilihan untuk melakukan perhitungan: ")
                            if  keliling_menu.isdigit():
                                keliling_menu = int(keliling_menu)
                                if  keliling_menu  == 1 :
                                    sisi_persegi = int(input("Masukan Nilai Sisi Persegi: "))
                                    print("Hasil Keliling Persegi dengan sisi {} cm adalah {}" .format(sisi_persegi, k_persegi(sisi_persegi)))
                                elif keliling_menu == 2:
                                    panjang_persegiPanjang = int(input("Masukan Nilai Panjang Persegi Panjang: "))
                                    lebar_persegiPanjang = int(input("Masukan Nilai Lebar Persegi Panjang: "))
                                    print("Hasil Keliling Persegi Panjang dengan panjang {} cm dan lebar {} cm adalah {} cm" .format(panjang_persegiPanjang, lebar_persegiPanjang,k_persegiPanjang(panjang_persegiPanjang, lebar_persegiPanjang)))
                                elif keliling_menu == 3:
                                    a_belahKetupat = int(input("Masukan nilai A: "))
                                    b_belahKetupat = int(input("Masukan nilai B: "))
                                    c_belahKetupat = int(input("Masukan nilai C: "))
                                    d_belahKetupat = int(input("Masukan nilai D: "))
                                    print("Hasil Keliling Belah Ketupat adalah {} cm" .format(k_belahKetupat(a_belahKetupat,b_belahKetupat,c_belahKetupat,d_belahKetupat)))
                                elif keliling_menu == 4:
                                    a_jajarGenjang = int(input("Masukan nilai A: "))
                                    b_jajarGenjang = int(input("Masukan nilai B: "))
                                    c_jajarGenjang = int(input("Masukan nilai C: "))
                                    d_jajarGenjang = int(input("Masukan nilai D: "))
                                    print("Hasil Keliling Jajar Genjang adalah {} cm" .format(k_jarjarGenjang(a_jajarGenjang,b_jajarGenjang,c_jajarGenjang,d_jajarGenjang)))
                                elif keliling_menu == 5:
                                    a_trapesium = int(input("Masukan nilai A: "))
                                    b_trapesium = int(input("Masukan nilai B: "))
                                    c_trapesium = int(input("Masukan nilai C: "))
                                    d_trapesium = int(input("Masukan nilai D: "))
                                    print("Hasil Keliling Trapesium adalah {} cm" .format(k_trapesium(a_trapesium,b_trapesium,c_trapesium,d_trapesium)))
                                elif keliling_menu == 6 :
                                    a_layangLayang = int(input("Masukan nilai A: "))
                                    b_layangLayang = int(input("Masukan nilai B: "))
                                    c_layangLayang = int(input("Masukan nilai C: "))
                                    d_layangLayang = int(input("Masukan nilai D: "))
                                    print("Hasil Keliling Layang - Layang adalah {} cm" .format(k_layang_layang(a_layangLayang,b_layangLayang,c_layangLayang,d_layangLayang)))
                                elif keliling_menu == 7 :
                                    a_segitiga = int(input("Masukan nilai A: "))
                                    b_segitiga = int(input("Masukan nilai B: "))
                                    c_segitiga = int(input("Masukan nilai C: "))
                                    print("Hasil Keliling Segitiga adalah {} cm" .format(k_segitiga(a_segitiga,b_segitiga,c_segitiga)))
                                elif keliling_menu == 8 :
                                    jari_jari_lingkaran = int(input("Masukan Nilai Jari - Jari Lingkaran: "))
                                    print("Hasil Keliling Lingkaran adalah {} cm" .format(k_lingkaran(jari_jari_lingkaran)))
                                elif keliling_menu == 9 :
                                    keliling_valid = True
                                else:
                                    print("Mohon maaf, hanya bisa memilih dengan pilihan yang ada")                                                   
                            elif keliling_menu.strip() == "":
                                print("Mohon maaf, wajib untuk diisi")
                            else:
                                print("Mohon maaf hanya bisa menggunakan angka")
                    elif bangun_datar_menu == 2:
                        luas_valid = False
                        while not luas_valid :
                            print("Menu Perhitungan Luas Bangun datar")
                            print("1. Luas Persegi")
                            print("2. Luas Persegi Panjang")
                            print("3. Luas Belah Ketupat")
                            print("4. Luas Jajar Genjang")
                            print("5. Luas Trapesium")
                            print("6. Luas Layang - Layang")
                            print("7. Luas Segitiga")
                            print("8. Luas Lingkaran")
                            print("9. Kembali")
                            luas_menu = input("Masukan pilihan untuk melakukan perhitungan: ")
                            if luas_menu.isdigit():
                                luas_menu = int(luas_menu)
                            elif luas_menu.strip() == "":
                                print("Mohon maaf, wajib untuk diisi")
                            else:
                                print("Mohon maaf hanya bisa menggunakan angka") 

                    elif bangun_datar_menu == 3:
                        bangun_datar_valid = True
                    else :
                        print("Mohon maaf, hanya bisa memilih dengan pilihan yang ada")
                elif bangun_datar_menu.strip() == "":
                    print("Mohon maaf, wajib untuk diisi")
                else:
                    print("Mohon maaf hanya bisa menggunakan angka")
        elif choice == 3:
             bangun_ruang_valid = False
             while not bangun_ruang_valid :
                print("Menu Perhitungan Bangun Ruang")
                print("1. Perhitungan Luas Permukaan Bangun Ruang")
                print("2. Perhitungan Volume Bangun Ruang")
                print("3. Kembali ke Menu Utama")
                bangun_ruang_menu = input("Masukan pilihan untuk melakukan perhitungan:  ")
                if bangun_ruang_menu.isdigit():
                    bangun_ruang_menu = int(bangun_ruang_menu)
                    if bangun_ruang_menu == 1 :
                        print("Menu Perhitungan Luas Permukaan Bangun Ruang")
                    elif bangun_ruang_menu == 2:
                        print("Menu perhitungan Volume bangun Ruang")
                    elif bangun_datar_menu == 3:
                        bangun_ruang_valid = True
                    else :
                        print("Mohon maaf, hanya bisa memilih dengan pilihan yang ada")
                elif bangun_ruang_menu.strip() == "":
                    print("Mohon maag, wajib untuk diisi")
                else :
                    print("Mohon maaf, hanya bisa menggunakan angka")    
        elif choice == 4:
            perubahan_waktu_valid = False
            while not perubahan_waktu_valid :
                print("Menu Perubahan Waktu ")
                print("1. Perhitungan Perubahan Waktu Detik")
                print("2. Perhitungan Perubahan Waktu Menit")
                print("3. Perhitungan Perubahan Waktu Jam")
                print("4. Kembali ke Menu Utama")
                perubahan_waktu = input("Masukan pilihan untuk melakukan perhitungan: ")
                if perubahan_waktu.isdigit() :
                    perubahan_waktu = int(perubahan_waktu)
                    if perubahan_waktu == 1 :
                        print("Menu Perhitungan Perubahan Waktu Detik")
                    elif perubahan_waktu == 2:
                        print("Menu Perhitungan Perubahan Waktu Menit")
                    elif perubahan_waktu == 3:
                        print("Menu Perhitungan Perubahan Waktu Jam")
                    elif perubahan_waktu == 4 :
                        perubahan_waktu_valid == True
                    else : 
                        print("Mohon maaf, hanya bisa memilih dengan pilihan yang ada")
                elif perubahan_waktu.strip() == "":
                    print("Mohon maaf, wajib untuk diisi")
                else :
                    print("Mohon maaf, hanya bisa menggunakan angka")    
        elif choice == 5:
            perubahan_jarak_valid = False
            while not perubahan_jarak_valid : 
                print("Menu Perubahan Jarak")
                print("1. Perhitungan Perubahan Jarak Centimeter (CM) ")
                print("2. Perhitungan Perubahan Jarak Meter (M) ")
                print("3. Perhitungan Perubahan Jarak Kilometer (KM) ")
                print("4. Perhitungan Perubahan Jarak Mil    ")
                print("5. Kembali ke Menu Utama")
                perubahan_jarak = input("Masukan pilihan untuk melakukan perhitungan: ")
                if perubahan_jarak.isdigit():
                    perubahan_jarak = int(perubahan_jarak)
                    if perubahan_jarak == 1:
                        print("Menu Perhitungan Perubahan Jarak Centimeter (CM)")
                    elif perubahan_jarak == 2:
                        print("Menu Perhitungan Perubahan Jarak Meter (M)")
                    elif perubahan_jarak == 3:
                        print("Menu Perhitungan Perubahan Jarak Kilometer (KM)")
                    elif perubahan_jarak == 4:
                        print("Menu Perhitungan Perubahan Jarak Mil ")
                    elif perubahan_jarak == 5:
                        perubahan_jarak_valid = True
                    else:
                        print("Mohon maaf, hanya bisa memilih dengan pilihan yang ada")
                elif perubahan_jarak.strip() == "":
                    print("Mohon maaf, wajib untuk diisi")
                else:
                    print("Mohon maaf, hanya bisa menggunakan angka")    
        elif choice == 6:
            break
        else :
            print("Mohon maaf, hanya bisa memilih dengan pilihan yang ada")
    elif choice.strip() == "":
        print("Mohon maaf, wajib untuk diisi")
    else:
        print("Mohon maaf hanya bisa menggunakan angka")
