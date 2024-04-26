# Rumus keliling Bangun Datar
import math

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


# Rumus Volume Bangun Ruang
