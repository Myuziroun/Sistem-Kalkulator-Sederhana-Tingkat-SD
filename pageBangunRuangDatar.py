from rumusBangunDatarRuang import k_belahKetupat, k_jarjarGenjang, k_layang_layang, k_lingkaran, k_persegi, k_persegiPanjang, k_segitiga, k_trapesium ;

def page_bangun_Datar() :
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


def page_bangun_ruang() :
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
            elif bangun_ruang_menu == 3:
                bangun_ruang_valid = True
            else :
                print("Mohon maaf, hanya bisa memilih dengan pilihan yang ada")
        elif bangun_ruang_menu.strip() == "":
            print("Mohon maag, wajib untuk diisi")
        else :
            print("Mohon maaf, hanya bisa menggunakan angka")    