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
                centimeter_valid = False
                while not centimeter_valid :
                    print("Menu Perhitungan Perubahan Jarak Centimeter (CM)")
                    print("1. Centimeter ke Meter")
                    print("2. Centimeter ke Kilomter")
                    print("3. Centimeter ke Mil")
                    print("4. Kembali ")
                    centimeter_menu = input("Masukan pilihan untuk melakukan perhitungan: ")
                    if centimeter_menu.isdigit() :
                        centimeter_menu = int(centimeter_menu)
                        if centimeter_menu==1:
                            centimeter_meter = float(input("Masukan Panjang Centimeter untuk dirubah ke Meter: "))
                            print("Hasil perhitungan dari {} cm ke meter adalah {} m" .format(centimeter_meter, centimeter_ke_meter(centimeter_meter)))
                        elif centimeter_menu == 2:
                            centimeter_kilometer = float(input("Masukan Panjang Centimeter untuk dirubah ke Kilometer: "))
                            print("Hasil perhitungan dari {} cm ke kilometer adalah {} km" .format(centimeter_kilometer, centimeter_ke_meter(centimeter_kilometer)))
                        elif centimeter_menu == 3:
                            centimeter_mil = float(input("Masukan Panjang Centimeter untuk dirubah ke Mil:  "))
                            print("Hasil perhitungan dari {} cm ke mil adalah {} mil" .format(centimeter_mil, centimeter_ke_mil(centimeter_mil)))
                        elif centimeter_menu == 4:
                            centimeter_valid == True                            
                        else:
                            print("Mohon maaf hanya bisa memilih sesuai dengan menu")
            elif perubahan_jarak == 2:
                meter_valid = False
                while not meter_valid :
                    print("Menu Perhitungan Perubahan Jarak Meter (M)")
                    print("1. Meter ke Centimeter")
                    print("2. Meter ke Kilomter")
                    print("3. Meter ke Mil")
                    print("4. Kembali ")
                    meter_menu = input("Masukan pilihan untuk melakukan perhitungan: ")
                    if meter_menu.isdigit():
                        meter_menu = int(meter_menu)
                        if meter_menu == 1:
                            meter_cm = float(input("Masukan Panjang Meter untuk dirubah ke Centimeter: "))
                            print("Hasil perhitungan dari {} m ke Centimeter adalah {} cm" .format(meter_cm, meter_ke_centimeter(meter_cm)))
                        elif meter_menu == 2:
                            meter_km = float(input("Masukan Panjang Meter untuk dirubah ke Kilometer: "))
                            print("Hasil perhitungan dari {} m ke Kilometer adalah {} km" .format(meter_km, meter_ke_kilometer(meter_km)))
                        elif meter_menu == 3:
                            meter_mil = float(input("Masukan Panjang Meter untuk dirubah ke Mil: "))
                            print("Hasil perhitungan dari {} m ke Mil adalah {} Mil" .format(meter_mil, meter_ke_mil(meter_mil)))
                        elif meter_menu == 4:
                            meter_valid = True 
                        else :
                            print("Mohon maaf hanya bisa memilih sesuai dengan menu")
                    elif meter_menu.strip() == "":
                        print("Mohon maaf isian tidak boleh kosong")
                    else:
                        print("Mohon maaf hanya bisa mengisi dengan Angka")
            elif perubahan_jarak == 3:
                kilometer_valid = False
                while not kilometer_valid :
                    print("Menu Perhitungan Perubahan Jarak Kilometer (KM)")
                    print("1. Kilometer ke Centimeter")
                    print("2. Kilometer ke Meter")
                    print("3. Kilometer ke Mil")
                    print("4. Kembali ke Menu Utama")
                    kilometer_menu = input("Masukan pilihan untuk melakukan perhitungan: ")
                    if kilometer_menu.isdigit():
                        kilometer_menu = int(kilometer_menu)
                        if kilometer_menu == 1:
                            kilometer_cm = float(input("Masukan Panjang Kilometer untuk dirubah ke Centimeter: "))
                            print("Hasil perhitungan dari {}km ke Centimeter adalah {}cm" .format(kilometer_cm, kilometer_ke_centimeter(kilometer_cm)))
                        elif kilometer_menu == 2:
                            kilometer_m = float(input("Masukan Panjang Kilometer untuk dirubah ke Meter: "))
                            print("Hasil perhitungan dari {}km ke Meter adalah {}meter " .format(kilometer_m, kilometer_ke_meter(kilometer_m)))
                        elif kilometer_menu == 3 :
                            kilometer_mil = float(input("Masukan Panjang Kilometer untuk dirubah ke Centimeter: "))
                            print("Hasil perhitungan dari {}km ke Mil adalah {}mil " .format(kilometer_mil, kilometer_ke_mil(kilometer_mil)))
                        elif kilometer_menu == 4 :
                            kilometer_valid = True
                        else:
                            print("Mohon maaf hanya bisa memilih sesuai dengan menu")
                    elif kilometer_menu.strip() == "":
                        print("Mohon maaf isian tidak boleh kosong")
                    else:
                        print("Mohon maaf hanya bisa mengisi dengan Angka")
            elif perubahan_jarak == 4:
                mil_valid = False 
                while not mil_valid:
                    print("Menu Perhitungan Perubahan Jarak Mil ")
                    print("1. Mil ke Centimeter")
                    print("2. Mil ke Meter")
                    print("3. Mil ke Kilometer")
                    print("4. Kembali ke Menu Utama")
                    mil_menu = input("Masukan pilihan untuk melakukan perhitungan: ")
                    if mil_menu.isdigit():
                        mil_menu = int(kilometer_menu)
                        if mil_menu == 1:
                            mil_cm = float(input("Masukan Panjang Mil untuk dirubah ke Centimeter: "))
                            print("Hasil perhitungan dari {}mil ke Centimeter adalah {}cm " .format(mil_cm, mil_ke_centimeter(mil_cm)))
                        elif mil_menu == 2:
                            mil_m = float(input("Masukan Panjang Mil untuk dirubah ke Meter: "))
                            print("Hasil perhitungan dari {}mil ke Meter adalah {}m " .format(mil_m, mil_ke_meter(mil_m)))
                        elif mil_menu == 3 :
                            mil_km = float(input("Masukan Panjang Mil untuk dirubah ke Kilometer: "))
                            print("Hasil perhitungan dari {}Mil ke kilometer adalah {}km " .format(mil_km, mil_ke_kilometer(mil_km)))
                        elif mil_menu == 4 :
                            mil_valid = True
                        else:
                            print("Mohon maaf hanya bisa memilih sesuai dengan menu")
                    elif kilometer_menu.strip() == "":
                        print("Mohon maaf isian tidak boleh kosong")
                    else:
                        print("Mohon maaf hanya bisa mengisi dengan Angka")
            elif perubahan_jarak == 5:
                perubahan_jarak_valid = True
            else:
                print("Mohon maaf, hanya bisa memilih dengan pilihan yang ada")
        elif perubahan_jarak.strip() == "":
            print("Mohon maaf, wajib untuk diisi")
        else:
            print("Mohon maaf, hanya bisa menggunakan angka")    