print("=" * 50)
print("          SELAMAT DATANG DI ALFIE'STORE          ")
print("=" * 50)

username = input("Masukkan Username (Nama Panggilan) : ")
password = input("Masukkan Password (2 Digit NIM)    : ")

password_benar = "86" 

if username != "" and password == password_benar:
    print("\nLogin Berhasil! Memuat sistem top up...\n")
    print("=" * 50)
    print("                MENU UTAMA TOP UP                 ")
    print("=" * 50)
    
    id_player = input("Masukkan ID Player          : ")
    
    print("\nPilih Nama Game:")
    print("1. Genshin Impact")
    print("2. Minecraft")
    print("3. Mobile Legends")
    pilih_game = input("Masukkan pilihan game (1/2/3): ")
    
    if pilih_game == "1":
        nama_game = "Genshin Impact"
    elif pilih_game == "2":
        nama_game = "Minecraft"
    elif pilih_game == "3":
        nama_game = "Mobile Legends"
    else:
        nama_game = "Game Umum"

    print("\nPilih Kategori Top Up:")
    print("- Kecil    (Rp 15.000)")
    print("- Menengah (Rp 50.000)")
    print("- Besar    (Rp 150.000)")
    kategori = input("Masukkan Kategori (Kecil/Menengah/Besar): ").capitalize()

    if kategori == "Kecil":
        harga_dasar = 15000
    elif kategori == "Menengah":
        harga_dasar = 50000
    elif kategori == "Besar":
        harga_dasar = 150000
    else:
        harga_dasar = 15000
        kategori = "Kecil (Default)"

    print("\nPilih Metode Pembayaran:")
    print("- Pulsa")
    print("- E-Wallet")
    metode = input("Masukkan Metode Pembayaran (Pulsa/E-Wallet): ").capitalize()

    biaya_admin = 2500 if metode == "Pulsa" else 500
    total_bayar = harga_dasar + biaya_admin

    print("\n" + "=" * 50)
    print(f" RINCIAN SEMENTARA TRANSAKSI:")
    print(f" Harga Dasar      : Rp {harga_dasar:,}")
    print(f" Biaya Admin      : Rp {biaya_admin:,}")
    print(f" Total Bayar      : Rp {total_bayar:,}")
    print("=" * 50)

    uang_bayar = int(input("Masukkan nominal uang pembayaran: Rp "))

    if uang_bayar < total_bayar:
        print("Transaksi Gagal! Saldo tidak mencukupi.")
    else:
        kembalian = uang_bayar - total_bayar
        
        print("\n" + "=" * 50)
        print("               STRUK PEMBELIAN TOP UP             ")
        print("=" * 50)
        print(f" ID Player         : {id_player}")
        print(f" Nama Game         : {nama_game}")
        print(f" Kategori Top Up   : {kategori}")
        print(f" Metode Pembayaran : {metode}")
        print("-" * 50)
        print(f" Harga Dasar       : Rp {harga_dasar:,}")
        print(f" Biaya Admin       : Rp {biaya_admin:,}")
        print(f" Total Bayar       : Rp {total_bayar:,}")
        print(f" Uang Tunai        : Rp {uang_bayar:,}")
        print(f" Kembalian         : Rp {kembalian:,}")
        print("=" * 50)
        print("  TERIMA KASIH TELAH BERTRANSAKSI DI ALFIE'STORE!  ")
        print("=" * 50)

else:
    print(" Login Gagal! Username atau Password salah.")