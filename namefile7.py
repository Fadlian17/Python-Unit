# Ganjil

batasan = int(input('Masukkan Batasan Angka : '))

for a in range(2, batasan, 1):
    mod = 1
    for b in range(2, a, 1):
        if (a % b == 0):
            mod = 0

    if (mod == 1):
        print(a)
