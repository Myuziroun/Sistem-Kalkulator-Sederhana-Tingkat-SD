from satuanWaktu import *;

def page_perubahan_waktu() :
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
                detik_valid = False
                while not detik_valid :
                    print("Menu Perhitungan Perubahan Waktu Detik")
                    print("1. Perhitungan Detik ke Menit")
                    print("2. Perhitungan Detik ke Jam")
                    print("3. Kembali ke Menu Utama ")
                    detik_menu = input("Masukan pilihan untuk melakukan perhitungan: ")
                    if detik_menu.isdigit() :
                        detik_menu = int(detik_menu)
                        if detik_menu == 1 :
                            detik_menit = int(input("Masukan Jumlah Detik yang ingin dirubah ke Menit:  "))
                            print("Hasil perubahan dari {} detik ke menit adalah {} menit" .format(detik_menit, second_to_minute(detik_menit)))
                        elif detik_menu == 2:
                            detik_jam = int(input("Masukan Jumlah Detik yang ingin dirubah ke Jam: "))
                            print("Hasil perubahan dari {} detik ke jam adalah {} jam" .format(detik_jam, second_to_hour(detik_jam)))
                        elif detik_menu == 3:
                            detik_valid = True
                        else:
                            print("Mohon maaf hanya bisa memilih sesuai dengan menu :3")
                    elif detik_menu.strip() == "" :
                        print("Mohon maaf, isian tidak boleh kosong")
                    else :
                        print("Mohon maaf hanya bisa memilih dengan Angka ")
            elif perubahan_waktu == 2:
                menit_valid = False
                while not menit_valid:
                    print("Menu Perhitungan Perubahan Waktu Menit")
                    print("1. Perhitungan Menit ke Detik")
                    print("2. Perhitungan Menit ke Jam")
                    print("3. Kembali ke Menu Utama ")
                    menit_menu = int(input("Masukan pilihan untuk melakukan perhitungan: "))
                    if menit_menu.isdigit() :
                        menit_menu = int(menit_menu)
                        if menit_menu == 1:
                            menit_detik = int(input("Masukan Jumlah Menit yang Ingin dirubah ke Detik: "))
                            print("Hasil dari perubahan {} menit ke detik adalah {} detik" .format(menit_detik, minute_to_second(menit_detik)))
                        elif menit_menu == 2:
                            menit_jam = int(input("Masukan Jumlah Menit yang ingin dirubah ke Jam:  "))
                            print("Hasil dari perubahan {} menit ke jam adalah {} jam" .format(menit_jam, minute_to_hour(menit_jam)))
                        elif menit_menu == 3:
                            menit_valid == True
                        else:
                            print("Mohon maaf yang bisa memilih sesuai dengan menu :3")
                    elif menit_menu.strip() == "":
                        print("Mohon maaf, isian tidak boleh kosong")
                    else :
                        print("Mohon maaf hanya bisa memilih dengan Angka")

            elif perubahan_waktu == 3:
                jam_valid = False
                while not jam_valid:
                    print("Menu Perhitungan Perubahan Waktu Jam")
                    print("1. Perhitungan Jam ke Detik")
                    print("2. Perhitungan detik ke Menit")
                    print("3. Kembali ke Menu Utama ")
                    jam_menu = int(input("Masukan pilihan untuk melakukan perhitungan: "))
                    if jam_menu.isdigit():
                        jam_menu = int(jam_menu)
                        if jam_menu == 1:
                            jam_detik = int(input("Masukan Jumlah Jam yang ingin dirubah menjadi Detik: "))
                            print("Hasil perubahan dari {} jam ke detik adalah {} detik" .format(jam_detik, hour_to_second(jam_detik)))
                        elif jam_menu == 2:
                            jam_menit = int(input("Masukan Jumlah Jam yang ingin dirubah menjadi Menit: "))
                            print("Hasil perubahan dari {} jam ke menit adalah {} menit" .format(jam_menit, hour_to_second(jam_menit)))
                        elif jam_menu == 3:
                            jam_valid = True
                        else:
                            print("Mohon maaf hanya bisa memilih sesuai dengan menu :3")
                    elif jam_menu.strip() == "":
                        print("Mohon maaf isian tidak boleh kosong")
                    else:
                        print("Mohon maaf hanya bisa memasukan Angka")
            elif perubahan_waktu == 4 :
                perubahan_waktu_valid == True
            else : 
                print("Mohon maaf, hanya bisa memilih dengan pilihan yang ada")
        elif perubahan_waktu.strip() == "":
            print("Mohon maaf, wajib untuk diisi")
        else :
            print("Mohon maaf, hanya bisa menggunakan angka")    