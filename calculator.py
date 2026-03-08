# Kalkulator sederhana

def penambahan(a, b) :
    return a + b

def pengurangan(a, b):
    return a - b

def perkalian(a, b):
    return a * b

def pembagian(a, b):
    if b == 0:
        print('Tak Terdefinisikan')
    else:
        return a/b

def hitung(pilihan, a, b):
    if pilihan == '1':
        return penambahan(a, b), f'{a} + {b}'
    
    elif pilihan == '2':
        return pengurangan(a, b), f'{a} - {b}'
    
    elif pilihan == '3':
        return perkalian(a, b), f'{a} * {b}'
    
    elif pilihan == '4':
        return pembagian(a, b), f'{a} / {b}'
    
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

        if pilihan in ['1', '2', '3', '4']:
            try:
                a = float(input('Masukkan angka pertama: '))
                b = float(input('Masukkan angka kedua: '))
            except ValueError:
                print('Input tidak valid! Masukkan angka.')
                continue

            hasil, operasi = hitung(pilihan, a, b)

            if hasil is not None:
                print(f'Hasil: {hasil}')
                riwayat.append(f'{operasi} = {hasil}')

            print('\n----- Riwayat -----')
            for x, y in enumerate(riwayat[-5:], 1):
                print(f'{x}. {y}')

        elif pilihan == '5':
            print('Terima Kasih')
            break

        else:
            print('Inputan tidak valid! Masukkan 1-5.')

main()