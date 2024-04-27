
# Konversi Satuan Waktu

# Detik
# 1. Detik ke Menit
def second_to_minute(detik) :
    return detik / 60
# 2. Detik ke Jam
def second_to_hour(detik):
    return detik / 3600

# Menit 
# 1. Menit ke detik
def minute_to_second(menit):
    return menit * 60
# 2. Menit ke Jam
def  minute_to_hour(menit):
    return menit / 60

# Jam
# 1. Jam ke Detik 
def hour_to_second(jam):
    return jam * 3600
# 2. Jam ke Menit
def  hour_to_minute(jam):
    return jam * 60



# x1 = int(input("Masukan waktu  dalam detik: "))
# x2 = int(input("Masukan waktu dalam menit: "))
# x3 = int(input("Masukan waktu dalam jam: "))

# print("\n")
# print("Waktu dalam {} detik adalah {} menit " .format(x1 , second_to_minute(x1)))
# print("Waktu dalam {} detik adalah {} jam" .format(x1, second_to_hour(x1)))
# print("\n")
# print("Waktu dalam {} menit adalah {} detik" .format(x1, minute_to_second(x2)))
# print("Waktu dalam {} menit adalah {} jam" .format(x1, minute_to_hour(x2)))
# print("\n")
# print("Waktu dalam {} jam adalah {} detik" .format(x3, hour_to_second(x3)))
# print("Waktu dalam {} jam adalah {} menit" .format(x3, hour_to_minute(x3)))
