#Buat program Python yang mengambil status persiapan proyek dan menentukan apakah proyek 
#tersebut dapat diluncurkan. jika status  persiapan "Siap", program harus mencetak "Proyek 
#diluncurkan". Jika status  persiapan "Tunda", program harus mencetak "Proyek ditunda"

status_persiapan_proyek = str(input("Masukkan status persiapan proyek(Siap/Tunda) "))

if status_persiapan_proyek.lower() == "siap":
    mencetak = "Proyek diluncurkan"
elif status_persiapan_proyek.lower() == "tunda":
    mencetak = "proyek ditunda"

print ("statusnya", mencetak)