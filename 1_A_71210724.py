print("====== Program Manipulasi String ======")
print('Pilihan Menu :')
print("1. Hitung Kata")
print("2. Ubah Kata")

pilihan = input("Pilihan anda :")

def hitungkata():
    hitung = kalimat.replace(diubah,diganti)
    return hitung

def ubahkata():
    ubah = kalimat.count(menghitung)
    return ubah

if pilihan == "1":
    kalimat = input("Masukkan sebuah kalimat/kata : ")
    menghitung = input("Masukan kata yang ingin dihitung : ")
    print("Terdapat sebanyak", ubahkata(), "kata", menghitung, "di dalam kalimat")
elif pilihan == "2":
    kalimat = input("Masukkan sebuah kalimat/kata : ")
    diubah = input("Masukan kata yang ingin di ubah : ")
    diganti = input("masukkan kata pengganti : ")
    print("String berhasil diubah menjadi :", hitungkata())