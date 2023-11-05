#nama = FATHIR AKBAR ARDANDY  
#kelas =  XI-TKJ 2
#no = 10

#Deskripsi Pekerjaan: Buatlah sebuah fungsi yang menghitung bilangan Fibonacci ke-n.

def fibonacci(n):
    if n <= 0:
        return "Bilangan Fibonacci hanya terdefinisi untuk n >= 1"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Masukkan nilai n: "))

if n <= 0:
    print("Bilangan Fibonacci hanya terdefinisi untuk n >= 1")
else:
    hasil = fibonacci(n)
    print(f"Bilangan Fibonacci ke-{n} adalah {hasil}.")
