print("Selamat datang ke Dek Depe Holiday Tracker!")

#Input Banyak Tempat Wisata yang dikunjungi dan cek validasinya

valid = False

while not valid :
    banyak_wisata = int(input("\nMasukkan banyak tempat wisata yang kamu kunjungi : "))

    if banyak_wisata <= 0 :
        print("Input tidak valid. Silahkan masukkan input kembali!")
    else :
        valid = True


#Input Data Pengalaman Perjalanan

rating_perjalanan_terbaik = 0
jumlah_rating = 0

for i in range(1,banyak_wisata + 1) :
    tempat_perjalanan = input(f"\nPerjalanan {i}: ")
    rating_perjalanan = int(input(f"Rating perjalanan kamu ke {tempat_perjalanan} (indeks 1 - 10) : "))
    
    jumlah_rating += rating_perjalanan

    if rating_perjalanan >= rating_perjalanan_terbaik :
        rating_perjalanan_terbaik = rating_perjalanan
        perjalanan_mengesankan = tempat_perjalanan


rata_rata_rating = jumlah_rating / banyak_wisata 

#Ringkasan Data Pengalaman Liburan

print("\n---Summary---")
print(f"Perjalanan paling mengesankan adalah ketika pergi ke {perjalanan_mengesankan}")
print(f"Skala kebahagiaan Dek Depe adalah {rata_rata_rating:.2f}")
if rata_rata_rating >= 8:
    print(f"Dek Depe bahagia karena pengalamannya menyenangkan")
elif rata_rata_rating >= 5 :
    print(f"Dek Depe senang karena pengalamannya cukup baik")
else :
    print(f"Dek Depe sedih karena pengalamannya buruk")

print("\nTerimakasih telah menggunakan Dek Depe Holiday Tracker!")

