import math

#Input User
nama = input("Nama : ")

panjang_persegi   = float(input("Panjang persegi nametag (cm)   : "))
panjang_trapesium = float(input("Panjang trapesium nametag (cm) : "))

banyak_name_tag = int(input("Banyak Nametag : "))

#Luas Per Bagian

jari_jari = panjang_persegi / 2
luas_lingkaran = math.pi * (jari_jari * jari_jari)
luas_setengah_lingkaran = luas_lingkaran / 2

luas_persegi = panjang_persegi * panjang_persegi

luas_segitiga = (panjang_persegi * panjang_persegi ) / 2

luas_trapesium = ((panjang_persegi + panjang_trapesium) * panjang_persegi ) / 2


#Luas Total
luas_satu_nametag  = luas_setengah_lingkaran + luas_persegi + luas_segitiga + luas_trapesium
luas_total_nametag = banyak_name_tag * luas_satu_nametag

#Harga 
harga_kertas_per_cm_kuadrat = 0.40
uang_diperlukan = luas_total_nametag * harga_kertas_per_cm_kuadrat
uang_diperlukan = math.ceil(uang_diperlukan / 1000) * 1000

#Output

print(f"\nHalo, {nama}! Berikut informasi terkait nametag kamu:\n")

print(f'Luas 1 nametag      : {luas_satu_nametag:.2f} cm^2')
print(f"Luas total nametag  : {luas_total_nametag:.2f} cm^2")
print(f"Uang yang diperlukan: Rp{uang_diperlukan}")


