#Soal 5:
#Deskripsi Pekerjaan: Sebagai seorang guru, Anda harus menentukan nilai akhir siswa berdasarkan
#nilai tugas dan ujian.
#Soal:
#Buat program Python yang mengambil nilai tugas (skala 0-100) dan nilai ujian (skala 0-100) seorang
#siswa dan menentukan nilai akhirnya. Jika nilai tugas lebih dari 70 dan nilai ujian lebih dari 60, siswa
#lulus dengan nilai "Lulus". Jika tidak, siswa gagal dengan nilai "Gagal".

nilai_tugas = float(input("Masukkan nilai tugas(skala=0-100): "))
nilai_ujian = float(input("Masukkan nilai ujian(skala=0-100): "))

if nilai_tugas > 70 and nilai_ujian > 60:
    keterangan = "Lulus"
else:
    keterangan = "Gagal"

print("Anda ", keterangan)