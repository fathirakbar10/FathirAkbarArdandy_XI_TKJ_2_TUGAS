#Buat program Python yang mengambil informasi pembaruann perangkat lunak dan menentukan
#apakah sistem perlu di-restart. Jika pembaruan mengharuskan restart, reset program harus mencetak 
#"Sistem perlu di-restart". Jika tidak, programm harus mencetak "Sistem tidak perlu direstart"

informasi_pembaruan_perangkat_lunak = str(input("Masukkan informasi pembaruan perangkat lunak (perlu/tidak): "))

if informasi_pembaruan_perangkat_lunak.lower() == "perlu":
    mencetak = "Sistem perlu di-restart"
elif informasi_pembaruan_perangkat_lunak.lower() == "tidak":
    mencetak = "Sistem tidak  perlu  di-restart"

print("Sistem mengatakan", mencetak)