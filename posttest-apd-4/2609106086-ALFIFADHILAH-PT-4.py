def main():
    
    # USERNAME: alfie
    # PASSWORD: 086
    CORRECT_USERNAME = "alfie"
    CORRECT_PIN = "086"       
    saldo = 1000000
    
    max_percobaan = 3
    login_berhasil = False

    print("=" * 45)
    print("        SELAMAT DATANG DI ATM ALFIE'S")
    print("=" * 45)

    for percobaan in range(1, max_percobaan + 1):
        print(f"\n--- Percobaan Login ke-{percobaan} dari {max_percobaan} ---")
        username_input = input("Masukkan Username : ")
        pin_input = input("Masukkan PIN (3 digit): ")

        if username_input == CORRECT_USERNAME and pin_input == CORRECT_PIN:
            login_berhasil = True
            break
        else:
            sisa_percobaan = max_percobaan - percobaan
            if sisa_percobaan > 0:
                print(f"Login Gagal! Sisa percobaan: {sisa_percobaan}")
            else:
                print("Login Gagal!")

    if not login_berhasil:
        print("\n" + "=" * 20)
        print("Akun Anda Terblokir!")
        print("=" * 20)
        return

    # --- MENU UTAMA ATM ---
    while True:
        print("\n" + "=" * 45)
        print("                MENU UTAMA ATM")
        print("=" * 45)
        print(" [1] Cek Saldo")
        print(" [2] Tarik Tunai")
        print(" [3] Setor Tunai")
        print(" [4] Keluar")
        print("=" * 45)
        
        pilihan = input("Silakan pilih menu (1-4): ")

        if pilihan == "1":
            print("\n---------------------------------------------")
            print(f"Sisa saldo Anda saat ini: Rp {saldo:,}")
            print("---------------------------------------------")

        elif pilihan == "2":
            print("\n--- MENU TARIK TUNAI ---")
            print("Ketentuan: Nominal harus kelipatan Rp 50.000 atau Rp 100.000")
            try:
                tarik = int(input("Masukkan nominal tarik tunai: Rp "))
                
                if tarik % 50000 != 0:
                    print("Kesalahan: Nominal harus kelipatan Rp 50.000!")
                elif tarik > saldo:
                    print("Saldo tidak mencukupi!")
                elif tarik <= 0:
                    print("Nominal penarikan harus lebih dari 0!")
                else:
                    saldo -= tarik
                    print("\nTransaksi Berhasil!")
                    print(f"Nominal ditarik : Rp {tarik:,}")
                    print(f"Sisa saldo      : Rp {saldo:,}")
            except ValueError:
                print("Masukkan angka yang valid!")

        elif pilihan == "3":
            print("\n--- MENU SETOR TUNAI ---")
            print("Ketentuan: Nominal harus kelipatan Rp 50.000")
            try:
                setor = int(input("Masukkan nominal setor tunai: Rp "))
                
                if setor <= 0:
                    print("Nominal setor harus lebih dari 0!")
                elif setor % 50000 != 0:
                    print("Kesalahan: Nominal harus kelipatan Rp 50.000!")
                else:
                    saldo += setor
                    print("\nTransaksi Berhasil!")
                    print(f"Nominal disetor : Rp {setor:,}")
                    print(f"Total saldo kini: Rp {saldo:,}")
            except ValueError:
                print("Masukkan angka yang valid!")

        elif pilihan == "4":
            print("\n" + "=" * 51)
            print("Terima kasih telah menggunakan layanan ATM ALFIE'S.")
            print("=" * 51)
            break
        
        else:
            print("Pilihan tidak valid! Silakan pilih menu 1 sampai 4.")

if __name__ == "__main__":
    main()