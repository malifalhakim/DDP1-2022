print("Selamat datang di Pacil Mart!")

#meminta input file txt
nama_file = input("\nMasukkan nama file input : ")

#Mengakses file txt
try :
    file = open(nama_file,"r")

    #Mencek apakah file txt kosong atau bukan
    if file.read() == '' :
        print("\nFile input ada tapi isinya kosong")
    else:
        file = open(nama_file,"r")
        #Membuat tabel data belanjaan
        print("\nBerikut adalah daftar belanjaanmu:")
        print(f"\nNama Barang |  Jumlah| Kembalian")
        print(f"--------------------------------")
        for line in file:
            parts = line.split()
            nama_barang = parts[0]
            uang_dipunya = int(parts[1])
            harga_satuan = int(parts[2])
            jumlah_barang = uang_dipunya // harga_satuan
            kembalian = uang_dipunya - (jumlah_barang * harga_satuan)
            print(f"{nama_barang:<12}|{jumlah_barang:>8}|{kembalian:>10}")

        print("\nTerima kasih sudah belanja di Pacil Mart!")
        
        file.close()
    
    file.close()

#Mengatasi file yang tidak ada
except FileNotFoundError:
    print("\nFile tidak tersedia")

