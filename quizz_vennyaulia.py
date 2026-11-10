print("===================================")
print("     PROGRAM UJIAN MATEMATIKA")
print("===================================")

# Input nama mahasiswa
nama = input("Masukkan nama mahasiswa: ")

# Menentukan target nilai
if nama == "Andi":
    target = 70
elif nama == "Budi":
    target = 75
elif nama == "Citra":
    target = 80
else:
    print("Nama mahasiswa tidak terdaftar.")
    exit()

print("Nama mahasiswa :", nama)
print("Target nilai   :", target)
print("-----------------------------------")

# Proses ujian
percobaan = 0
lulus = False

while percobaan < 3 and lulus == False:
    percobaan += 1

    nilai = int(input(f"Masukkan nilai ujian ke-{percobaan}: "))

    if nilai >= target:
        lulus = True
        print("Selamat,", nama, "berhasil lulus!")
    else:
        print("Nilai belum mencapai target.")

print("-----------------------------------")

# Menampilkan hasil akhir
if lulus:
    print(nama, "berhasil lulus setelah", percobaan, "kali percobaan.")
else:
    print(nama, "dinyatakan tidak lulus setelah 3 kali percobaan.")

print("===================================")
print("          PROGRAM SELESAI")
print("===================================")
