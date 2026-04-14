import math

c = 3e8
vmax = 0.00064 * c
N = 500

dt = 1.0

with open("zaman_kaymasi 500lük.csv", "w") as file:
    file.write("beta(v/c),gamma,dt_prime\n")

    for i in range(N + 1):
        v = (vmax * i) / N
        beta = v / c

        gamma = 1.0 / math.sqrt(1 - beta**2)
        dt_prime = gamma * dt

        file.write(f"{beta},{gamma},{dt_prime}\n")

print("csv dosyası oluşturuldu")