#PROGRAM KONVERSI DESIMAL KE OCTAL

print("Selamat Datang di Bunker Hacker!")

#Meminta input banyak konversi yang diinginkan user
banyak_konversi = int(input("\nMasukkan berapa kali konversi ingin dilakukan : "))

#Proses meminta input angka desimal dari user dan mengkonversikannya ke octal
for i in range(1, banyak_konversi + 1):
    angka_decimal = int(input(f"\nMasukkan angka ke-{i} yang ingin dikonversikan (dalam desimal) : "))

    #Theorema untuk mengkonversi desimal ke octal(yang masih terbalik)
    hasil_bagi = angka_decimal // 8
    sisa_bagi  = angka_decimal % 8
    angka_octal_terbalik = str(sisa_bagi)

    while hasil_bagi > 0 :
        hasil_bagi,sisa_bagi = hasil_bagi // 8 , hasil_bagi % 8
        angka_octal_terbalik += str(sisa_bagi)

    #Membalikkan octal yang terbalik ke bentuk octal yang sebenarnya
    angka_octal = angka_octal_terbalik[::-1]
    print(f"Hasil konversi desimal ke basis 8 : {angka_octal}")

print("\nTerima kasih telah menggunakan Bunker Hacker!")