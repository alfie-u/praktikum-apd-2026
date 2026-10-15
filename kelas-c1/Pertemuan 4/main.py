# nilai = [75, 60, 80, 90, 50]
# for elemen in nilai:
#   if elemen >= 70:
#     print(f"Lulus dengan nilai {elemen}")
#   else:
#     print(f"Tidak lulus nilai {elemen}")

# for i in range(1, 11):
#   print(i)

# for i in range(5, 0, -1):
#   print(f"Angka ke-{i}")

# for i in range(2):
#   for j in range(3):
#     print(f"{i} x {j} = {i*j}")

# jawab = "ya"
# hitung = 0

# while(jawab == "ya"):
#   hitung += 1
#   jawab = input("Mau Lanjut? ")

# print(f"Total Perulangan : {hitung}")

# for i in range(4):
#   print(i)
#   break

# i = 0
# while True:
#   print(i)
#   i += 1
#   if i >= 11:
#     break

for i in range(10):
  if i % 2 == 0:
    continue
  print(i)