komponen_1 = 120000
komponen_2 = 135000
komponen_3 = 150000
komponen_4 = 175000
komponen_5 = 200000
komponen_6 = 220000

biaya_admin = 15000
nim = 86

harga_komponen = [
  komponen_1, komponen_2, komponen_3, komponen_4, komponen_5, komponen_6,
]

total_biaya = (
    komponen_1 + komponen_2 + komponen_3 + komponen_4 + komponen_5 + komponen_6 + biaya_admin
)

rata_rata = total_biaya / len(harga_komponen)

bolean = nim != rata_rata

kurs_gbp = 20000
total_biaya_gbp = total_biaya / kurs_gbp

slice_komponen = harga_komponen[-6:-2]

print("=== PROGRAM PERHITUNGAN BIAYA ROKET MAS ELON MUSK ===")
print("Daftar Harga Komponen     :", harga_komponen)
print("Total Biaya               : Rp", total_biaya)
print("Total Biaya dalam GBP     :", total_biaya_gbp)
print("Rata-rata Biaya           :", rata_rata)
print("2 Digit NIM               :", nim)
print("Hasil Bolean              :", bolean)
print("Slice Komponen 1 sampai 4 :", slice_komponen,
)