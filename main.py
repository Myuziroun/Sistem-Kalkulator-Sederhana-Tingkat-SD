from operasiAritmatika import penjumlahan, pengurangan, pembagian, perkalian;
from rumusBangunDatarRuang import *;
from satuanJarak import centimeter_ke_kilomter, centimeter_ke_meter, centimeter_ke_mil, meter_ke_centimeter, meter_ke_kilometer, meter_ke_mil, mil_ke_centimeter, mil_ke_kilometer, mil_ke_meter, kilometer_ke_centimeter, kilometer_ke_meter, kilometer_ke_mil;
from satuanWaktu import second_to_minute, second_to_hour,  minute_to_hour, minute_to_second, hour_to_minute, hour_to_second;


while True:
    print("Menu Utama")
    print("1. Perhitungan Aritmatika (+, -, /, *) ")
    print("2. Perhitungan Bangun Datar ")
    print("3. Perhitungan Bangun Ruang ")
    print("4. Perhitungan Perubahan Waktu ")
    print("5. Perhitungan Perubahan Jarak ")
    choice = input("Masukan pilihan untuk melakukan perhitungan: ")
    if choice.isdigit() :
        choice = int(choice)
        
    elif choice.strip() == "":
        print("Mohon maaf, wajib untuk diisi")
    else:
        print("Mohon maaf hanya bisa menggunakan angka")
