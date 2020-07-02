import unittest
from codename import examCode as EC


class SoalTest(unittest.TestCase):
    def test_satu(self):
        self.assertEqual(EC.satu1("saya"), 4)
        self.assertIsNotNone(EC.satu1("saya"))

    def test_dua(self):
        self.assertEqual(EC.dua2(90), "A")
        self.assertIsNotNone(EC.dua2(85))

    def test_tiga(self):
        self.assertEqual(EC.tiga3(43), "Ganjil")
        self.assertIsNotNone(EC.tiga3(45))

    def test_empat(self):
        self.assertEqual(EC.empat4(1900), "Bukan Tahun Kabisat")
        self.assertIsNotNone(EC.empat4(2000))

    def test_lima(self):
        self.assertEqual(EC.lima5(21), "Dewasa")
        self.assertIsNotNone(EC.lima5(19))

    def test_enam(self):
        self.assertEqual(EC.enam6(4, 8), [4, 5, 6, 7, 8])
        self.assertIsNotNone(EC.enam6(1, 10))

    def test_tujuh(self):
        self.assertIn(11, EC.tujuh7())
        self.assertIsNotNone(EC.tujuh7())

    def test_delapan(self):
        self.assertEqual(EC.delapan8(), EC.delapan8())
        self.assertIsNone(EC.delapan8())

    def test_sembilan(self):
        self.assertEqual(EC.sembilan9("saya ingin makan nasi goreng"),
                         "goreng nasi makan ingin saya")

    def test_sepuluh(self):
        self.assertIn('Handuk', EC.sepuluh10())
        self.assertIsNotNone(EC.sepuluh10())


if __name__ == '__main__':
    unittest.main()
