import math
import csv

veri_sayisi = 5000

# Mach değerleri (0 - 10 arası mesela)
mach_degerleri = [i * 10 / veri_sayisi for i in range(veri_sayisi)]

ses_hizi = 343          # m/s
isik_hizi = 3e8         # m/s

sonuclar = []

for M in mach_degerleri:
    x = (M * ses_hizi) / isik_hizi
    gamma = 1 / math.sqrt(1 - x**2)
    sonuclar.append([M, x, gamma])

with open("mach_zaman_kaymasi.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Mach", "v/c", "gamma"])
    writer.writerows(sonuclar)

print("Dosya oluşturuldu: mach_zaman_kaymasi.csv")