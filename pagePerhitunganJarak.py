from satuanJarak import *;

def page_perubahan_jarak() :
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