import os

# Struktur Data Menggunakan Dictionary
# users: key adalah username, value adalah list/dictionary berisi [password, role]
users = {
    "admin": ["admin123", "admin"],
    "alfie": ["123", "user"]
}

# pets: key adalah ID hewan (integer), value adalah dictionary detail hewan
pets = {
    1: {"nama": "Milo", "jenis": "Kucing", "usia": "2 Tahun", "kelamin": "Jantan", "status": "Belum Diadopsi"},
    2: {"nama": "Luna", "jenis": "Anjing", "usia": "1 Tahun", "kelamin": "Betina", "status": "Belum Diadopsi"},
    3: {"nama": "Leo", "jenis": "Kucing", "usia": "3 Tahun", "kelamin": "Jantan", "status": "Sudah Diadopsi"}
}

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
        # Mengakses dictionary users menggunakan perulangan for dan .items()
        for uname, detail in users.items():
            if uname == username_input and detail[0] == password_input:
                login_sukses = True
                role_login = detail[1]
                user_aktif = uname
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
  
                # --- MENU 1: READ ---
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
                            for id_pet, p in pets.items():
                                print(f"ID: {id_pet} | Nama: {p['nama']} | Jenis: {p['jenis']} | Usia: {p['usia']} | Kelamin: {p['kelamin']} | Status: {p['status']}")
                    
                    elif sub_read == "2":
                        cari_nama = input("\nMasukkan nama hewan yang dicari: ")
                        ditemukan = False
                        for id_pet, p in pets.items():
                            if p['nama'].lower() == cari_nama.lower():
                                print(f"\n[DITEMUKAN] ID: {id_pet} | Nama: {p['nama']} | Jenis: {p['jenis']} | Usia: {p['usia']} | Kelamin: {p['kelamin']} | Status: {p['status']}")
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
                        for id_pet, p in pets.items():
                            if p['status'] == target_status:
                                print(f"ID: {id_pet} | Nama: {p['nama']} | Jenis: {p['jenis']} | Usia: {p['usia']} | Kelamin: {p['kelamin']}")
                                ada = True
                        if not ada:
                            print("Tidak ada hewan dengan status tersebut.")
                    else:
                        print("[ERROR] Pilihan tidak valid.")
                    
                    input("\nTekan Enter untuk kembali ke menu...")

                # --- MENU 2 (Admin): CREATE ---
                elif menu_pilih == "2" and role_login == "admin":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("--- TAMBAH DATA HEWAN BARU ---")
                    
                    # Menentukan ID baru secara otomatis untuk dictionary
                    if len(pets) == 0:
                        id_baru = 1
                    else:
                        id_baru = max(pets.keys()) + 1
                        
                    nama = input("Masukkan Nama Hewan: ")
                    jenis = input("Masukkan Jenis Hewan (Kucing/Anjing): ")
                    usia = input("Masukkan Usia Hewan (Contoh: 2 Tahun): ")
                    kelamin = input("Masukkan Jenis Kelamin (Jantan/Betina): ")
                    status_awal = "Belum Diadopsi"

                    # Menyimpan data baru ke dalam dictionary pets menggunakan key id_baru
                    pets[id_baru] = {
                        "nama": nama,
                        "jenis": jenis,
                        "usia": usia,
                        "kelamin": kelamin,
                        "status": status_awal
                    }
                    
                    print(f"\n[SUKSES] Data hewan '{nama}' berhasil ditambahkan!")
                    input("\nTekan Enter untuk kembali...")

                # --- MENU 2 (User): AJUKAN ADOPSI ---
                elif menu_pilih == "2" and role_login == "user":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("--- AJUKAN ADOPSI HEWAN ---")
                    for id_pet, p in pets.items():
                        if p['status'] == "Belum Diadopsi":
                            print(f"ID: {id_pet} | Nama: {p['nama']} | Jenis: {p['jenis']} | Usia: {p['usia']} | Kelamin: {p['kelamin']}")
                    
                    id_pilih = input("\nMasukkan ID hewan yang ingin diadopsi: ")
                    
                    valid_id = True
                    for karakter in id_pilih:
                        if karakter < '0' or karakter > '9':
                            valid_id = False
                            break
                    
                    if valid_id and id_pilih != "":
                        id_angka = int(id_pilih)
                        # Pengecekan key di dalam dictionary pets
                        if id_angka in pets and pets[id_angka]['status'] == "Belum Diadopsi":
                            pets[id_angka]['status'] = "Sudah Diadopsi"
                            print("\n[SUKSES] Selamat! Anda berhasil mengajukan adopsi hewan.")
                        else:
                            print("\n[GAGAL] ID hewan tidak ditemukan atau sudah diadopsi.")
                    else:
                        print("\n[ERROR] Masukkan angka ID yang valid.")
                    
                    input("\nTekan Enter untuk kembali...")

                # --- MENU 3 (Admin): UPDATE ---
                elif menu_pilih == "3" and role_login == "admin":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("--- UPDATE DATA / STATUS HEWAN ---")
                    print("1. Ubah Status Adopsi Hewan")
                    print("2. Perbaiki Profil (Salah Ketik)")
                    sub_up = input("Pilih opsi (1/2): ")
                    
                    if sub_up == "1":
                        for id_pet, p in pets.items():
                            print(f"ID: {id_pet} | Nama: {p['nama']} | Status: {p['status']}")
                        id_up = input("\nMasukkan ID hewan yang ingin diubah statusnya: ")
                        
                        valid_id = True
                        for k in id_up:
                            if k < '0' or k > '9':
                                valid_id = False
                                break
                        
                        if valid_id and id_up != "":
                            id_a = int(id_up)
                            if id_a in pets:
                                if pets[id_a]['status'] == "Belum Diadopsi":
                                    pets[id_a]['status'] = "Sudah Diadopsi"
                                else:
                                    pets[id_a]['status'] = "Belum Diadopsi"
                                print(f"\n[SUKSES] Status hewan {pets[id_a]['nama']} diubah menjadi: {pets[id_a]['status']}")
                            else:
                                print("\n[GAGAL] ID tidak ditemukan.")
                        else:
                            print("\n[ERROR] ID harus berupa angka.")
                            
                    elif sub_up == "2":
                        for id_pet, p in pets.items():
                            print(f"ID: {id_pet} | Nama: {p['nama']} | Jenis: {p['jenis']} | Usia: {p['usia']} | Kelamin: {p['kelamin']}")
                        id_edt = input("\nMasukkan ID hewan yang ingin diedit: ")
                        
                        valid_id = True
                        for k in id_edt:
                            if k < '0' or k > '9':
                                valid_id = False
                                break
                                
                        if valid_id and id_edt != "":
                            id_e = int(id_edt)
                            if id_e in pets:
                                print(f"Mengedit data: {pets[id_e]['nama']}")
                                pets[id_e]['nama'] = input("Nama baru (kosongkan jika tetap): ") or pets[id_e]['nama']
                                pets[id_e]['jenis'] = input("Jenis baru (kosongkan jika tetap): ") or pets[id_e]['jenis']
                                pets[id_e]['usia'] = input("Usia baru (kosongkan jika tetap): ") or pets[id_e]['usia']
                                pets[id_e]['kelamin'] = input("Kelamin baru (kosongkan jika tetap): ") or pets[id_e]['kelamin']
                                print("\n[SUKSES] Profil hewan berhasil diperbarui!")
                            else:
                                print("\n[GAGAL] ID tidak ditemukan.")
                        else:
                            print("\n[ERROR] ID harus berupa angka.")
                    else:
                        print("[ERROR] Pilihan tidak valid.")
                    
                    input("\nTekan Enter untuk kembali...")

                # --- MENU 4 (Admin): DELETE ---
                elif menu_pilih == "4" and role_login == "admin":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("--- HAPUS DATA HEWAN (DELETE) ---")
                    for id_pet, p in pets.items():
                        print(f"ID: {id_pet} | Nama: {p['nama']} | Status: {p['status']}")
                    
                    id_del = input("\nMasukkan ID hewan yang ingin dihapus: ")
                    
                    valid_id = True
                    for k in id_del:
                        if k < '0' or k > '9':
                            valid_id = False
                            break
                            
                    if valid_id and id_del != "":
                        id_d = int(id_del)
                        # Menghapus item dari dictionary menggunakan metode del
                        if id_d in pets:
                            hewan_terhapus = pets.pop(id_d)
                            print(f"\n[SUKSES] Data hewan '{hewan_terhapus['nama']}' berhasil dihapus.")
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

    # --- MENU REGISTER ---
    elif pilihan_awal == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("--- REGISTER AKUN BARU ---")
        new_user = input("Buat Username baru: ")
        
        sudah_ada = False
        if new_user in users:
            sudah_ada = True
        
        if sudah_ada:
            print("\n[GAGAL] Username sudah digunakan, silakan gunakan yang lain.")
        elif new_user == "":
            print("\n[GAGAL] Username tidak boleh kosong.")
        else:
            new_pass = input("Buat Password baru: ")
            if new_pass == "":
                print("\n[GAGAL] Password tidak boleh kosong.")
            else:
                # Menambahkan akun baru ke dictionary users
                users[new_user] = [new_pass, "user"]
                print("\n[SUKSES] Akun berhasil didaftarkan! Silakan login.")
        input("\nTekan Enter untuk kembali ke menu utama...")

    elif pilihan_awal == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Terima kasih telah menggunakan sistem adopsi hewan!")
        break
    else:
        print("\n[ERROR] Pilihan tidak valid.")
        input("Tekan Enter untuk melanjutkan...")