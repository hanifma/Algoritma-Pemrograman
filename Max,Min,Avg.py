#Input 5 int
#max
#min
#average

a = int(input("Masukan angka ke-1 : "))
b = int(input("Masukan angka ke-2 : "))
c = int(input("Masukan angka ke-3 : "))
d = int(input("Masukan angka ke-4 : "))
e = int(input("Masukan angka ke-5 : "))

x = max(a,b,c,d,e)
n = min(a,b,c,d,e)
avg = (a+b+c+d+e)/5

print("\n Nilai Maksimum: ", x)
print("Nilai Minimum: ", n)
print("Rata-rata: ", avg)
