from time import sleep #mengambil package time fungsi sleep
countDown = int(input("Masukan Waktu Hitung Mundur: ")) #menamai variabel dan mengambil inputan
while (countDown >= 0): #perulangan ketika variabel lebih dari sama dengan nol
    if countDown != 0: #jika variabel tidak sama dengan nol
        print(countDown) #akan mencetak variabel
        countDown = countDown - 1 #variabel yang dicetak akan dikurangi 1
        sleep(1) #selisih waktu  dalam detik
    else: #jika kondisi diatas tidak sesuai 
        print("Duarrr Nmax!") #print Duar Nmax
        break #untuk memcah/menghentikan loop
