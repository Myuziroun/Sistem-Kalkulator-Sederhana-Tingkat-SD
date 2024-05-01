from rumusBangunDatarRuang import * ;

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
                        if  luas_menu == 1 :
                            sisi_persegi_luas = float(input("Masukan Nilai Sisi Persegi: "))
                            print("Hasil Luas Persegi dengan panjang sisi {} cm adalah {} cm^2" .format(sisi_persegi_luas,L_Persegi(sisi_persegi)))
                        elif luas_menu == 2:
                            panjang_persegiPanjang_luas = float(input("Masukan Nilai Panjang Persegi Panjang: "))
                            lebar_persegiPanjang_luas = float(input("Masukan Nilai Lebar Persegi Panjang: "))
                            print("Hasil Luas Persegi Panjang dengan panjang {} dan lebar {} adalah {} cm^2" .format(panjang_persegiPanjang_luas, lebar_persegiPanjang_luas, L_persegiPanjang(panjang_persegiPanjang_luas, lebar_persegiPanjang_luas)))
                        elif luas_menu == 3:
                            diagonal_satu_belahKetupat_luas = float(input("Masukan nilai Diagonal 1: "))
                            diagonal_dua_belahKetupat_luas = float(input("Masukan nilai Diagonal 2: "))
                            print("Hasil Luas Belah Ketupat dengan Diagonal 1 {} cm dan Diagonal 2 {} cm adalah {} cm^2" .format(diagonal_satu_belahKetupat_luas, diagonal_dua_belahKetupat_luas, L_belahKetupat(diagonal_satu_belahKetupat_luas,diagonal_dua_belahKetupat_luas)))
                        elif luas_menu == 4:
                            panjang_jajarGenjang_luas = float(input("Masukan Nilai Panjang Jajar Genjang: "))
                            lebar_jajarGenjang_luas = float(input("Masukan Nilai Lebar Jajar Genjang: "))
                            print("Hasil Luas Jajar Genjang dengan Panjang {} cm dan Lebar {} cm adalah {} cm^2" .format(panjang_jajarGenjang_luas, lebar_jajarGenjang_luas, L_jajarGenjang(panjang_jajarGenjang_luas, lebar_jajarGenjang_luas)))
                        elif luas_menu == 5:
                            a_trapesium_luas = float(input("Masukan Nilai A Trapesium: "))
                            b_trapesium_luas = float(input("Masukan Nilai B Trapesium: "))
                            tinggi_trapesium_luas = float(input("Masukan Nilai Tinggi Trapesium: "))
                            print("Hasil Luas Jajar Genjang dengan a {} cm, b {} cm, dan Tinggi {} cm adalah {} cm^2" .format(a_trapesium_luas, b_trapesium_luas, tinggi_trapesium_luas, L_trapesium(a_trapesium_luas, b_trapesium_luas, tinggi_trapesium_luas)))
                        elif luas_menu == 6 :
                            diagonal_satu_layang_luas = float(input("Masukan Nilai Diagonal 1 Layang - Layang: "))
                            diagonal_dua_layang_luas = float(input("Masukan Nilai Diagonal 2 Layang - Layang: "))
                            print("Hasil Luas Layang - Layng dengan Diagonal 1 {} cm dan Diagonal 2 {} adalah {} cm^2" .format(diagonal_satu_belahKetupat_luas, diagonal_dua_layang_luas, L_layang_layang(diagonal_satu_layang_luas, diagonal_dua_layang_luas)))
                        elif luas_menu == 7 :
                            alas_segitiga_luas = float(input("Masukan Nilai Alas Segitiga: "))
                            tinggi_segitiga_luas = float(input("Masukan Nilai Tinggi Segitiga: "))
                            print("Hasil Luas Segitiga dengan Alas {} cm dan Tinggi {} adalah {} cm^2" .format(alas_segitiga_luas, tinggi_segitiga_luas, L_Segitiga(alas_segitiga_luas, tinggi_segitiga_luas)))
                        elif luas_menu == 8 :
                            jari_lingkaran_luas = float(input("Masukan Nilai Jari - Jari Lingkaran: "))
                            print("Hasil Luas Lingkaran dengan Jari - Jari {} cm adalah {} cm^2" .format(jari_lingkaran_luas, L_lingkaran(jari_lingkaran_luas)))                          
                        elif luas_menu == 9 :
                            luas_valid == True
                        else:
                            print("Mohon maaf hanya bisa memilih yang ada pada menu pilihan")
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
                luas_permukaan_valid = False
                while not luas_permukaan_valid :
                    print("Menu Perhitungan Luas Permukaan Bangun Ruang")
                    print("1. Luas Permukaan Kubus")
                    print("2. Luas Permukaan Balok")
                    print("3. Luas Permukaan Limas segiempat")
                    print("4. Luas Permukaan Prisma Segitiga")
                    print("5. Luas Permukaan Limas Segitiga")
                    print("6. Luas Permukaan Selinder")
                    print("7. Luas Permukaan Kerucut")
                    print("8. Luas Permukaan Bola")
                    print("9 . Kembali")
                    luas_permukaan_menu = input("Masukan pilihan untuk melakukan perhitungan: ")
                    if luas_permukaan_menu.isdigit() :
                        luas_permukaan_menu = int(luas_permukaan_menu)
                        if luas_permukaan_menu == 1:
                            rusuk_kubus_luas = float(input("Masukan Nilai Rusuk Kubus: "))
                            print("Hasil Luas Permukaan Kubus dengan Rusuk {}cm adalah {}cm^3" .format(rusuk_kubus_luas, L_kubus(rusuk_kubus_luas)))
                        elif luas_permukaan_menu == 2:
                            panjang_balok_luas = float(input("Masukan Nilai Panjang Balok: "))
                            lebar_balok_luas = float(input("Masukan Nilai Lebar Balok: "))
                            tinggi_balok_luas = float(input("Masukan Nilai Tinggi Balok: "))
                            print("Hasil Luas Permukaan Balok dengan Panjang {}cm, Lebar {}cm dan Tinggi {}cm adalah {}cm^3" .format(panjang_balok_luas, lebar_balok_luas, tinggi_balok_luas, L_balok(panjang_balok_luas, lebar_balok_luas, tinggi_balok_luas)))
                        elif luas_permukaan_menu == 3:
                            sisi_limas_segiempat_luas = float(input("Masukan Nilai Sisi Limas Segiempat: "))
                            tinggi_limas_segiempat_luas = float(input("Masukan Nilai Tinggi Limas Segiempat: "))
                            print("Hasil Luas Permukaan Limas Segiempat dengan Sisi {}cm dan Tinggi {}cm  adalah {}cm^3" .format(sisi_limas_segiempat_luas, tinggi_limas_segiempat_luas,L_limas_SegiEmpat(sisi_limas_segiempat_luas, tinggi_limas_segiempat_luas)))
                        elif luas_permukaan_menu == 4:
                            a_prisma_luas = float(input("Masukan Nilai A Prisma: "))
                            b_prisma_luas = float(input("Masukan Nilai B Prisma: "))
                            c_prisma_luas = float(input("Masukan Nilai C Prisma: "))
                            alas_prisma_luas = float(input("Masukan Nilai Alas Prisma: "))
                            tinggi_prisma_luas = float(input("Masukan Nilai Tinggi Segitiga Prisma: "))
                            Tinggi_prisma_luas = float(input("Masukan Nilai Tinggi Prisma: "))
                            print("Hasil Luas Permukaan Prisma dengan a {}cm, b {}cm,"\
                                  " c {}cm, alas {}cm tinggi segitiga {} cm dan tinggi prisma {}cm "\
                                    "adalah {}cm^3" .format(a_prisma_luas, b_prisma_luas, c_prisma_luas, alas_prisma_luas, tinggi_prisma_luas, Tinggi_prisma_luas, L_prisma(a_prisma_luas, b_prisma_luas, c_prisma_luas, alas_prisma_luas, tinggi_prisma_luas, Tinggi_prisma_luas)))
                        elif luas_permukaan_menu == 5:
                            sisi_limas_segitiga_luas = float(input("Masukan Nilai Sisi Limas Segitiga: "))
                            tinggi_limas_segitiga_luas = float(input("Masukan Nilai Tinggi Limas Segitiga: "))
                            print("Hasil Luas Permukaan Limas Segitiga dengan Sisi {}cm dan Tinggi {}cm adalah {}cm^3" .format(sisi_limas_segitiga_luas,tinggi_limas_segitiga_luas, L_limas_Segi_tiga(sisi_limas_segitiga_luas,tinggi_limas_segitiga_luas)))
                        elif luas_permukaan_menu == 6:
                            jari_tabung_luas = float(input("Masukan Nilai Jari - Jari Tabung: "))
                            tinggi_tabung_luas = float(input("Masukan Nilai Tinggi Tabung: "))
                            print("Hasil Luas Permukaan Tabung dengan Jari - Jari {}cm, dan Tinggi {}cm adalah {}cm^3" .format(jari_tabung_luas,tinggi_tabung_luas, L_selinder(jari_tabung_luas,tinggi_tabung_luas)))
                        elif luas_permukaan_menu == 7:
                            sisi_Kerucut_luas = float(input("Masukan Nilai Sisi Kerucut: "))
                            jari_Kerucut_luas = float(input("Masukan Nilai Jari - jari Kerucut: "))
                            print("Hasil Luas Permukaan Kerucut dengan Sisi {}cm, dan Jari - Jari {}cm adalah {}cm^3" .format(sisi_Kerucut_luas, jari_Kerucut_luas, L_kerucut(sisi_Kerucut_luas, jari_Kerucut_luas)))
                        elif luas_permukaan_menu == 8:
                            jari_bola_luas = float(input("Masukan Nilai Jari - Jari Bola: "))
                            print("Hasil Luas Permukaan Bola dengan Jari - Jari {}cm adalah {}cm^3" .format(jari_bola_luas, L_bola(jari_bola_luas)))
                        elif luas_permukaan_menu == 9:
                            luas_permukaan_valid = True
                        else :
                            print("Mohon maaf hanya bisa memilih yang ada pada menu pilihan")                 
                    elif luas_permukaan_menu.strip() == "":
                        print("Mohon maaf, wajib untuk diisi")
                    else:
                        print("Mohon maaf hanya bisa menggunakan angka")
            elif bangun_ruang_menu == 2:
                volume_valid = False
                while not volume_valid :
                    print("Menu perhitungan Volume bangun Ruang")
                    print("1. Volume Kubus")
                    print("2. Volume Balok")
                    print("3. Volume Limas segiempat")
                    print("4. Volume Prisma Segitiga")
                    print("5. Volume Limas Segitiga")
                    print("6. Volume Tabung")
                    print("7. Volume Kerucut")
                    print("8. Volume Bola")
                    print("9 . Kembali")
                    volume_menu = input("Masukan Pilihan untuk melakukan perhitungan: ")
                    if volume_menu.isdigit():
                        volume_menu = int(volume_menu)
                        if volume_menu == 1 :
                            rusuk_kubus_volume =float(input("Masukan Nilai Rusuk Kubus: "))
                            print("Hasil perhitungan Volume Kubus dengan Rusuk {}cm adalah {}cm^3" .format(rusuk_kubus_volume,V_kubus(rusuk_kubus_volume)))
                        elif volume_menu == 2 :
                            panjang_balok_volume =float(input("Masukan Nilai Panjang Balok: "))
                            lebar_balok_volume =float(input("Masukan Nilai Lebar Balok: "))
                            tinggi_balok_volume =float(input("Masukan Nilai Tinggi Balok: "))
                            print("Hasil perhitungan Volume Balok dengan Panjang {}cm, Lebar {}cm, dan Tinggi {}cm adalah {}cm^3" .format(panjang_balok_volume,lebar_balok_volume, tinggi_balok_volume,V_balok(panjang_balok_volume,lebar_balok_volume, tinggi_balok_volume)))
                        elif volume_menu == 3 :
                            sisi_limas_segiempat_volume =float(input("Masukan Nilai Rusuk Limas Segiempat: "))
                            tinggi_limas_segiempat_volume =float(input("Masukan Nilai Rusuk Limas Segiempat: "))
                            print("Hasil perhitungan Volume Limas Segiempat dengan Sisi {}cm dan Tinggi {}cm adalah {}cm^3" .format(sisi_limas_segiempat_volume, tinggi_limas_segiempat_volume,V_limas_segiempat(sisi_limas_segiempat_volume, tinggi_limas_segiempat_volume)))
                        elif volume_menu == 4 :
                            alas_prisma_segitiga_volume =float(input("Masukan Nilai Alas Prisma Segitiga: "))
                            tinggi_prisma_segitiga_volume =float(input("Masukan Nilai Tinggi Segitiga: "))
                            Tinggi_prisma_segitiga_volume =float(input("Masukan Nilai Tinggi Prisma: "))
                            print("Hasil perhitungan Volume Prisma Segitiga dengan Alas {}cm, Tinggi Segitiga {}cm, dan Tinggi Prisma {}cm adalah {}cm^3" .format(alas_prisma_segitiga_volume,tinggi_prisma_segitiga_volume,Tinggi_prisma_segitiga_volume,V_prisma_Segitiga(alas_prisma_segitiga_volume,tinggi_prisma_segitiga_volume,Tinggi_prisma_segitiga_volume)))
                        elif volume_menu == 5 :
                            alas_limas_Segitiga_volume =float(input("Masukan Nilai Alas Limas Segitiga: "))
                            tinggi_limas_Segitiga_volume =float(input("Masukan Nilai Tinggi Segitiga: "))
                            Tinggi_limas_Segitiga_volume =float(input("Masukan Nilai Tinggi Limas Segitiga: "))
                            print("Hasil perhitungan Volume Limas Segitiga dengan Alas {}cm, Tinggi Segitiga {}cm, dan Tinggi Prisma {}cm adalah {}cm^3" .format(alas_limas_Segitiga_volume,tinggi_limas_Segitiga_volume,Tinggi_limas_Segitiga_volume,V_limas_Segi_tiga(alas_limas_Segitiga_volume,tinggi_limas_Segitiga_volume,Tinggi_limas_Segitiga_volume)))
                        elif volume_menu == 6 :
                            jari_tabung_volume =float(input("Masukan Nilai Jari - Jari Tabung: "))
                            tinggi_tabung_volume =float(input("Masukan Nilai Tinggi Tabung: "))
                            print("Hasil perhitungan Volume Tabung dengan Jari - Jari {}cm, dan Tinggi {}cm adalah {}cm^3" .format(jari_tabung_volume,tinggi_tabung_volume,V_tabung(jari_tabung_volume, tinggi_tabung_volume)))
                        elif volume_menu == 7 :
                            jari_kerucut_volume =float(input("Masukan Nilai Jari - Jari Kerucut: "))
                            tinggi_kerucut_volume =float(input("Masukan Nilai Tinggi Kerucut: "))
                            print("Hasil perhitungan Volume Kerucut dengan Jari - Jari {}cm, dan Tinggi {}cm adalah {}cm^3" .format(jari_kerucut_volume, tinggi_kerucut_volume,V_kerucut(jari_kerucut_volume, tinggi_kerucut_volume)))
                        elif volume_menu == 8 :
                            jari_bola_volume =float(input("Masukan Nilai Jari - Jari Bola: "))
                            print("Hasil perhitungan Volume Bola dengan Jari - Jari {}cm adalah {}" .format(jari_bola_volume,V_bola(jari_bola_volume)))
                        elif volume_menu == 9 :
                            volume_valid = True
                        else:
                            print("Mohon maaf hanya bisa memilih yang ada pada menu pilihan")                 
                    elif volume_menu.strip() == "":
                        print("Mohon maaf, wajib untuk diisi")
                    else:
                        print("Mohon maaf hanya bisa menggunakan angka")
            elif bangun_ruang_menu == 3:
                bangun_ruang_valid = True
            else :
                print("Mohon maaf, hanya bisa memilih dengan pilihan yang ada")
        elif bangun_ruang_menu.strip() == "":
            print("Mohon maag, wajib untuk diisi")
        else :
            print("Mohon maaf, hanya bisa menggunakan angka")    