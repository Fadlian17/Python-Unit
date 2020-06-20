# Kabisat
tahun = int(input("Masukkan Data tahun: "))
if (tahun % 4) == 0:
    if (tahun % 100) == 0:
        if (tahun % 400) == 0:
            print("{0} merupakan tahun kabisat".format(tahun))
        else:
            print("{0} bukan merupakan tahun kabisat".format(tahun))
    else:
        print("{0} merupakan tahun kabisat".format(tahun))
else:
    print("{0} bukan merupakan tahun kabisat".format(tahun))
