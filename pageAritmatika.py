from operasiAritmatika import *;

# page Perhitungan Artimatika 
def page_Aritamtika() :
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