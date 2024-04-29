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