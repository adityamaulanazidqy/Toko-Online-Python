while True :
    print('>_< Selamat Datang Di Warung Python Zidqy >_<')
    print('👇 Berikut Ini Beberapa List Menu Makanan & Minuman 👇')

    print('\n- List Menu Hidangan')
    print('--------------------')

    print('1. Makanan')
    print('2. Minuman')
    print('3. Keluar ✖️')

    print('--------------------')

    menu = int(input('Pilih List Diatas : '))

    # Jika Memilih Makanan

    if menu == 1 :
            print('\n- List Makanan')
            print('--------------------')
            print('1. Makanan Berat')
            print('2. Makanan Ringan')
            print('4. Kembali Ke Menu Hidangan')
            print('5. Keluar ✖️')
            print('--------------------')
            input_makanan = int(input('Makanan Apa Yang Kamu Inginkan Kawan? : '))

            # Jika Memilih Makanan Berat
            if input_makanan == 1 :
                print('\n- List Makanan Berat')
                print('--------------------')
                print('1. Rujak Cingur  - Harga : 9k')
                print('2. Nasi Goreng   - Harga : 11k')
                print('3. Tahu Tek      - Harga : 13k')
                print('4. Kembali Ke Menu Hidangan')
                print('5. Keluar ✖️')
                print('--------------------')
                pilih_makananberat = int(input("Pilihlah Berbagai Makanan Berat Di Atas : "))

                if pilih_makananberat == 1 :
                    order_makananberat = int(input("Mau Pesen Berapa? : "))
                    print("Jadi Totalnya Adalah : ", 9 * order_makananberat,'k\n')
                    yakin_berat_1 = input('Mau Pesan Lagi?( yah / tidak ) : ')
                    if yakin_berat_1 == 'yah' :
                        continue
                    elif yakin_berat_1 == 'tidak' :
                        print('Yah Sudah Datang Kembali Yah Kapan\"')
                        break
                    else :
                        print('Anda Keluar, Masukkan Tidak Dimengerti')
                        break

                elif pilih_makananberat == 2 :
                    order_makananberat = int(input("Mau Pesen Berapa? : "))
                    print("Jadi Totalnya Adalah : ", 11 * order_makananberat,'k\n')
                    yakin_berat_2 = input('Mau Pesan Lagi?( yah / tidak ) : ')
                    if yakin_berat_2 == 'yah' :
                        continue
                    elif yakin_berat_2 == 'tidak' :
                        print('Yah Sudah Datang Kembali Yah Kapan\"')
                        break
                    else :
                        print('Anda Keluar, Masukkan Tidak Dimengerti')
                        break
                elif pilih_makananberat == 3 :
                    order_makananberat = int(input("Mau Pesen Berapa? : "))
                    print("Jadi Totalnya Adalah : ", 13 * order_makananberat,'k\n')
                    yakin_berat_3 = input('Mau Pesan Lagi?( yah / tidak ) : ')
                    if yakin_berat_3 == 'yah' :
                        continue
                    elif yakin_berat_3 == 'tidak' :
                        print('Yah Sudah Datang Kembali Yah Kapan\"')
                        break
                    else :
                        print('Anda Keluar, Masukkan Tidak Dimengerti')
                        break
                elif pilih_makananberat == 4 :
                    print("Kembali Ke Menu Hidangan")
                    continue
                elif pilih_makananberat == 5 :
                    print("Sampai Jumpa Lagi Yah!")
                    break
                else :
                    print('Maaf Perintah Tidak Dimengerti')

            # Jika Memilih Makanan Ringan
            elif input_makanan == 2 :
                print('\n- List Makanan Ringan')
                print('--------------------')
                print('1. Kripik Tempe  - Harga : 8k')
                print('2. Citathos      - Harga : 4k')
                print('3. Roti Nana     - Harga : 2k')
                print('4. Kembali Ke Menu Hidangan')
                print('5. Keluar ✖️')
                print('--------------------')
                pilih_makananringan = int(input("Pilihlah Berbagai Makanan Ringan Di Atas : "))

                if pilih_makananringan == 1 :
                    order_makananringan = int(input("Mau Pesen Berapa? : "))
                    print("Jadi Totalnya Adalah : ", 8 * order_makananringan,'k\n')
                    yakin_ringan_1 = input('Mau Pesan Lagi?( yah / tidak ) : ')
                    if yakin_ringan_1 == 'yah' :
                        continue
                    elif yakin_ringan_1 == 'tidak' :
                        print('Yah Sudah Datang Kembali Yah Kapan\"')
                        break
                    else :
                        print('Anda Keluar, Masukkan Tidak Dimengerti')
                        break
                elif pilih_makananringan == 2 :
                    order_makananringan = int(input("Mau Pesen Berapa? : "))
                    print("Jadi Totalnya Adalah : ", 4 * order_makananringan,'k\n')
                    yakin_ringan_2 = input('Mau Pesan Lagi?( yah / tidak ) : ')
                    if yakin_ringan_2 == 'yah' :
                        continue
                    elif yakin_ringan_2 == 'tidak' :
                        print('Yah Sudah Datang Kembali Yah Kapan\"')
                        break
                    else :
                        print('Anda Keluar, Masukkan Tidak Dimengerti')
                        break
                elif pilih_makananringan == 3 :
                    order_makananringan = int(input("Mau Pesen Berapa? : "))
                    print("Jadi  Adalah : ", 2 * order_makananringan,'k\n')
                    yakin_ringan_3 = input('Mau Pesan Lagi?( yah / tidak ) : ')
                    if yakin_ringan_3 == 'yah' :
                        continue
                    elif yakin_ringan_3 == 'tidak' :
                        print('Yah Sudah Datang Kembali Yah Kapan\"')
                        break
                    else :
                        print('Anda Keluar, Masukkan Tidak Dimengerti')
                        break
                elif pilih_makananringan == 4 :
                    print('4. Kembali Ke Menu Hidangan')
                    continue
                elif pilih_makananringan == 5 :
                    print("Sampai Jumpa Lagi Yah!")
                    break
                else :
                    print('Maaf Perintah Tidak Dimengerti')
            else :
                print('Masukkan List Yang Benar')
                continue
        
    # Jika Memilih Minuman
    elif menu == 2 :
            print('\n- List Minuman')
            print('--------------------')
            print('1. Minuman Dingin')
            print('2. Minuman Panas')
            print('4. Kembali Ke Menu Hidangan')
            print('5. Keluar ✖️')
            print('--------------------')
            input_minuman = int(input("Minuman Apa Yang Kamu Inginkan Kawan? : "))

            # Jika Memilih Minuman Dingin
            if input_minuman == 1 :
                    print('\n- List Minuman Dingin 🥶')
                    print('--------------------')
                    print('1. Es Joshua     - Harga : 4k')
                    print('2. Es Campur     - Harga : 8k')
                    print('3. Es Cincau     - Harga : 6k')
                    print('4. Kembali Ke Menu Hidangan')
                    print('5. Keluar ✖️')
                    print('--------------------')
                    pilih_minumandingin = int(input("Pilihlah Berbagai Minuman Dingin Di Atas : "))

                    if pilih_minumandingin == 1 :
                        order_minumdingin = int(input("Mau Pesen Berapa? : "))
                        print("Jadi Totalnya Adalah : ", 4 * order_minumdingin,'k\n')

                        yakin_dingin_1 = input('Mau Pesan Lagi?( yah / tidak ) : ')
                        if yakin_dingin_1 == 'yah' :
                            continue
                        elif yakin_dingin_1 == 'tidak' :
                            print('Yah Sudah Datang Kembali Yah Kapan\"')
                            break
                        else :
                            print('Anda Keluar, Masukkan Tidak Dimengerti')
                            break
                    elif pilih_minumandingin == 2 :
                        order_minumdingin = int(input("Mau Pesen Berapa? : "))
                        print("Jadi Totalnya Adalah : ", 8 * order_minumdingin,'k\n')

                        yakin_dingin_2 = input('Mau Pesan Lagi?( yah / tidak ) : ')
                        if yakin_dingin_2 == 'yah' :
                            continue
                        elif yakin_dingin_2 == 'tidak' :
                            print('Yah Sudah Datang Kembali Yah Kapan\"')
                            break
                        else :
                            print('Anda Keluar, Masukkan Tidak Dimengerti')
                            break
                    elif pilih_minumandingin == 3 :
                        order_minumdingin = int(input("Mau Pesen Berapa? : "))
                        print("Jadi Totalnya Adalah : ", 6 * order_minumdingin,'k\n')

                        yakin_dingin_3 = input('Mau Pesan Lagi?( yah / tidak ) : ')
                        if yakin_dingin_3 == 'yah' :
                            continue
                        elif yakin_dingin_3 == 'tidak' :
                            print('Yah Sudah Datang Kembali Yah Kapan\"')
                            break
                        else :
                            print('Anda Keluar, Masukkan Tidak Dimengerti')
                            break
                    elif pilih_minumandingin == 4 :
                        print('4. Kembali Ke Menu Hidangan')
                        continue
                    elif pilih_makananringan == 5 :
                        print("Sampai Jumpa Lagi Yah!")
                        break
                    else :
                        print('Maaf Perintah Tidak Dimengerti')

            # Jika Memilih Minuman Panas
            elif input_minuman == 2 :
                    print('\n- List Minuman Panas 🥵')
                    print('--------------------')
                    print('1. Kopi Hitam    - Harga : 8k')
                    print('2. Kopi ToraMoca - Harga : 4k')
                    print('3. Kopi Espresso - Harga : 2k')
                    print('4. Kembali Ke Menu Hidangan')
                    print('5. Keluar ✖️')
                    print('--------------------')
                    pilih_minumanpanas = int(input("Pilihlah Berbagai Minuman Panas Di Atas : "))

                    if pilih_minumanpanas == 1 :
                        order_minumpanas = int(input("Mau Pesen Berapa? : "))
                        print("Jadi Totalnya Adalah : ", 4 * order_minumpanas,'k\n')

                        yakin_panas_1 = input('Mau Pesan Lagi?( yah / tidak ) : ')
                        if yakin_panas_1 == 'yah' :
                            continue
                        elif yakin_panas_1 == 'tidak' :
                            print('Yah Sudah Datang Kembali Yah Kapan\"')
                            break
                        else :
                            print('Anda Keluar, Masukkan Tidak Dimengerti')
                            break
                    elif pilih_minumanpanas == 2 :
                        order_minumpanas = int(input("Mau Pesen Berapa? : "))
                        print("Jadi Totalnya Adalah : ", 8 * order_minumpanas,'k\n')

                        yakin_panas_2 = input('Mau Pesan Lagi?( yah / tidak ) : ')
                        if yakin_panas_2 == 'yah' :
                            continue
                        elif yakin_panas_2 == 'tidak' :
                            print('Yah Sudah Datang Kembali Yah Kapan\"')
                            break
                        else :
                            print('Anda Keluar, Masukkan Tidak Dimengerti')
                            break
                    elif pilih_minumanpanas == 3 :
                        order_minumpanas = int(input("Mau Pesen Berapa? : "))
                        print("Jadi Totalnya Adalah : ", 6 * order_minumpanas,'k\n')

                        yakin_panas_3 = input('Mau Pesan Lagi?( yah / tidak ) : ')
                        if yakin_panas_3 == 'yah' :
                            continue
                        elif yakin_panas_3 == 'tidak' :
                            print('Yah Sudah Datang Kembali Yah Kapan\"')
                            break
                        else :
                            print('Anda Keluar, Masukkan Tidak Dimengerti')
                            break
                    elif pilih_minumanpanas == 4 :
                        print('4. Kembali Ke Menu Hidangan')
                        continue
                    elif pilih_makananringan == 5 :
                        print("Sampai Jumpa Lagi Yah!")
                        break
                    else :
                        print('Maaf Perintah Tidak Dimengerti')
    else :
            print("Sampai Jumpa Lagi Yah!")
            break
