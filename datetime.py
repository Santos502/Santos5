#Muhamad Agung Santoso
#Library datetime

#konversi tanggal dan waktu sekarang kedalam format: tanggal bulan tahun jam:menit
import datetime

konversi1 = datetime.datetime.now()
hariSekarang = konversi1.strftime('%d %B %Y %H:%M')

print(hariSekarang)
