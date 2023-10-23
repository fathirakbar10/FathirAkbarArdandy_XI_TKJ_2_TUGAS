#Buat program Python yang mengambil durasi peminjaman buku dalam hari dan menentukan jenis
#pinjaman berdasarkan aturan berikut:
#- peminjaman 7 hari atau kurang: "Peminjaman pendek"
#- peminjaman lebih dari 7 hari hingga 30  hari:  "Peminjaman menengah"
#- peminjaman lebih dari 30 hari: "peminjaman panjang"

durasi_peminjaman_buku =  int(input("berapa hari meminjaman buku "))

if durasi_peminjaman_buku < 7:
    jenis_peminjaman = "Peminjaman pendek"
elif durasi_peminjaman_buku > 7 and durasi_peminjaman_buku < 30:
    jenis_peminjaman = "Peminjaman menengah"
elif durasi_peminjaman_buku > 30:
    jenis_peminjaman = "Peminjaman panjang"

print("JENIS PEMINJAMAN =", jenis_peminjaman)