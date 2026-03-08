# Kalkulator sederhana

def penambahan(a, b) :
    return a + b

def pengurangan(a, b):
    return a - b

def  perkalian(a, b):
    return a * b

def pembagian(a, b):
    if b == 0:
        print('Tak Terdefinisikan')
    else:
        return a/b

def menu():
    print('='*5,'Kalkulator','='*5)
    print('1, Penambahan')
    print('2, Pengurangan')
    print('3, Perkalian')
    print('4, Pembagian')
    print('5, Keluar')

def main():
    riwayat = []

    while True:
        menu()
        pilihan = input('Pilih Operasi(1-5): ')

        if pilihan == '1':
            a = int(input('Masukkan angka: '))
            b = int(input('Masukkan angka: '))
            hasil = penambahan(a,b)
            print(hasil)
            riwayat.append(hasil)
            print(riwayat)
        elif pilihan == '2':
            a = int(input('Masukkan angka: '))
            b = int(input('Masukkan angka: '))
            hasil = pengurangan(a,b)
            print(hasil)
            riwayat.append(hasil)
            print(riwayat)
        elif pilihan == '3':
            a = int(input('Masukkan angka: '))
            b = int(input('Masukkan angka: '))
            hasil = perkalian(a,b)
            print(hasil)
            riwayat.append(hasil)
            print(riwayat)
        elif pilihan == '4':
            a = int(input('Masukkan angka: '))
            b = int(input('Masukkan angka: '))
            hasil = pembagian(a,b)
            print(hasil)
            riwayat.append(hasil)
            print(riwayat)
        elif pilihan == '5':
            print('Terima Kasih')
            break
        else:
            print('Inputan tidak valid')

    
main()