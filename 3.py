import random
angka = random.randint(24, 65)
print("Tebak angka 24 sampai 65")

Tebak = 0

while Tebak != angka :
    Tebak = eval(input("Masukan tebakanmu :"))

    if Tebak == angka:
        print("Betul!, angkanya", angka)
        n = 23
        while n < angka:
            n += 1
            print(n, end=' ')
    elif Tebak > angka:
        print("Angkanya Terlalu tinggi")
    else:
        print("Angkanya Terlalu rendah")
