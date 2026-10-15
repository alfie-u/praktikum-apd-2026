import os

users = [
    ["admin", "admin123", "admin"],
    ["alfie", "123", "user"]
]

pets = [
    [1, "Milo", "Kucing", "2 Tahun", "Jantan", "Belum Diadopsi"],
    [2, "Luna", "Anjing", "1 Tahun", "Betina", "Belum Diadopsi"],
    [3, "Leo", "Kucing", "3 Tahun", "Jantan", "Sudah Diadopsi"]
]

status_login = False
role_login = ""
user_aktif = ""

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 45)
    print("       APLIKASI ADOPSI HEWAN PELIHARAAN")
    print("=" * 45)
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    print("-" * 45)
    
    pilihan_awal = input("Pilih menu (1-3): ")
    
    if pilihan_awal == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("--- MENU LOGIN ---")
        username_input = input("Masukkan Username: ")
        password_input = input("Masukkan Password: ")
        
        login_sukses = False
        for u in users:
            if u[0] == username_input and u[1] == password_input:
                login_sukses = True
                role_login = u[2]
                user_aktif = u[0]
                break
        
        if login_sukses:
            print(f"\n[SUKSES] Selamat datang, {user_aktif} ({role_login})!")
            input("Tekan Enter untuk masuk ke menu utama...")
            status_login = True
            
            while status_login:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=" * 45)
                print(f"       DASHBOARD ADOPSI HEWAN [{role_login.upper()}]")
                print("=" * 45)
                print("1. Lihat Daftar Hewan")
                if role_login == "admin":
                    print("2. Tambah Data Hewan")
                    print("3. Ubah Data / Status Hewan")
                    print("4. Hapus Data Hewan")
                else:
                    print("2. Ajukan Adopsi Hewan")
                print("5. Logout")
                print("-" * 45)
                
                menu_pilih = input("Pilih menu: ")
  
                if menu_pilih == "1":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("--- DAFTAR HEWAN PELIHARAAN ---")
                    print("1. Tampilkan Semua Hewan")
                    print("2. Cari Berdasarkan Nama")
                    print("3. Filter Berdasarkan Status")
                    sub_read = input("Pilih opsi (1-3): ")
                    
                    if sub_read == "1":
                        print("\n--- Seluruh Hewan ---")
                        if len(pets) == 0:
                            print("Belum ada data hewan.")
                        else:
                            for p in pets:
                                print(f"ID: {p[0]} | Nama: {p[1]} | Jenis: {p[2]} | Usia: {p[3]} | Kelamin: {p[4]} | Status: {p[5]}")
                    
                    elif sub_read == "2":
                        cari_nama = input("\nMasukkan nama hewan yang dicari: ")
                        ditemukan = False
                        for p in pets:
                            if p[1].lower() == cari_nama.lower():
                                print(f"\n[DITEMUKAN] ID: {p[0]} | Nama: {p[1]} | Jenis: {p[2]} | Usia: {p[3]} | Kelamin: {p[4]} | Status: {p[5]}")
                                ditemukan = True
                                break
                        if not ditemukan:
                            print("\n[INFO] Hewan dengan nama tersebut tidak ditemukan.")
                    
                    elif sub_read == "3":
                        print("\nPilih Status:")
                        print("1. Belum Diadopsi")
                        print("2. Sudah Diadopsi")
                        pilih_status = input("Pilih (1/2): ")
                        target_status = "Belum Diadopsi" if pilih_status == "1" else "Sudah Diadopsi"
                        
                        print(f"\n--- Daftar Hewan: {target_status} ---")
                        ada = False
                        for p in pets:
                            if p[5] == target_status:
                                print(f"ID: {p[0]} | Nama: {p[1]} | Jenis: {p[2]} | Usia: {p[3]} | Kelamin: {p[4]}")
                                ada = True
                        if not ada:
                            print("Tidak ada hewan dengan status tersebut.")
                    else:
                        print("[ERROR] Pilihan tidak valid.")
                    
                    input("\nTekan Enter untuk kembali ke menu...")

                elif menu_pilih == "2" and role_login == "admin":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("--- TAMBAH DATA HEWAN BARU ---")
                    
                    id_baru = len(pets) + 1
                    if len(pets) > 0:
                        id_baru = pets[-1][0] + 1
                        
                    nama = input("Masukkan Nama Hewan: ")
                    jenis = input("Masukkan Jenis Hewan (Kucing/Anjing): ")
                    usia = input("Masukkan Usia Hewan (Contoh: 2 Tahun): ")
                    kelamin = input("Masukkan Jenis Kelamin (Jantan/Betina): ")
                    status_awal = "Belum Diadopsi"

                    data_baru_tuple = (id_baru, nama, jenis, usia, kelamin, status_awal)
                    pets.append(list(data_baru_tuple))
                    
                    print(f"\n[SUKSES] Data hewan '{nama}' berhasil ditambahkan!")
                    input("\nTekan Enter untuk kembali...")

                elif menu_pilih == "2" and role_login == "user":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("--- AJUKAN ADOPSI HEWAN ---")
                    for p in pets:
                        if p[5] == "Belum Diadopsi":
                            print(f"ID: {p[0]} | Nama: {p[1]} | Jenis: {p[2]} | Usia: {p[3]} | Kelamin: {p[4]}")
                    
                    id_pilih = input("\nMasukkan ID hewan yang ingin diadopsi: ")
                    
                    valid_id = True
                    for karakter in id_pilih:
                        if karakter < '0' or karakter > '9':
                            valid_id = False
                            break
                    
                    if valid_id and id_pilih != "":
                        id_angka = int(id_pilih)
                        berhasil_adopsi = False
                        for p in pets:
                            if p[0] == id_angka and p[5] == "Belum Diadopsi":
                                p[5] = "Sudah Diadopsi"
                                berhasil_adopsi = True
                                break
                        if berhasil_adopsi:
                            print("\n[SUKSES] Selamat! Anda berhasil mengajukan adopsi hewan.")
                        else:
                            print("\n[GAGAL] ID hewan tidak ditemukan atau sudah diadopsi.")
                    else:
                        print("\n[ERROR] Masukkan angka ID yang valid.")
                    
                    input("\nTekan Enter untuk kembali...")

                elif menu_pilih == "3" and role_login == "admin":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("--- UPDATE DATA / STATUS HEWAN ---")
                    print("1. Ubah Status Adopsi Hewan")
                    print("2. Perbaiki Profil (Salah Ketik)")
                    sub_up = input("Pilih opsi (1/2): ")
                    
                    if sub_up == "1":
                        for p in pets:
                            print(f"ID: {p[0]} | Nama: {p[1]} | Status: {p[5]}")
                        id_up = input("\nMasukkan ID hewan yang ingin diubah statusnya: ")
                        
                        valid_id = True
                        for k in id_up:
                            if k < '0' or k > '9':
                                valid_id = False
                                break
                        
                        if valid_id and id_up != "":
                            id_a = int(id_up)
                            ketemu = False
                            for p in pets:
                                if p[0] == id_a:
                                    ketemu = True
                                    if p[5] == "Belum Diadopsi":
                                        p[5] = "Sudah Diadopsi"
                                    else:
                                        p[5] = "Belum Diadopsi"
                                    print(f"\n[SUKSES] Status hewan {p[1]} diubah menjadi: {p[5]}")
                                    break
                            if not ketemu:
                                print("\n[GAGAL] ID tidak ditemukan.")
                        else:
                            print("\n[ERROR] ID harus berupa angka.")
                            
                    elif sub_up == "2":
                        for p in pets:
                            print(f"ID: {p[0]} | Nama: {p[1]} | Jenis: {p[2]} | Usia: {p[3]} | Kelamin: {p[4]}")
                        id_edt = input("\nMasukkan ID hewan yang ingin diedit: ")
                        
                        valid_id = True
                        for k in id_edt:
                            if k < '0' or k > '9':
                                valid_id = False
                                break
                                
                        if valid_id and id_edt != "":
                            id_e = int(id_edt)
                            ketemu = False
                            for p in pets:
                                if p[0] == id_e:
                                    ketemu = True
                                    print(f"Mengedit data: {p[1]}")
                                    p[1] = input("Nama baru (kosongkan jika tetap): ") or p[1]
                                    p[2] = input("Jenis baru (kosongkan jika tetap): ") or p[2]
                                    p[3] = input("Usia baru (kosongkan jika tetap): ") or p[3]
                                    p[4] = input("Kelamin baru (kosongkan jika tetap): ") or p[4]
                                    print("\n[SUKSES] Profil hewan berhasil diperbarui!")
                                    break
                            if not ketemu:
                                print("\n[GAGAL] ID tidak ditemukan.")
                        else:
                            print("\n[ERROR] ID harus berupa angka.")
                    else:
                        print("[ERROR] Pilihan tidak valid.")
                    
                    input("\nTekan Enter untuk kembali...")

                elif menu_pilih == "4" and role_login == "admin":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("--- HAPUS DATA HEWAN (DELETE) ---")
                    for p in pets:
                        print(f"ID: {p[0]} | Nama: {p[1]} | Status: {p[5]}")
                    
                    id_del = input("\nMasukkan ID hewan yang ingin dihapus: ")
                    
                    valid_id = True
                    for k in id_del:
                        if k < '0' or k > '9':
                            valid_id = False
                            break
                            
                    if valid_id and id_del != "":
                        id_d = int(id_del)
                        index_hapus = -1
                        for i in range(len(pets)):
                            if pets[i][0] == id_d:
                                index_hapus = i
                                break
                        
                        if index_hapus != -1:
                            hewan_terhapus = pets.pop(index_hapus)
                            print(f"\n[SUKSES] Data hewan '{hewan_terhapus[1]}' berhasil dihapus.")
                        else:
                            print("\n[GAGAL] ID hewan tidak ditemukan.")
                    else:
                        print("\n[ERROR] ID harus berupa angka.")
                        
                    input("\nTekan Enter untuk kembali...")

                elif (menu_pilih == "5" and role_login == "admin") or (menu_pilih == "3" and role_login == "user"):
                    status_login = False
                    print("\n[INFO] Berhasil Logout.")
                    input("Tekan Enter untuk kembali ke menu utama...")
                else:
                    print("\n[ERROR] Pilihan menu tidak valid.")
                    input("Tekan Enter untuk melanjutkan...")
        else:
            print("\n[GAGAL] Username atau Password salah!")
            input("Tekan Enter untuk coba lagi...")

    elif pilihan_awal == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("--- REGISTER AKUN BARU ---")
        new_user = input("Buat Username baru: ")
        
        sudah_ada = False
        for u in users:
            if u[0] == new_user:
                sudah_ada = True
                break
        
        if sudah_ada:
            print("\n[GAGAL] Username sudah digunakan, silakan gunakan yang lain.")
        elif new_user == "":
            print("\n[GAGAL] Username tidak boleh kosong.")
        else:
            new_pass = input("Buat Password baru: ")
            if new_pass == "":
                print("\n[GAGAL] Password tidak boleh kosong.")
            else:
                users.append([new_user, new_pass, "user"])
                print("\n[SUKSES] Akun berhasil didaftarkan! Silakan login.")
        input("\nTekan Enter untuk kembali ke menu utama...")

    elif pilihan_awal == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Terima kasih telah menggunakan sistem adopsi hewan!")
        break
    else:
        print("\n[ERROR] Pilihan tidak valid.")
        input("Tekan Enter untuk melanjutkan...")