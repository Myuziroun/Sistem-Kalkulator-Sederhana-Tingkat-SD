import math
# Rumus Bangun Datar

# Rumus Keliling Bangun Datar
# 1. Keliling Persegi
def k_persegi(sisi):
    return 4 * sisi
# 2. Keliling Persegi Panjang
def k_persegiPanjang(panjang, lebar):
    return 2*(panjang + lebar)
# 3. Keliling Jajar Genjang
def k_jarjarGenjang(a,b,c,d):
    return a + b + c + d
# 4. Keliling Belah Ketupat
def k_belahKetupat(a,b,c,d) :
    return a + b + c + d
# 5. Keliling Segitiga
def k_segitiga(a,b,c) :
    return a + b + c
# 6. Keliling Layang - Layang
def k_layang_layang(a,b,c,d) :
    return a + b + c + d
# 7. Keliling Trapesium
def k_trapesium(a,b,c,d) :
    return a + b + c + d
# 8. Keliling lingkaran
def k_lingkaran(r) :
    return 2*math.pi*r
        
# Rumus Luas Bangun Datar

# 1. Luas Persegi
def L_Persegi(sisi) :
    return sisi * sisi
# 2. Luas Persegi Panjang
def L_persegiPanjang(panjang, lebar):
    return panjang * lebar
# 3. Luas Jajar Genjang
def L_jajarGenjang(alas, tinggi):
    return alas * tinggi
# 4. Luas Belah Ketupat
def L_belahKetupat(diagonal1, diagonal2):
    return 1/2 * diagonal1 * diagonal2
# 5. Luas Layang - layang
def L_layang_layang(diagonal1,diagonal2):
    return 1/2 * diagonal1 * diagonal2
# 6. Luas Trapesium
def L_trapesium(a,b,tinggi):
    return (a+b)/2 * tinggi
# 7. Luas Segitiga
def L_Segitiga(alas, tinggi) :
    return 1/2 * alas * tinggi
# 8. Luas Lingkaran
def L_lingkaran(r):
    return math.pi * r * r


# Rumus Bangun Ruang

# Rumus Luas Bangun Ruang

# 1. Luas Kubus
def  L_kubus(rusuk) :
    return 6 * (rusuk ** 2)
# 2. Luas Balok
def L_balok(panjang, lebar, tinggi) :
    return (2 * panjang * lebar) + (2 * panjang * tinggi) + (2 * lebar * tinggi)
# 3. Luas Limas Segi Empat
def L_limas_SegiEmpat(sisi,tinggi) :
    return L_Persegi(sisi) + (4 *(L_Segitiga(sisi,tinggi)))
# 4.  Luas Prisma Segitiga
def L_prisma(sisi1,tinggi, Tinggi, sisi2,sisi3,alas) :
    return ((sisi1 + sisi2 + sisi3) * Tinggi) , ((sisi1 + sisi2 + sisi3) * Tinggi +(alas * tinggi))
# 5. Luas Limas Segitiga
def L_limas_Segi_tiga(sisi,tinggi) :
    return  (4 * L_Segitiga(sisi,tinggi))
# 6. Luas Selinder (Tabung)
def L_selinder(jari, tinggi) :
    luasSelimut = 2 * math.pi * jari * tinggi
    luasPermukaan = luasSelimut + ( 2 * math.pi * jari**2)
    return luasSelimut, luasPermukaan
# 7.  Luas Kerucut
def L_kerucut(sisi, jari, tinggi) :
    luasSelimut = 2 * math.pi * sisi
    luasPermukaan = luasSelimut + (math.pi * jari**2)
    return luasSelimut, luasPermukaan
# 8. Luas Bola
def L_bola(jari) :
    return 4 * math.pi * jari **2

# Rumus Volume Bangun Ruang

# 1. Volume Kubus
def V_kubus(rusuk):
    return rusuk ** 3
# 2. Volume Balok
def V_balok(panjang,lebar,tinggi):
    return L_persegiPanjang(panjang,lebar) * tinggi 
# 3. Volume Limas Segiempat
def V_limas_segiempat(sisi,tinggi):
    return 1/3 * L_Persegi(sisi) * tinggi
# 4. Volume Prisma Segitiga 
def V_prisma_Segitiga(alas,tinggi,Tinggi):
    return L_Segitiga(alas,tinggi) * Tinggi
# 5. Volume Limas Segitiga 
def V_limas_Segi_tiga(alas,tinggi,Tinggi):
    return 1/3 * (L_Segitiga(alas,tinggi)) * Tinggi
# 6. Volume Tabung
def V_tabung(jari, tinggi) :
    return math.pi * jari**2 * tinggi
# 7. Volume Kerucut
def V_kerucut(jari, tinggi) :
    return 1/3 * math.pi * jari**2 * tinggi
# 8. Volume Bola
def V_bola(jari) :
    return 4/3 * math.pi * jari**3


# sisi = int(input("masukan nilai sisi : "))
# tinggi = int(input("Masukan nilai tinggi : "))

# print("Luas permukaan dari limas segi empat adalah {}" .format(L_limasEmpat(sisi,tinggi)))

