from food import Food
from drink import Drink
from snack import Snack
from softdrink import SoftDrink

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
print('Makanan Berat')
index = 0
for food in foods:
    print(str(index) + '. ' + food.info())
    index += 1

print('Makanan Ringan')
index = 0
for snack in snacks:
    print(str(index) + '. ' + snack.info())
    index += 1

print('Minuman Dingin')
index = 0
for softdrink in softdrinks:
    print(str(index) + '. ' + softdrink.info())
    index += 1

print('Minuman Panas')
index = 0
for drink in drinks:
    print(str(index) + '. ' + drink.info())
    index += 1

print('--------------------')

food_order = int(input('Masukkan List makanan Berat : '))
selected_food = foods[food_order]

snack_order = int(input('Masukkan List makanan Ringan : '))
selected_snack = snacks[snack_order]

softdrink_order = int(input('Masukkan List minuman Dingin : '))
selected_softdrink = drinks[softdrink_order]

drink_order = int(input('Masukkan List minuman Panas : '))
selected_drink = drinks[drink_order]


# Ambil input dari console dan tetapkan ke variable count
count = int(input('Mau Pesan berapa paket makanan berat? (Mumpung Ada Diskon 10% untuk 3 atau lebih Loh!): '))

# Panggil method get_total_price dari selected_food dan selected_drink
result = selected_food.get_total_price(count) +  selected_snack.get_total_price(count) + selected_drink.get_total_price(count) + selected_softdrink.get_total_price(count) 
# Cetak 'Total harga adalah $____'
print('Total harga adalah ' + str (result) + 'k')
print('Terima Kasih Sudah Beli Di Warung Python Saya...')
