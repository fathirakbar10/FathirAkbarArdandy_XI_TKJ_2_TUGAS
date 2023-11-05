#nama = FATHIR AKBAR ARDANDY  
#kelas =  XI-TKJ 2
#no = 10

# Deskripsi Pekerjaan: Buatlah sebuah fungsi untuk menghitung jumlah digit dari suatu bilangan.

def hitung_jumlah_digit(n):
    total = 0
    for digit in str(n):
        if digit.isdigit():
            total += int(digit)
    return total

bilangan = input("Masukkan bilangan: ")

hasil_jumlah_digit = hitung_jumlah_digit(bilangan)
print(f"Jumlah digit dari {bilangan} adalah {hasil_jumlah_digit}.")

