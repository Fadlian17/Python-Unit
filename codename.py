# class CodeUnit():

#     """Code unit test"""
#     # soal 1
#     @staticmethod
#     def satu1(karakters):
#         return len(karakters)

#     # soal 2
#     @staticmethod
#     def dua2(score):
#         if score in range(90, 100):
#             return "A"
#         elif score in range(80, 90):
#             return "B"
#         elif score in range(70, 80):
#             return "C"
#         elif score in range(60, 70):
#             return "D"
#         elif score in range(0, 60):
#             return "E"

#     # soal dua
#     @staticmethod
#     def grade(nilai):
#         if type(nilai) == int:
#             return CodeUnit.dua2(nilai)
#         else:
#             raise ValueError('Inputan harus angka')

#     # soal tiga
#     def tiga3(nilai):
#         data = {0: 'Genap', 1: 'Ganjil'}
#         return data[nilai % 2]

#     @staticmethod
#     def ganjil_genap(nilai):
#         if type(nilai) == int:
#             return CodeUnit.tiga3(nilai)
#         else:
#             raise ValueError('Inputan harus angka')

#     # soal empat

#     def empat4(tahun):
#         if tahun % 400 == 0:
#             return "Kabisat"
#         elif tahun % 100 == 0:
#             return "Bukan Kabisat"
#         elif tahun % 4 == 0:
#             return "Kabisat"
#         else:
#             return "Bukan Kabisat"

#     @staticmethod
#     def tahun_kabisat(tahun):
#         if type(tahun) == int:
#             return CodeUnit.empat4(tahun)
#         else:
#             raise ValueError('Inputan harus angka')

#     @staticmethod
#     def lima5(film):
#         film = int(input("Rating sebuah Film = "))

#         if (film >= 21):
#             print("Khusus DEWASA")

#         elif (film >= 13):
#             print("Khusus Remaja")

#         elif (film >= 9):
#             print("Bimbingan Orang tua")

#         elif (film < 9):
#             print("Semua Usia")

#     @staticmethod
#     def kategori_film_rating(film):
#         if type(film) == int:
#             return CodeUnit.lima5(film)
#         else:
#             raise ValueError('Inputan harus angka')

#     # soal 6

#     def enam6(a, b):
#         output = []
#         for x in range(a, b+1):
#             output.append(str(x))
#         return output

#     @staticmethod
#     def range_angka(a, b):
#         if type(a) == int and type(b) == int:
#             return ', '.join(CodeUnit.enam6(a, b)[0:len(CodeUnit.enam6(a, b))])
#         else:
#             raise ValueError('Inputan harus angka')

#     # soal 7
#     @staticmethod
#     def tujuh7(a, b):
#         return list(filter(lambda x: x % 2 == 1, range(a, b)))

#     # soal 8

#     @staticmethod
#     def delapan8(a, b):
#         def cetak(a, b):
#             datas = []
#             for item in range(a, b):
#                 if item % 2 == 0:
#                     if item % 5 == 0:
#                         if item % 100 == 0:
#                             datas.append(
#                                 "%i. Genap Kelipatan Seratus" % (item))
#                         else:
#                             datas.append("%i. Genap Kelipatan Lima" % (item))
#                     else:
#                         datas.append("%i. Genap" % (item))
#                 else:
#                     if item % 5 == 0:
#                         datas.append("%i. Ganjil Kelipatan Lima" % (item))
#                     else:
#                         datas.append("%i. Ganjil" % (item))
#             return datas

#     # soal 9
#     @staticmethod
#     def sembilan9(sentence):
#         string = sentence.split()
#         print(' '.join(string[::-1]))

#     # soal 10
#     @staticmethod
#     def sepuluh10(datas, awal, akhir):
#         datas = datas
#         datas.insert(0, awal)
#         datas.insert(len(datas)+1, akhir)
#         return datas


# if __name__ == "__main__":
#     tes = CodeUnit()
#     print(CodeUnit.dua2(39))
#     print(CodeUnit.empat4(2004))
#     print(CodeUnit.lima5(9))
#     print(CodeUnit.enam6(4, 8))
#     print(CodeUnit.tujuh7(1, 100))
#     print("\n")
#     print(CodeUnit.delapan8(1, 10))
#     print("\n")
#     print(CodeUnit.sembilan9('saya ingin makan nasi goreng'))
#     print(CodeUnit.sepuluh10(
#         ['Meja', 'Buku', 'Topi', 'Baju', 'Kayu'], 'Handuk', 'Celana'))
#     print("Result OK")

class examCode:
    @staticmethod
    def satu1(var):
        string = var
        total = 0

        for x in string:
            total = total + 1
        return total

    @staticmethod
    def dua2(var):
        nilai = var

        if nilai >= 90:
            return "A"
        elif (nilai >= 80) and (nilai <= 89):
            return "B"
        elif (nilai >= 70) and (nilai <= 79):
            return "C"
        elif (nilai >= 60) and (nilai <= 69):
            return "D"
        elif nilai <= 59:
            return "E"
        else:
            return "Tidak termasuk dalam kategori"

    @staticmethod
    def tiga3(var):
        bilangan = var

        if bilangan % 2 == 0:
            return "Genap"
        else:
            return "Ganjil"

    @staticmethod
    def empat4(var):
        tahun = var

        if tahun % 4 == 0:
            if tahun % 100 == 0:
                if tahun % 400 == 0:
                    return "Tahun Kabisat"
                else:
                    return "Bukan Tahun Kabisat"
            else:
                return "Tahun Kabisat"
        else:
            return "Bukan Tahun Kabisat"

    @staticmethod
    def lima5(var):
        ratingFilms = var
        if ratingFilms >= 21:
            return "Dewasa"
        elif ratingFilms >= 13:
            return "Remaja"
        elif ratingFilms >= 9:
            return "BIMBINGAN ORANG TUA"
        elif ratingFilms < 9:
            return "SEMUA USIA"

    @staticmethod
    def enam6(var1, var2):
        bil = []
        lbal1 = var1
        lbal2 = var2
        lbal3 = lbal2+1
        rentangAngka = range(lbal1, lbal3)

        for i in rentangAngka:
            bil.append(i)
        return bil

    @staticmethod
    def tujuh7():
        prime = list()
        for x in range(1, 100):
            if x % 2 == 1:
                prime.append(x)
            else:
                pass
        return prime

    @staticmethod
    def delapan8():
        for i in range(1, 1001):
            if (i % 2) == 1:
                if (i % 5) == 0:
                    if __name__ == "__main__":
                        print(i, "Ganjil kelipatan 5")
                else:
                    if __name__ == "__main__":
                        print(i, "Ganjil")
            elif (i % 2) == 0:
                if (i % 5) == 0:
                    if (i % 100) == 0:
                        if __name__ == "__main__":
                            print(i, "kelipatan 100")
                    else:
                        if __name__ == "__main__":
                            print(i, "Genap kelipatan 5")
                else:
                    if __name__ == "__main__":
                        print(i, "Genap")

    @staticmethod
    def sembilan9(var):
        text = var
        pish = text.split()
        rev = " ".join(reversed(pish))
        return rev

    @staticmethod
    def sepuluh10():
        stuff = ['Meja', 'Buku', 'Topi', 'Baju', 'Kayu']

        stuff.insert(0, "Handuk")

        stuff.insert(6, "Celana")

        return stuff
