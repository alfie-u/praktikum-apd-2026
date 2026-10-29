# # angka = {1, 2, 3, 6}
# prima = {2, 3, 5, 7}
# # print(angka.difference(prima))
# # print(prima - angka)

# prima.add(11)
# print(prima)


# aset = {
# "jenis" : "rumah",
# "harga" : 120000000,
# "alamat" : "Jl. Raya No. 1",
# "berpenghuni" : True,
# "luas" : "120m x 80m"
# }
# print(aset)
# aset.clear()
# print(aset)
# # Output
# {'jenis': 'rumah', 'harga': 120000000, 'alamat': 'Jl. Raya No. 1',
# 'berpenghuni': True, 'luas': '120m x 80m'}
# {}

key = "ayam geprek", "ayam goreng", "ayam bakar",
value = 12000
menu = dict.fromkeys(key, value)

print(menu)
# Output
{'ayam geprek': 12000, 'ayam goreng': 12000, 'ayam bakar': 12000}