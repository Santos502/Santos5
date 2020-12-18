#Muhamad Agung Santoso

#memperbaiki program sederhana

print('\n Kalkulator Suhu \n')

print('''1. Celcius ke Reamur
2. Celcius ke Fahrenheit
3. Celcius ke Kelvin''')

def kembali():
    print('apakah anda ingin lanjut? y|t')
    keluar = True
    milih = str(input('apakah anda ingin lanjut?: '))
    while keluar:
        if (milih == 'y'):
            return pilihan()
        elif (milih == 't'):
            print('Terima Kasih')
            keluar = False
        else:
            print('Masukkan pilihan yang sesuai')
            return kembali()

def pilihan():
    pilih = int(input('Masukkan pilihan anda: '))
    #Reamur
    if (pilih == 1):
        celcius = float(input('Masukkan celcius: '))
        reamur = (4/5) * celcius
        print(celcius, 'celcius =', reamur, 'reamur')
        return kembali()
    #Fahrenheit
    elif (pilih == 2):
        celcius = float(input('Masukkan celcius: '))
        fahrenheit = (9/5) * celcius + 32
        print(celcius, 'celcius =', fahrenheit, 'fahrenheit')
        return kembali()
    #Kelvin
    elif (pilih == 3):
        celcius = float(input('Masukkan celcius: '))
        kelvin = celcius + 273
        print(celcius, 'celcius =', kelvin, 'kelvin')
        return kembali()
    else:
        print('Masukkan pilihan yang benar!')
        return pilihan()

pilihan()
