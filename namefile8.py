# kelipatan
def cetak(a, b):
    for item in range(a, b):
        if item % 2 == 0:
            if item % 5 == 0:
                if item % 100 == 0:
                    print("%i. Genap Kelipatan Seratus" % (item))
                else:
                    print("%i. Genap Kelipatan Lima" % (item))
            else:
                print("%i. Genap" % (item))
        else:
            if item % 5 == 0:
                print("%i. Ganjil Kelipatan Lima" % (item))
            else:
                print("%i. Ganjil" % (item))


cetak(1, 200)
