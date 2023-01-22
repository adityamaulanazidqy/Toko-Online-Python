while True :
    # Pembukaan
    print(' -----------------------------------------------')
    print('| >_< Selamat Datang Di Warung Python Zidqy >_< |')
    print(' -----------------------------------------------') 
    print('\n👇 Berikut Ini Beberapa List Menu Makanan & Minuman 👇\n')
    print(' --------------------')
    print('| List Menu Hidangan |')
    print(' --------------------')
    print('| 1. Makanan         |')
    print('| 2. Minuman         |')
    print(' --------------------')
    print('| 3. Keluar ✖️        |')

    print(' --------------------')

    menu = int(input('\nPilih List Diatas : '))

    # Jika Memilih Makanan

    if menu == 1 :
            print('\n        --------------')
            print('       | List Makanan |')
            print('        --------------')
            print(' ---------------------------')
            print('| 1. Makanan Berat           |')
            print('| 2. Makanan Ringan          |')
            print('| 3. Kembali Ke Menu Hidangan|')
            print('| 4. Keluar ✖️                |')
            print(' ---------------------------')
            input_makanan = int(input('\nMakanan Apa Yang Kamu Inginkan Kawan? : '))

            # Jika Memilih Makanan Berat
            if input_makanan == 1 :
                print('\n       --------------------')
                print('      | List Makanan Berat |')
                print('       --------------------')
                print(' -------------------------------')
                print('|     Nome        |     Harga   |')
                print(' -------------------------------')
                print('| 1. Rujak Cingur | 9.000k      |')
                print('| 2. Nasi Goreng  | 11.000k     |')
                print('| 3. Tahu Tek     | 13.000k     |')
                print('|-------------------------------|')
                print('| 4. Kembali Ke Menu Hidangan   |')
                print('| 5. Keluar ✖️                   |')
                print(' -------------------------------')
                pilih_makananberat = int(input("\nPilihlah Berbagai Makanan Berat Di Atas : "))

                if pilih_makananberat == 1 :
                    order_makananberat = int(input("Mau Pesen Berapa? : "))
                    print("Jadi Totalnya Adalah : ", 9 * order_makananberat,'.000k\n')
                    yakin_berat_1 = input('Mau Pesan Lagi?( yah / tidak ) : ')
                    if yakin_berat_1 == 'yah' :
                        continue
                    elif yakin_berat_1 == 'tidak' :
                        print('\n ---------------------')
                        print('|    Selamat Makan!   |')
                        print(' ---------------------\n')
                        break
                    else :
                        print('\nAnda Keluar, Masukkan Tidak Dimengerti\n')
                        break

                elif pilih_makananberat == 2 :
                    order_makananberat = int(input("Mau Pesen Berapa? : "))
                    print("Jadi Totalnya Adalah : ", 11 * order_makananberat,'.000k\n')
                    yakin_berat_2 = input('Mau Pesan Lagi?( yah / tidak ) : ')
                    if yakin_berat_2 == 'yah' :
                        continue
                    elif yakin_berat_2 == 'tidak' :
                        print('\n ---------------------')
                        print('|    Selamat Makan!   |')
                        print(' ---------------------\n')
                        break
                    else :
                        print('\nAnda Keluar, Masukkan Tidak Dimengerti\n')
                        break
                elif pilih_makananberat == 3 :
                    order_makananberat = int(input("Mau Pesen Berapa? : "))
                    print("Jadi Totalnya Adalah : ", 13 * order_makananberat,'.000k\n')
                    yakin_berat_3 = input('Mau Pesan Lagi?( yah / tidak ) : ')
                    if yakin_berat_3 == 'yah' :
                        continue
                    elif yakin_berat_3 == 'tidak' :
                        print('\n ---------------------')
                        print('|    Selamat Makan!   |')
                        print(' ---------------------\n')
                        break
                    else :
                        print('\nAnda Keluar, Masukkan Tidak Dimengerti\n')
                        break
                elif pilih_makananberat == 4 :
                    print("\nKembali Ke Menu Hidangan\n")
                    continue
                elif pilih_makananberat == 5 :
                    print("\nSampai Jumpa Lagi Yah!\n")
                    break
                else :
                    print('\nMaaf Perintah Tidak Dimengerti\n')

            # Jika Memilih Makanan Ringan
            elif input_makanan == 2 :
                print('\n      ---------------------')
                print('     | List Makanan Ringan |')
                print('      ---------------------')
                print(' -------------------------------')
                print('|     Nomer       |     Harga   |')
                print(' -------------------------------')
                print('| 1. Kripik Tempe  | 8.000k     |')
                print('| 2. Citathos      | 4.000k     |')
                print('| 3. Roti Nana     | 2.000k     |')
                print('|-------------------------------|')
                print('| 4. Kembali Ke Menu Hidangan   |')
                print('| 5. Keluar ✖️                   |')
                print(' -------------------------------')
                pilih_makananringan = int(input("\nPilihlah Berbagai Makanan Ringan Di Atas : "))

                if pilih_makananringan == 1 :
                    order_makananringan = int(input("Mau Pesen Berapa? : "))
                    print("Jadi Totalnya Adalah : ", 8 * order_makananringan,'.000k\n')
                    yakin_ringan_1 = input('Mau Pesan Lagi?( yah / tidak ) : ')
                    if yakin_ringan_1 == 'yah' :
                        continue
                    elif yakin_ringan_1 == 'tidak' :
                        print('\n ---------------------')
                        print('|    Selamat Makan!   |')
                        print(' ---------------------\n')
                        break
                    else :
                        print('\nAnda Keluar, Masukkan Tidak Dimengerti\n')
                        break
                elif pilih_makananringan == 2 :
                    order_makananringan = int(input("Mau Pesen Berapa? : "))
                    print("Jadi Totalnya Adalah : ", 4 * order_makananringan,'.000k\n')
                    yakin_ringan_2 = input('Mau Pesan Lagi?( yah / tidak ) : ')
                    if yakin_ringan_2 == 'yah' :
                        continue
                    elif yakin_ringan_2 == 'tidak' :
                        print('\n ---------------------')
                        print('|    Selamat Makan!   |')
                        print(' ---------------------\n')
                        break
                    else :
                        print('\nAnda Keluar, Masukkan Tidak Dimengerti\n')
                        break
                elif pilih_makananringan == 3 :
                    order_makananringan = int(input("Mau Pesen Berapa? : "))
                    print("Jadi  Adalah : ", 2 * order_makananringan,'.000k\n')
                    yakin_ringan_3 = input('Mau Pesan Lagi?( yah / tidak ) : ')
                    if yakin_ringan_3 == 'yah' :
                        continue
                    elif yakin_ringan_3 == 'tidak' :
                        print('\n ---------------------')
                        print('|    Selamat Makan!   |')
                        print(' ---------------------\n')
                        break
                    else :
                        print('\nAnda Keluar, Masukkan Tidak Dimengerti\n')
                        break
                elif pilih_makananringan == 4 :
                    print('\nKembali Ke Menu Hidangan\n')
                    continue
                elif pilih_makananringan == 5 :
                    print("\nSampai Jumpa Lagi Yah!\n")
                    break
                else :
                    print('\nMaaf Perintah Tidak Dimengerti\n')
                    break
            else :
                print('Masukkan List Yang Benar\n')
                continue
        
    # Jika Memilih Minuman
    elif menu == 2 :
            print('\n        --------------      ')
            print('       | List Minuman |       ')
            print(' ----------------------------')
            print('| 1. Minuman Dingin           |')
            print('| 2. Minuman Panas            |')
            print('| 3. Kembali Ke Menu Hidangan |')
            print('| 4. Keluar ✖️                 |')
            print(' ----------------------------')
            input_minuman = int(input("\nMinuman Apa Yang Kamu Inginkan Kawan? : "))

            # Jika Memilih Minuman Dingin
            if input_minuman == 1 :
                    print('\n      ---------------------    ')
                    print('     | List Minuman Dingin |     ')
                    print('      ---------------------    ')
                    print(' --------------------------------')
                    print('|     Nomer       |     Harga    |')
                    print(' --------------------------------')
                    print('| 1. Es Joshua    | 8.000k       |')
                    print('| 2. Es Campur    | 10.000k      |')
                    print('| 3. Es Cincau    | 6.000k       |')
                    print('|--------------------------------|')
                    print('| 4. Kembali Ke Menu Hidangan    |')
                    print('| 5. Keluar ✖️                    |')
                    print(' --------------------------------')
                    pilih_minumandingin = int(input("\nPilihlah Berbagai Minuman Dingin Di Atas : "))

                    if pilih_minumandingin == 1 :
                        order_minumdingin = int(input("Mau Pesen Berapa? : "))
                        print("Jadi Totalnya Adalah : ", 4 * order_minumdingin,'.000k\n')

                        yakin_dingin_1 = input('Mau Pesan Lagi?( yah / tidak ) : ')
                        if yakin_dingin_1 == 'yah' :
                            continue
                        elif yakin_dingin_1 == 'tidak' :
                            print('\n ---------------------')
                            print('|    Selamat Makan!   |')
                            print(' ---------------------\n')
                            break
                        else :
                            print('\nAnda Keluar, Masukkan Tidak Dimengerti\n')
                            break
                    elif pilih_minumandingin == 2 :
                        order_minumdingin = int(input("Mau Pesen Berapa? : "))
                        print("Jadi Totalnya Adalah : ", 8 * order_minumdingin,'.000k\n')

                        yakin_dingin_2 = input('Mau Pesan Lagi?( yah / tidak ) : ')
                        if yakin_dingin_2 == 'yah' :
                            continue
                        elif yakin_dingin_2 == 'tidak' :
                            print('\n ---------------------')
                            print('|    Selamat Makan!   |')
                            print(' ---------------------\n')
                            break
                        else :
                            print('\nAnda Keluar, Masukkan Tidak Dimengerti\n')
                            break
                    elif pilih_minumandingin == 3 :
                        order_minumdingin = int(input("Mau Pesen Berapa? : "))
                        print("Jadi Totalnya Adalah : ", 6 * order_minumdingin,'.000k\n')

                        yakin_dingin_3 = input('Mau Pesan Lagi?( yah / tidak ) : ')
                        if yakin_dingin_3 == 'yah' :
                            continue
                        elif yakin_dingin_3 == 'tidak' :
                            print('\n ---------------------')
                            print('|    Selamat Makan!   |')
                            print(' ---------------------\n')
                            break
                        else :
                            print('\nAnda Keluar, Masukkan Tidak Dimengerti\n')
                            break
                    elif pilih_minumandingin == 4 :
                        print('\nKembali Ke Menu Hidangan\n')
                        continue
                    elif pilih_makananringan == 5 :
                        print("\nSampai Jumpa Lagi Yah!\n")
                        break
                    else :
                        print('\nMaaf Perintah Tidak Dimengerti\n')

            # Jika Memilih Minuman Panas
            elif input_minuman == 2 :
                    print('\n      --------------------    ')
                    print('     | List Minuman Panas |     ')
                    print('      --------------------    ')
                    print(' --------------------------------')
                    print('|     Nomer       |     Harga    |')
                    print(' --------------------------------')
                    print('| 1. Kopi Hitam   | 3.000k       |')
                    print('| 2. Kopi ToraMoca| 4.000k       |')
                    print('| 3. Kopi Espresso| 2.000k       |')
                    print('|--------------------------------|')
                    print('| 4. Kembali Ke Menu Hidangan    |')
                    print('| 5. Keluar ✖️                    |')
                    print(' --------------------------------')
                    pilih_minumanpanas = int(input("\nPilihlah Berbagai Minuman Panas Di Atas : "))

                    if pilih_minumanpanas == 1 :
                        order_minumpanas = int(input("Mau Pesen Berapa? : "))
                        print("Jadi Totalnya Adalah : ", 3 * order_minumpanas,'.000k\n')

                        yakin_panas_1 = input('Mau Pesan Lagi?( yah / tidak ) : ')
                        if yakin_panas_1 == 'yah' :
                            continue
                        elif yakin_panas_1 == 'tidak' :
                            print('\n ---------------------')
                            print('|    Selamat Makan!   |')
                            print(' ---------------------\n')
                            break
                        else :
                            print('\nAnda Keluar, Masukkan Tidak Dimengerti\n')
                            break
                    elif pilih_minumanpanas == 2 :
                        order_minumpanas = int(input("Mau Pesen Berapa? : "))
                        print("Jadi Totalnya Adalah : ", 4 * order_minumpanas,'.000k\n')

                        yakin_panas_2 = input('Mau Pesan Lagi?( yah / tidak ) : ')
                        if yakin_panas_2 == 'yah' :
                            continue
                        elif yakin_panas_2 == 'tidak' :
                            print('\n ---------------------')
                            print('|    Selamat Makan!   |')
                            print(' ---------------------\n')
                            break
                        else :
                            print('\nAnda Keluar, Masukkan Tidak Dimengerti\n')
                            break
                    elif pilih_minumanpanas == 3 :
                        order_minumpanas = int(input("Mau Pesen Berapa? : "))
                        print("Jadi Totalnya Adalah : ", 2 * order_minumpanas,'.000k\n')

                        yakin_panas_3 = input('Mau Pesan Lagi?( yah / tidak ) : ')
                        if yakin_panas_3 == 'yah' :
                            continue
                        elif yakin_panas_3 == 'tidak' :
                            print('\n ---------------------')
                            print('|    Selamat Makan!   |')
                            print(' ---------------------\n')
                            break
                        else :
                            print('\nAnda Keluar, Masukkan Tidak Dimengerti\n')
                            break
                    elif pilih_minumanpanas == 4 :
                        print('\nKembali Ke Menu Hidangan\n')
                        continue
                    elif pilih_makananringan == 5 :
                        print("\nSampai Jumpa Lagi Yah!\n")
                        break
                    else :
                        print('\nMaaf Perintah Tidak Dimengerti\n')
                        break
    else :
            print('\n  -------------------------')
            print(" | Sampai Jumpa Lagi Yah!  |")
            print('  -------------------------\n')
            break
