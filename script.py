from food import Food
from drink import Drink
from snack import Snack
from softdrink import SoftDrink

# Jika Ingin Menggunakan Function

# from makanan_berat import Berat
# from makanan_ringan import Ringan
# from minuman_dingin import Dingin
# from minuman_panas import Panas

food1 = Food('Nasi Goreng', 11, 330)
food2 = Food('Rujak Cingur', 9, 450)
food3 = Food('Tahu Tek', 12, 550)

foods = [food1, food2, food3]

snack1 = Snack('Keriping Tempe', 8, 90)
snack2 = Snack('Citathos', 4, 75)
snack3 = Snack('Roti Nana', 2, 35)

snacks = [snack1, snack2, snack3]

softdrink1 = SoftDrink('Es Josua', 4, 180)
softdrink2 = SoftDrink('Es Campur', 8, 350)
softdrink3 = SoftDrink('Es Cincau', 6, 200)

softdrinks = [softdrink1, softdrink2, softdrink3]

drink1 = Drink('Kopi Hitam', 3, 25)
drink2 = Drink('Kopi ToraMoca', 5, 30)
drink3 = Drink('Kopi Espresso', 10, 30)

drinks = [drink1, drink2, drink3]


print('Selamat Datang Di Warung Python Zidqy')
print('Berikut Ini Beberapa List Menu Makanan & Minuman')

print('--------------------')
print('- List Menu Hidangan')

print('1. Makanan')
print('2. Minuman')

print('--------------------')

menu = int(input('Pilih List Diatas : '))

# Jika Memilih Makanan

if menu == 1 :
            print('- List Makanan')
            print('--------------------')
            print('1. Makanan Berat')
            print('2. Makanan Ringan')
            print('--------------------')
            input_makanan = int(input('Makanan Apa Yang Kamu Inginkan Kawan? : '))

            # Jika Memilih Makanan Berat
            if input_makanan == 1 :
                print('- List Makanan Berat')
                print('--------------------')
                print('1. Rujak Cingur  - Harga : 9k')
                print('2. Nasi Goreng   - Harga : 11k')
                print('3. Tahu Tek      - Harga : 13k')
                print('4. Untuk Kembali Ke Menu Sebelumnya')
                print('--------------------')
                pilih_makananberat = int(input("Pilihlah Berbagai Minuman Di Atas : "))
                order_makananberat = int(input("Mau Pesen Berapa? : "))
                if pilih_makananberat == 1 :
                    print("Jadi Totalnya Adalah : ", 9 * order_makananberat,'k')
                elif pilih_makananberat == 2 :
                    print("Jadi Totalnya Adalah : ", 11 * order_makananberat,'k')
                elif pilih_makananberat == 3 :
                    print("Jadi Totalnya Adalah : ", 13 * order_makananberat,'k')
                elif pilih_makananberat == 4 :
                    print("Anda Telah Kembali ")
                else :
                    print("Pilihan Tidak Dimengerti") 

            # Jika Memilih Makanan Ringan
            elif input_makanan == 2 :
                print('- List Makanan Ringan')
                print('--------------------')
                print('1. Kripik Tempe  - Harga : 8k')
                print('2. Citathos      - Harga : 4k')
                print('3. Roti Nana     - Harga : 2k')
                print('4. Untuk Kembali Ke Menu Sebelumnya')
                print('--------------------')
                pilih_makananringan = int(input("Pilihlah Berbagai Minuman Di Atas : "))
                order_makananringan = int(input("Mau Pesen Berapa? : "))
                if pilih_makananringan == 1 :
                    print("Jadi Totalnya Adalah : ", 8 * order_makananringan,'k')
                elif pilih_makananringan == 2 :
                    print("Jadi Totalnya Adalah : ", 4 * order_makananringan,'k')
                elif pilih_makananringan == 3 :
                    print("Jadi  Adalah : ", 2 * order_makananringan,'k')
                elif pilih_makananringan == 'x' :
                    print("Anda Telah Kembali ")
                else :
                    print("Pilihan Tidak Dimengerti")
            else :
                print('Masukkan List Yang Benar')
        
# Jika Memilih Minuman
elif menu == 2 :
            print('- List Minuman')
            print('--------------------')
            print('1. Minuman Dingin')
            print('2. Minuman Panas')
            print('--------------------')
            input_minuman = int(input("Minuman Apa Yang Kamu Inginkan Kawan? : "))

            # Jika Memilih Minuman Dingin
            if input_minuman == 1 :
                    print('- List Minuman Dingin')
                    print('--------------------')
                    print('1. Es Joshua     - Harga : 4k')
                    print('2. Es Campur     - Harga : 8k')
                    print('3. Es Cincau     - Harga : 6k')
                    print('4. Untuk Kembali Ke Menu Sebelumnya')
                    print('--------------------')
                    pilih_minumandingin = int(input("Pilihlah Berbagai Minuman Di Atas : "))
                    order_minumdingin = int(input("Mau Pesen Berapa? : "))
                    if pilih_minumandingin == 1 :
                        print("Jadi Totalnya Adalah : ", 4 * order_minumdingin,'k')
                    elif pilih_minumandingin == 2 :
                        print("Jadi Totalnya Adalah : ", 8 * order_minumdingin,'k')
                    elif pilih_minumandingin == 3 :
                        print("Jadi Totalnya Adalah : ", 6 * order_minumdingin,'k')
                    elif pilih_minumandingin == 'x' :
                        print("Anda Telah Kembali ")
                    else :
                        print("Pilihan Tidak Dimengerti")

            # Jika Memilih Minuman Panas
            elif input_minuman == 2 :
                    print('- List Minuman Panas')
                    print('--------------------')
                    print('1. Kopi Hitam    - Harga : 8k')
                    print('2. Kopi ToraMoca - Harga : 4k')
                    print('3. Kopi Espresso - Harga : 2k')
                    print('4. Untuk Kembali Ke Menu Sebelumnya')
                    print('--------------------')
                    pilih_minumanpanas = int(input("Pilihlah Berbagai Minuman Di Atas : "))
                    order_minumpanas = int(input("Mau Pesen Berapa? : "))
                    if pilih_minumanpanas == 1 :
                        print("Jadi Totalnya Adalah : ", 4 * order_minumpanas,'k')
                    elif pilih_minumanpanas == 2 :
                        print("Jadi Totalnya Adalah : ", 8 * order_minumpanas,'k')
                    elif pilih_minumanpanas == 3 :
                        print("Jadi Totalnya Adalah : ", 6 * order_minumpanas,'k')
                    elif pilih_minumanpanas == 'x' :
                        print("Anda Telah Kembali ")
                    else :
                        print("Pilihan Tidak Dimengerti")
else :
        print('Masukkan List Yang Benar')
            