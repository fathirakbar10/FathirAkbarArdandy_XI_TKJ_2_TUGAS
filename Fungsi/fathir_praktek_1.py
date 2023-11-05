#nama = FATHIR AKBAR ARDANDY  
#kelas =  XI-TKJ 2
#no = 10

#Deskripsi Pekerjaan: Buatlah sebuah fungsi yang menghitung total dari deret bilangan ganjil hingga
#batas tertentu yang ditentukan pengguna.

def total_deret_ganjil(batas):
    total = 0
    for i in range(1, batas + 1, 2):
        total += i
    return total

batas = int(input("Masukkan batas: "))
hasil = total_deret_ganjil(batas)
print(f"Total deret bilangan ganjil hingga batas {batas} adalah {hasil}.")
