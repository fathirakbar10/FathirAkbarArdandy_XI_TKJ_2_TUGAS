#NAMA = FATHIR AKBAR ARDANDY 
#KELAS = XI-TKJ 2
#NO. = 10

#Deskripsi pekerjaan = seorang pelari ingin 
#meningkatkan jarak  tempuhnya setiap minggunya. 
#ia mulai
#dengan 5 kilometer dan meningkatkan jaraknya 
#sebesar 10% setiap mingggunya. Buatlah program 
#yang menghtung berapa minggu yang dibutuhkan agar pelari itu dapat berlari lebih dari 10
#kilometer 

jarak_awal = 5 
target_jarak = 10 
kenaikan_mingguan = 0.10  

minggu = 0  # 

while jarak_awal < target_jarak:
    jarak_awal += jarak_awal * kenaikan_mingguan  
    minggu += 1  

print(f'Dibutuhkan {minggu} minggu untuk pelari mencapai lebih dari {target_jarak} kilometer.')
    