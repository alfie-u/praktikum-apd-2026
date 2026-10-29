import os

users = {
    "admin": ["admin123", "admin"],
    "alfie": ["123", "user"]
}

pets = {
    1: {"nama": "Milo", "jenis": "Kucing", "usia": "2 Tahun", "kelamin": "Jantan", "status": "Belum Diadopsi"},
    2: {"nama": "Luna", "jenis": "Anjing", "usia": "1 Tahun", "kelamin": "Betina", "status": "Belum Diadopsi"},
    3: {"nama": "Leo", "jenis": "Kucing", "usia": "3 Tahun", "kelamin": "Jantan", "status": "Sudah Diadopsi"}
}

status_login = False
role_login = ""
user_aktif = ""

STATUS_BELUM = "Belum Diadopsi"
STATUS_SUDAH = "Sudah Diadopsi"

def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_header(judul):
    garis = "=" * 45
    print(garis)
    print(f"  {judul}")
    print(garis)

def jeda(pesan="Tekan Enter untuk kembali..."):
    input(f"\n{pesan}")

def cetak_hewan(id_pet, data, dengan_status=True):
    baris = (f"ID: {id_pet} | Nama: {data['nama']} | Jenis: {data['jenis']} | "
             f"Usia: {data['usia']} | Kelamin: {data['kelamin']}")
    if dengan_status:
        baris += f" | Status: {data['status']}"
    print(baris)

def generate_id_baru():
    if len(pets) == 0:
        return 1
    return max(pets.keys()) + 1

def hitung_total_hewan():
    total = len(pets)
    return total

def input_angka(pesan):
    try:
        angka = int(input(pesan))
    except ValueError:
        print("\n[ERROR] Input yang Anda masukkan bukan angka (integer)!")
        return None
    else:
        return angka
    finally:
        pass

def cek_login(username, password):
    try:
        data_user = users[username]
    except KeyError:
        return None
    else:
        if data_user[0] == password:
            return data_user[1]
        return None

def ambil_hewan(id_pet):
    try:
        return pets[id_pet]
    except KeyError:
        return None

def hitung_status_rekursif(daftar_id, status, indeks=0):
    if indeks == len(daftar_id):
        return 0
    cocok = 1 if pets[daftar_id[indeks]]["status"] == status else 0
    return cocok + hitung_status_rekursif(daftar_id, status, indeks + 1)

def validasi_username(username):
    if username == "":
        raise ValueError("Username tidak boleh kosong.")
    if len(username) < 5:
        raise ValueError("Username minimal memiliki 5 karakter.")
    if username in users:
        raise ValueError("Username sudah digunakan, silakan gunakan yang lain.")

def validasi_password(password):
    if password == "":
        raise ValueError("Password tidak boleh kosong.")
    if len(password) < 5:
        raise ValueError("Password minimal memiliki 5 karakter.")

def validasi_teks(teks, nama_field):
    if teks.strip() == "":
        raise ValueError(f"{nama_field} tidak boleh kosong.")

def menu_register():
    bersihkan_layar()
    print("--- REGISTER AKUN BARU ---")
    try:
        username_baru = input("Buat Username baru: ")
        validasi_username(username_baru)
        password_baru = input("Buat Password baru: ")
        validasi_password(password_baru)
    except ValueError as e:
        print(f"\n[GAGAL] {e}")
    else:
        users[username_baru] = [password_baru, "user"]
        print("\n[SUKSES] Akun berhasil didaftarkan! Silakan login.")
    finally:
        jeda("Tekan Enter untuk kembali ke menu utama...")

def menu_login():
    global status_login, role_login, user_aktif

    bersihkan_layar()
    print("--- MENU LOGIN ---")
    username_input = input("Masukkan Username: ")
    password_input = input("Masukkan Password: ")

    role = cek_login(username_input, password_input)
    if role is None:
        print("\n[GAGAL] Username atau Password salah!")
        jeda("Tekan Enter untuk coba lagi...")
        return

    user_aktif = username_input
    role_login = role
    status_login = True
    print(f"\n[SUKSES] Selamat datang, {user_aktif} ({role_login})!")
    jeda("Tekan Enter untuk masuk ke menu utama...")

def logout():
    global status_login, role_login, user_aktif
    status_login = False
    role_login = ""
    user_aktif = ""
    print("\n[INFO] Berhasil Logout.")
    jeda("Tekan Enter untuk kembali ke menu utama...")

def lihat_hewan():
    bersihkan_layar()
    print("--- DAFTAR HEWAN PELIHARAAN ---")
    print("1. Tampilkan Semua Hewan")
    print("2. Cari Berdasarkan Nama")
    print("3. Filter Berdasarkan Status")
    sub_read = input("Pilih opsi (1-3): ")

    if sub_read == "1":
        print("\n--- Seluruh Hewan ---")
        if hitung_total_hewan() == 0:
            print("Belum ada data hewan.")
        else:
            for id_pet, data in pets.items():
                cetak_hewan(id_pet, data)
            daftar_id = list(pets.keys())
            belum = hitung_status_rekursif(daftar_id, STATUS_BELUM)
            sudah = hitung_status_rekursif(daftar_id, STATUS_SUDAH)
            print(f"\nTotal: {hitung_total_hewan()} | {STATUS_BELUM}: {belum} | {STATUS_SUDAH}: {sudah}")

    elif sub_read == "2":
        cari_nama = input("\nMasukkan nama hewan yang dicari: ")
        ditemukan = False
        for id_pet, data in pets.items():
            if data['nama'].lower() == cari_nama.lower():
                print("\n[DITEMUKAN]")
                cetak_hewan(id_pet, data)
                ditemukan = True
                break
        if not ditemukan:
            print("\n[INFO] Hewan dengan nama tersebut tidak ditemukan.")

    elif sub_read == "3":
        print("\nPilih Status:")
        print("1. Belum Diadopsi")
        print("2. Sudah Diadopsi")
        pilih_status = input("Pilih (1/2): ")
        if pilih_status == "1":
            target_status = STATUS_BELUM
        elif pilih_status == "2":
            target_status = STATUS_SUDAH
        else:
            print("\n[ERROR] Pilihan tidak valid.")
            jeda()
            return

        print(f"\n--- Daftar Hewan: {target_status} ---")
        ada = False
        for id_pet, data in pets.items():
            if data['status'] == target_status:
                cetak_hewan(id_pet, data, dengan_status=False)
                ada = True
        if not ada:
            print("Tidak ada hewan dengan status tersebut.")
    else:
        print("\n[ERROR] Pilihan tidak valid.")

    jeda()

def tambah_hewan():
    bersihkan_layar()
    print("--- TAMBAH DATA HEWAN BARU ---")
    id_baru = generate_id_baru()

    try:
        nama = input("Masukkan Nama Hewan: ")
        validasi_teks(nama, "Nama hewan")
        jenis = input("Masukkan Jenis Hewan (Kucing/Anjing): ")
        validasi_teks(jenis, "Jenis hewan")
        usia = input("Masukkan Usia Hewan (Contoh: 2 Tahun): ")
        validasi_teks(usia, "Usia hewan")
        kelamin = input("Masukkan Jenis Kelamin (Jantan/Betina): ")
        validasi_teks(kelamin, "Jenis kelamin")
        if kelamin.lower() not in ("jantan", "betina"):
            raise ValueError("Jenis kelamin harus 'Jantan' atau 'Betina'.")
    except ValueError as e:
        print(f"\n[GAGAL] {e}")
    else:
        pets[id_baru] = {
            "nama": nama,
            "jenis": jenis,
            "usia": usia,
            "kelamin": kelamin.capitalize(),
            "status": STATUS_BELUM
        }
        print(f"\n[SUKSES] Data hewan '{nama}' berhasil ditambahkan dengan ID {id_baru}!")
    finally:
        jeda()

def ajukan_adopsi():
    bersihkan_layar()
    print("--- AJUKAN ADOPSI HEWAN ---")
    tersedia = False
    for id_pet, data in pets.items():
        if data['status'] == STATUS_BELUM:
            cetak_hewan(id_pet, data, dengan_status=False)
            tersedia = True

    if not tersedia:
        print("Saat ini tidak ada hewan yang tersedia untuk diadopsi.")
        jeda()
        return

    id_pilih = input_angka("\nMasukkan ID hewan yang ingin diadopsi: ")
    if id_pilih is not None:
        data = ambil_hewan(id_pilih)
        if data is not None and data['status'] == STATUS_BELUM:
            data['status'] = STATUS_SUDAH
            print(f"\n[SUKSES] Selamat! Anda berhasil mengajukan adopsi untuk {data['nama']}.")
        else:
            print("\n[GAGAL] ID hewan tidak ditemukan atau sudah diadopsi.")
    jeda()

def ubah_status_hewan():
    for id_pet, data in pets.items():
        print(f"ID: {id_pet} | Nama: {data['nama']} | Status: {data['status']}")
    id_up = input_angka("\nMasukkan ID hewan yang ingin diubah statusnya: ")
    if id_up is None:
        return

    data = ambil_hewan(id_up)
    if data is None:
        print("\n[GAGAL] ID tidak ditemukan.")
        return
    if data['status'] == STATUS_BELUM:
        data['status'] = STATUS_SUDAH
    else:
        data['status'] = STATUS_BELUM
    print(f"\n[SUKSES] Status hewan {data['nama']} diubah menjadi: {data['status']}")

def edit_profil_hewan():
    for id_pet, data in pets.items():
        cetak_hewan(id_pet, data, dengan_status=False)
    id_edit = input_angka("\nMasukkan ID hewan yang ingin diedit: ")
    if id_edit is None:
        return

    data = ambil_hewan(id_edit)
    if data is None:
        print("\n[GAGAL] ID tidak ditemukan.")
        return

    print(f"Mengedit data: {data['nama']}")
    data['nama'] = input("Nama baru (kosongkan jika tetap): ") or data['nama']
    data['jenis'] = input("Jenis baru (kosongkan jika tetap): ") or data['jenis']
    data['usia'] = input("Usia baru (kosongkan jika tetap): ") or data['usia']
    data['kelamin'] = input("Kelamin baru (kosongkan jika tetap): ") or data['kelamin']
    print("\n[SUKSES] Profil hewan berhasil diperbarui!")

def ubah_data():
    bersihkan_layar()
    print("--- UPDATE DATA / STATUS HEWAN ---")
    print("1. Ubah Status Adopsi Hewan")
    print("2. Perbaiki Profil (Salah Ketik)")
    sub_up = input("Pilih opsi (1/2): ")

    if sub_up == "1":
        ubah_status_hewan()
    elif sub_up == "2":
        edit_profil_hewan()
    else:
        print("\n[ERROR] Pilihan tidak valid.")
    jeda()

def hapus_hewan():
    bersihkan_layar()
    print("--- HAPUS DATA HEWAN (DELETE) ---")
    for id_pet, data in pets.items():
        print(f"ID: {id_pet} | Nama: {data['nama']} | Status: {data['status']}")

    id_del = input_angka("\nMasukkan ID hewan yang ingin dihapus: ")
    if id_del is not None:
        try:
            hewan_terhapus = pets.pop(id_del)
        except KeyError:
            print("\n[GAGAL] ID hewan tidak ditemukan.")
        else:
            print(f"\n[SUKSES] Data hewan '{hewan_terhapus['nama']}' berhasil dihapus.")
    jeda()

def tampilkan_menu_dashboard():
    bersihkan_layar()
    tampilkan_header(f"DASHBOARD ADOPSI HEWAN [{role_login.upper()}]")
    print("1. Lihat Daftar Hewan")
    if role_login == "admin":
        print("2. Tambah Data Hewan")
        print("3. Ubah Data / Status Hewan")
        print("4. Hapus Data Hewan")
        print("5. Logout")
    else:
        print("2. Ajukan Adopsi Hewan")
        print("3. Logout")
    print("-" * 45)

def dashboard():
    while status_login:
        tampilkan_menu_dashboard()
        menu_pilih = input("Pilih menu: ")

        if menu_pilih == "1":
            lihat_hewan()
        elif menu_pilih == "2" and role_login == "admin":
            tambah_hewan()
        elif menu_pilih == "2" and role_login == "user":
            ajukan_adopsi()
        elif menu_pilih == "3" and role_login == "admin":
            ubah_data()
        elif menu_pilih == "4" and role_login == "admin":
            hapus_hewan()
        elif (menu_pilih == "5" and role_login == "admin") or (menu_pilih == "3" and role_login == "user"):
            logout()
        else:
            print("\n[ERROR] Pilihan menu tidak valid.")
            jeda("Tekan Enter untuk melanjutkan...")

def tampilkan_menu_awal():
    bersihkan_layar()
    tampilkan_header("APLIKASI ADOPSI HEWAN PELIHARAAN")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    print("-" * 45)

def main():
    try:
        while True:
            tampilkan_menu_awal()
            pilihan_awal = input("Pilih menu (1-3): ")

            if pilihan_awal == "1":
                menu_login()
                if status_login:
                    dashboard()
            elif pilihan_awal == "2":
                menu_register()
            elif pilihan_awal == "3":
                break
            else:
                print("\n[ERROR] Pilihan tidak valid.")
                jeda("Tekan Enter untuk melanjutkan...")
    except KeyboardInterrupt:
        print("\n\n[INFO] Program dihentikan paksa oleh pengguna (Ctrl+C).")
    except EOFError:
        print("\n\n[INFO] Input terputus, program dihentikan.")
    finally:
        print("Terima kasih telah menggunakan sistem adopsi hewan!")

if __name__ == "__main__":
    main()