#Deskripsi pekerjaan: Sebagai seorang manajer proyek, Anda harus menentukan apakah suatu proyek akan selesai tepat waktu atau terlambat 

#Soal : Buat program python yang mengambil estimasi waktu selesai proyek  dan tanggal target selesai. 
# Jika estimasi waktu selesai lebih awal atau sama dengan target, 
# program harus mencetak "Tepat waktu" jika tidak, program harus mencetak "Terlambat".

#jawaban 
tanggal_estimasi_selesai = input("tanggal waktu selesai: ")
tanggal_estimasi_target = input("tanggal waktu target: ")

if tanggal_estimasi_selesai <= tanggal_estimasi_target:
    print("Tepat waktu")
else:
    print("Terlambat")