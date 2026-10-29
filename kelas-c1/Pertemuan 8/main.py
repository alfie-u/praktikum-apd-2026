# from prettytable import PrettyTable
# # Membuat objek tabel dan menentukan nama-nama kolom
# tabel = PrettyTable()
# tabel.field_names = ["NIM", "Nama Mahasiswa", "Prodi"]
# # Menambahkan satu baris data ke dalam tabel
# tabel.add_row(["2609106001", "Andi Alarice", "Informatika"])
# # Menambahkan beberapa baris data sekaligus menggunakan list di dalam list
# tabel.add_rows([
# ["2609106002", "Hammam Nopal", "Informatika"],
# ["2609106003", "Abimar LLM", "Sistem Informasi"]
# ])
# # Mengatur perataan teks pada kolom tertentu ('l' = kiri, 'c' = tengah, 'r'= kanan)
# tabel.align["Nama Mahasiswa"] = "l"
# print(tabel)


# import random
# # Menghasilkan satu bilangan bulat acak dari 1 sampai 5 (inklusif)
# print(random.randint(1, 5))
# # Memilih 1 elemen acak dari list atau string
# buah = ["pisang", "rambutan", "manggis"]
# huruf = "abcd"
# print(random.choice(buah)) # memilih 1 item acak pada list
# print(random.choice(huruf)) # memilih 1 karakter acak pada string
# # Menyusun 4 angka PIN acak menggunakan perulangan
# kumpulan_angka = "0123456789"
# pin_acak = ""
# for i in range(4):
#   pin_acak += random.choice(kumpulan_angka)
# print(pin_acak)
# # Mengacak urutan elemen di dalam list secara langsung
# kartu = ["As Wajik", "3 Hati", "7 Sekop"]
# random.shuffle(kartu)
# print(kartu)


import inquirer
# Menyusun daftar pertanyaan menu
pertanyaan = [
inquirer.List(
"menu",
message="Pilih menu aplikasi",
choices=["Tambah Data", "Lihat Data", "Keluar"],
),
]
# Menampilkan prompt di terminal dan menyimpan hasil pilihan
jawaban = inquirer.prompt(pertanyaan)
print(jawaban) # Output berupa Dictionary, misal: {'menu': 'Tambah Data'}
print(jawaban["menu"]) # Mengambil nilai berdasarkan key 'menu': Tambah Data