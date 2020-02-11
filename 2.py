import random #mengambil package random
 
rand = random.randint(1,10) #membuat variabel random angka dari selisih
kes = [] #penamaan nilai awal kes
 
while len(kes)<5: 
    inputan = input ("Masukan tebakan angka dari 1 - 10: ")
    try:
        pass_number = int(inputan)
    except:
        print("Itu bukan angka. Masukan Angka!")
        break

    if pass_number < 1 or pass_number > 10:
        print ("Nomormu keluar dari clue")
        break

    kes.append(pass_number)
    if pass_number > rand:
        print("Nomormu terlalu besar. Percobaan #{}".format(len(kes)))
        continue
    elif pass_number < rand:
        print("Nomormu terlalu kecil. Percobaan #{}".format(len(kes)))
        continue
    else:
        print("{} Nomormu benar".format(pass_number))
        print("Percobaanmu {} kali".format(len(kes)))
        break

if kes == 5 :
    print("Kesempatan anda Habis & Kamu Gagal!")
