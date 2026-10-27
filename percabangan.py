# variabel dan tipe data 

nama_mhs = input("Masukkan Nama :")
nilai_algoritma = int(input("Masukkan Nilai :"))
nilai_basisdata = int(input("Masukkan Nilai :"))
nilai_logika_informatika = int(input("Masukkan Nilai :"))
nilai_agama = int(input("Masukkan Nilai :"))
nilai_bahasa_indonesia = int(input("Masukkan Nilai :"))
nilai_bahasa_inggris = int(input("Masukkan Nilai :"))
nilai_pancasila = int(input("Masukkan Nilai :"))

rata_rata = (nilai_algoritma + nilai_basisdata + nilai_logika_informatika + nilai_agama + nilai_bahasa_indonesia + nilai_bahasa_inggris + nilai_pancasila) / 7
print(rata_rata)

# penentuan lulus atau tidak 
if rata_rata >=80 and rata_rata <=100:
    # kondisi jika terpenuhi
    # maka
    print("Nilai : A")
elif rata_rata >=70 and rata_rata <=80:
    print("Nilai : B")
elif rata_rata >=50 and rata_rata <=70:
    print("Nilai : C")
elif rata_rata >=30 and rata_rata <=50:
    print("Nilai : D")
elif rata_rata >=10 and rata_rata <=30:
    print("Nilai : E")
else:
    # cukup menampilkan hasil
    # maka
    print("Nilai Lebih dari 100 atau dibawah 50")