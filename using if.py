#Input 5 int
#max
#min
#average
#jml bulat
#jml ganjil
#yg ber nilai nol
#rage nilai

a = int(input("Masukan angka ke-1 : "))
b = int(input("Masukan angka ke-2 : "))
c = int(input("Masukan angka ke-3 : "))
d = int(input("Masukan angka ke-4 : "))
e = int(input("Masukan angka ke-5 : "))

tot = a+b+c+d+e


#MENCARI NILAI MINIMUM
maks = a
if a > maks:
    maks = a
if b > maks:
    maks = b
if c > maks:
    maks = c
if d > maks:
    maks = d
if e > maks:
    maks = e


#MENCARI NILAI MINIMUM
mins = a
if a < mins:
    mins = a
if b < mins:
    mins = b
if c < mins:
    mins = c
if d < mins:
    mins = d
if e < mins:
    mins = e


#MENCARI RATA-RATA
avg = tot/5


#MENCARI BILANGAN GANJJIL DAN GENAP
if a%2 == 1:
    ganjil1 = 1
    genap1 = 0
else:
    ganjil1 = 0
    genap1 = 1
if b%2 == 1:
    ganjil2 = 1
    genap2 = 0
else:
    ganjil2 = 0
    genap2 = 1
if c%2 == 1:
    ganjil3 = 1
    genap3 = 0
else:
    ganjil3 = 0
    genap3 = 1
if d%2 == 1:
    ganjil4 = 1
    genap4 = 0
else:
    ganjil4 = 0
    genap4 = 1
if e%2 == 1:
    ganjil5 = 1
    genap5 = 0
else:
    ganjil5 = 0
    genap5 = 1
ganjil = ganjil1 + ganjil2 + ganjil3 + ganjil4 + ganjil5
genap = genap1 + genap2 + genap3 + genap4 + genap5 
# x = max(a,b,c,d,e)
# n = min(a,b,c,d,e)


#MENCARI BILANGAN YANG BERNILAI 0
if a == 0:
    nol1 = 1
else:
    nol1 = 0
if b == 0:
    nol2 = 1
else:
    nol2 = 0
if c == 0:
    nol3 = 1
else:
    nol3 = 0
if d == 0:
    nol4 = 1
else:
    nol4 = 0
if e == 0:
    nol5 = 1
else:
    nol5 = 0
nol = nol1 + nol2 + nol3 + nol4 + nol5


#MENCARI JARAK BILANGAN
ranges = maks - mins


print("\nNilai Maksimum: ", maks)
print("Nilai Minimum: ", mins)
print("Rata-rata: ", avg)
print("Jumlah Bilangan Genap: ", genap)
print("Jumlah Bilangan Ganjil: ", ganjil)
print("Jumlah Bilangan Nol ada: ", nol)
print("Range nilai: ", ranges)
