import unittest
from codename import CodeUnit as CU


class TestJumlahKarakter(unittest.TestCase):
    """docstring for TestJumlahKarakter"""
    # Ini untuk nomor 1

    def test_jumlah_karakter_saya(self):
        self.assertEqual(CU.jumlah_karakter('saya'), 4)

    def test_jumlah_karakter_lari(self):
        self.assertEqual(CU.jumlah_karakter('lari pagi'), 9)

    # Ini untuk nomor 2

    def test_grade_30(self):
        self.assertEqual(CU.grade(30), 'E')

    def test_grade_75(self):
        self.assertEqual(CU.grade(75), 'C')

    def test_error_grade(self):
        self.assertRaises(ValueError, CU.grade, 'tiga puluh')

    # Ini untuk nomor 3
    def test_ganjil_genap_43(self):
        self.assertEqual(CU.ganjil_genap(43), 'Ganjil')

    def test_ganjil_genap_1032(self):
        self.assertEqual(CU.ganjil_genap(1032), 'Genap')

    def test_error_ganjil_genap(self):
        self.assertRaises(ValueError, CU.ganjil_genap, 'tiga puluh')

    # Ini untuk nomor 4

    def test_kabisat_1900(self):
        self.assertEqual(CU.tahun_kabisat(1900), 'Bukan Kabisat')

    def test_kabisat_2000(self):
        self.assertEqual(CU.tahun_kabisat(2000), 'Kabisat')

    def test_kabisat_2001(self):
        self.assertEqual(CU.tahun_kabisat(2001), 'Bukan Kabisat')

    def test_kabisat_2016(self):
        self.assertEqual(CU.tahun_kabisat(2016), 'Kabisat')

    def test_error_kabisat(self):
        self.assertRaises(ValueError, CU.tahun_kabisat, 'tiga puluh')

    # Ini untuk nomor 5

    def test_kategori_film_15(self):
        self.assertEqual(CU.kategori_film_rating(15), 'Remaja')

    def test_kategori_film_32(self):
        self.assertEqual(CU.kategori_film_rating(32), 'Dewasa')

    def test_error_kategori_film(self):
        self.assertRaises(ValueError, CU.kategori_film_rating, 'tiga puluh')

    # Ini untuk nomor 6
    def test_loop_with_range(self):
        self.assertEqual(CU.range_angka(4, 8), '4, 5, 6, 7, 8')

    def test_error_loop_with_range(self):
        self.assertRaises(ValueError, CU.range_angka, '4', '8')

    # Ini untuk nomor 7
    def test_ganjil(self):
        myData = list(filter(lambda x: x % 2 == 1, range(1, 100)))
        self.assertListEqual(myData, CU.ganjil(1, 100))

    # Ini untuk nomor 8
    def test_ganjil_genap_kelipatan(self):
        self.assertListEqual(CU.ganjil_genap_kelipatan(
            1, 1000), CU.ganjil_genap_kelipatan(1, 1000))

    # Ini untuk nomor 9
    def test_membalikkan_kata(self):
        self.assertEqual(CU.membalikkan_kata(
            'saya ingin makan nasi goreng'), 'goreng nasi makan ingin saya')

    # Ini untuk nomor 10
    def test_add_to_array(self):
        self.assertEqual(CU.add_to_array(['Meja', 'Buku', 'Topi', 'Baju', 'Kayu'], 'Handuk', 'Celana'), [
                         'Handuk', 'Meja', 'Buku', 'Topi', 'Baju', 'Kayu', 'Celana'])


if __name__ == '__main__':
    unittest.main()
