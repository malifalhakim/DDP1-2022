import math

def is_balok(nama_bangun_ruang):
    """Memvalidasi input apakah memasukkan BALOK atau tidak"""
    return nama_bangun_ruang == 'BALOK'

def is_kerucut(nama_bangun_ruang):
    """Memvalidasi input apakah memasukkan KERUCUT atau tidak"""
    return nama_bangun_ruang == 'KERUCUT'

def is_stop(nama_bangun_ruang):
    """Memvalidasi input apakah memasukkan STOP atau tidak"""
    return nama_bangun_ruang == 'STOP'

def volume_balok(panjang,lebar,tinggi):
    """Menghitung volume balok"""
    return panjang * lebar * tinggi

def volume_kerucut(jari_jari,tinggi):
    """Menghitung volume kerucut"""
    return (math.pi * (jari_jari * jari_jari) * tinggi)/3

def harga_bayar(volume,rupiah_per_volume):
    """Menghitung harga yang harus dibayar per satuan volumenya"""
    return volume * rupiah_per_volume

#PROGRAM UTAMA
if __name__ == "__main__":
    print("\nSelamat datang di Depot Minuman Dek Depe!")
    print("=========================================")

    input_selesai = False
    total_volume  = 0
    #Proses memasukkan input data yang dibutuhkan dan menghitung volume
    while not input_selesai:
        bentuk_galon = input("\nMasukkan bentuk galon yang diinginkan (STOP untuk berhenti) : ")

        if is_balok(bentuk_galon):
            panjang = float(input("Masukkan panjang balok : "))
            lebar   = float(input("Masukkan lebar   balok : "))
            tinggi  = float(input("Masukkan tinggi  balok : "))

            total_volume += volume_balok(panjang,lebar,tinggi)
        elif is_kerucut(bentuk_galon):
            jari_jari = float(input("Masukkan jari-jari kerucut : "))
            tinggi    = float(input("Masukkan tinggi kerucut    : "))

            total_volume += volume_kerucut(jari_jari,tinggi)
        elif is_stop(bentuk_galon):
            input_selesai = True
        else :
            print("Input tidak benar, masukkan kembali")
    #Menampilkan Output
    print("\n====================================================")
    if total_volume > 0 :
        print(f"Total volume air yang dikeluarkan : {total_volume:.2f}")
        print(f"Total harga yang harus dibayar    : Rp{harga_bayar(total_volume,700):.2f}")
        print("====================================================")
        print("Terimakasih telah menggunakan Depot Air Minum Dek Depe!\n")
    else :
        print("Anda tidak memasukkan input satupun :(")
        print('Terimakasih telah menggunakan Depot Air Minum Dek Depe!')
        print("====================================================\n")