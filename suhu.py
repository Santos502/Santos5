#revisi lagi

print('\n Kalkulator Suhu \n')

def kembali():
    print('apakah anda ingin lanjut? y|t')
    keluar = True
    milih = str(input('apakah anda ingin lanjut?: '))
    while keluar:
        if (milih == 'y'):
            print('Ya')
            return konversi()
        elif (milih == 't'):
            print('Terima Kasih!')
            keluar = False
        else:
            print('Masukkan pilihan yang sesuai')
            return kembali()

def konversi():
    print('1. Celcius')
    print('2. Reamur')
    print('3. Fahrenheit')
    print('4. Kelvin')
    pilih = int(input('Masukkan pilihan konversi suhu: '))
    #Celcius
    if (pilih == 1):
        celcius = float(input('Masukkan celcius: '))
        print('celcius = ', celcius)
        reamur = (4/5) * celcius
        print(celcius, 'celcius =', reamur, 'reamur')
        fahrenheit = (9/5) * celcius + 32
        print(celcius, 'celcius =', fahrenheit, 'fahrenheit')
        kelvin = celcius + 273
        print(celcius, 'celcius =', kelvin, 'kelvin')
        return kembali()
    #Reamur
    elif (pilih == 2):
        reamur = float(input('Masukkan reamur: '))
        print('reamur = ', reamur)
        celcius = (5/4) * reamur
        print(reamur, 'reamur =', celcius, 'celcius')
        fahrenheit = (9/4) * reamur + 32
        print(reamur, 'reamur =', fahrenheit, 'fahrenheit')
        kelvin = (5/4) * reamur + 273
        print(reamur, 'reamur =', kelvin, 'kelvin')
        return kembali()
    #Fahrenheit
    elif (pilih == 3):
        fahrenheit = float(input('Masukkan fahrenheit: '))
        print('fahrenheit = ', fahrenheit)
        celcius = (5/9) * (fahrenheit-32)
        print(fahrenheit, 'fahrenheit =', celcius, 'celcius')
        reamur = (4/9) * (fahrenheit-32)
        print(fahrenheit, 'fahrenheit =', reamur, 'reamur')
        kelvin = (5/9) * (fahrenheit-32) + 273
        print(fahrenheit, 'fahrenheit =', kelvin, 'kelvin')
        return kembali()
    #Kelvin
    elif (pilih == 4):
        kelvin = float(input('Masukkan kelvin: '))
        print('kelvin = ', kelvin)
        celcius = kelvin - 273
        print(kelvin, 'kelvin =', celcius, 'celcius')
        reamur = (4/5) * (kelvin-273)
        print(kelvin, 'kelvin =', reamur, 'reamur')
        fahrenheit = (9/5) * (kelvin-273) + 32
        print(kelvin, 'kelvin =', fahrenheit, 'fahrenheit')
        return kembali()
    else:
        print('Masukkan pilihan yang sesuai!')
        return konversi()

konversi()
