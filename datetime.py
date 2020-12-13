#Muhamad Agung Santoso
#Library datetime

#konversi tanggal dan waktu sekarang kedalam format: tanggal bulan tahun jam:menit
import datetime

konversi = datetime.datetime.now()
hariSekarang = konversi.strftime('%d %B %Y %H:%M')

print(hariSekarang)
