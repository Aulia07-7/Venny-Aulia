
#input
nilai_tugas = int(input("masukkan nilai:"))
nilai_UTS = int(input("masukkan nilai:"))
nilai_UAS = int(input("masukkan nilai:"))
nilai_kehadiran = int(input("masukkan nilai:"))
#
print("========aritmatika=======")
nilai_akhir = (0.20 * nilai_tugas) + (0.30 * nilai_UTS) + (0.50 * nilai_UAS)
print("Nilai Akhir", nilai_akhir)
#
print("========logika========") 
# syarat predikat
memiliki_predikat_minimum = nilai_akhir > 85
# syarat lulus
memiliki_lulus_minimum = nilai_akhir > 75
memiliki_hadir_cukup = nilai_kehadiran > 80
# syarat belum lulus
memiliki_nilai_kurang = nilai_akhir < 75
hasil_and = memiliki_predikat_minimum and memiliki_lulus_minimum and memiliki_hadir_cukup
hasil_or = memiliki_predikat_minimum or memiliki_lulus_minimum or memiliki_hadir_cukup
is_lulus = memiliki_lulus_minimum and memiliki_hadir_cukup
hasil_not = not is_lulus
print("Hasil:", hasil_and)
print("Hasil or:", hasil_or)
print("Hasil not:", hasil_not)
syarat_predikat = (nilai_akhir > 85) and (nilai_kehadiran > 90) and (nilai_akhir % 2 == 0)
syarat_lulus = (nilai_akhir > 75) and (nilai_kehadiran > 80)
if syarat_predikat:
    status = "Lulus dengan predikat"
elif syarat_lulus:
    status = "Lulus"
else:
    status = "Belum Lulus"
#
print("========ekspresi========")
print("ekspresi 1:", memiliki_predikat_minimum and memiliki_hadir_cukup)
print("ekspresi 2:", memiliki_lulus_minimum or memiliki_nilai_kurang)
print("ekspresi 3:", nilai_kehadiran >= 80 and nilai_akhir > 75)
# output hasil
print("Nilai Akhir :", nilai_akhir)
print("Status :", status)


    
      