import starter_funcs as sf
import unittest


class TestEuler(unittest.TestCase):
    # Test Euler 1
    def test_euler1_01(self):
        self.assertTrue(type(sf.euler1()) == int)

    def test_euler1_02(self):
        self.assertTrue(sf.euler1() == 233168)

    def test_euler1_03(self):
        self.assertEqual(sf.euler1(10), 23)

    # Test Euler 2
    def test_euler2_01(self):
        self.assertTrue(type(sf.euler2()) == int)

    def test_euler2_02(self):
        self.assertTrue(sf.euler2() == 4613732)

    def test_euler2_03(self):
        self.assertEqual(sf.euler2(10), 10)

    # Test Euler 3
    def test_euler3_01(self):
        self.assertTrue(type(sf.euler3()) == int)

    def test_euler3_02(self):
        self.assertTrue(sf.euler3() == 6857)

    def test_euler3_03(self):
        self.assertEqual(sf.euler3(1234567), 9721)

    def test_euler3_04(self):
        self.assertEqual(sf.euler3(0), 0)

    # Test Euler 4
    def test_euler4_01(self):
        self.assertTrue(type(sf.euler4()) == int)

    def test_euler4_02(self):
        self.assertTrue(sf.euler4() == 906609)

    # Test Euler 5
    def test_euler5_01(self):
        self.assertTrue(type(sf.euler5()) == int)

    def test_euler5_02(self):
        self.assertTrue(sf.euler5() == 232792560)

    def test_euler5_03(self):
        self.assertEqual(sf.euler5(10), 2520)

    # Test Euler 6
    def test_euler6_01(self):
        self.assertTrue(type(sf.euler6()) == int)

    def test_euler6_02(self):
        self.assertTrue(sf.euler6() == 25164150)

    def test_euler6_03(self):
        self.assertEqual(sf.euler6(10), 2640)

    # Test Euler 7
    def test_euler7_01(self):
        self.assertTrue(type(sf.euler7()) == int)

    def test_euler7_02(self):
        self.assertTrue(sf.euler7() == 104743)

    def test_euler7_03(self):
        self.assertEqual(sf.euler7(10), 29)

    # Test Euler 8
    def test_euler8_01(self):
        self.assertTrue(type(sf.euler8()) == int)

    def test_euler8_02(self):
        self.assertTrue(sf.euler8() == 23514624000)

    def test_euler8_03(self):
        self.assertEqual(sf.euler8(4), 5832)

    # Test Euler 9
    def test_euler9_01(self):
        self.assertTrue(type(sf.euler9()) == int)

    def test_euler9_02(self):
        self.assertTrue(sf.euler9() == 31875000)

    def test_euler9_03(self):
        self.assertEqual(sf.euler9(12), 60)

    # Test Euler 10
    def test_euler10_01(self):
        self.assertTrue(type(sf.euler10()) == int)

    def test_euler10_02(self):
        self.assertTrue(sf.euler10() == 142913828922)

    def test_euler10_03(self):
        self.assertEqual(sf.euler10(10), 17)

    # Test Euler 11
    def test_euler11_01(self):
        self.assertTrue(type(sf.euler11()) == int)

    def test_euler11_02(self):
        self.assertTrue(sf.euler11() == 70600674)

    # Test Euler 12
    def test_euler12_01(self):
        self.assertTrue(type(sf.euler12()) == int)

    def test_euler12_02(self):
        self.assertTrue(sf.euler12() == 76576500)

    def test_euler12_03(self):
        self.assertEqual(sf.euler12(5), 28)

    # Test Euler 13
    def test_euler13_01(self):
        self.assertTrue(type(sf.euler13()) == str)

    def test_euler13_02(self):
        self.assertTrue(sf.euler13() == "5537376230")

    def test_euler13_03(self):
        self.assertEqual(sf.euler13(5), "55373")

    # Test Euler 14
    def test_euler14_01(self):
        self.assertTrue(type(sf.euler14()) == int)

    def test_euler14_02(self):
        self.assertTrue(sf.euler14() == 837799)

    def test_euler14_03(self):
        self.assertEqual(sf.euler14(20), 18)

    # Test Euler 15
    def test_euler15_01(self):
        self.assertTrue(type(sf.euler15()) == int)

    def test_euler15_02(self):
        self.assertTrue(sf.euler15() == 137846528820)

    def test_euler15_03(self):
        self.assertEqual(sf.euler15(10), 184756)

    # Test Euler 16
    def test_euler16_01(self):
        self.assertTrue(type(sf.euler16()) == int)

    def test_euler16_02(self):
        self.assertTrue(sf.euler16() == 1366)

    def test_euler16_03(self):
        self.assertEqual(sf.euler16(100), 115)

    # Test Euler 17
    def test_euler17_01(self):
        self.assertTrue(type(sf.euler17()) == int)

    def test_euler17_02(self):
        self.assertTrue(sf.euler17() == 21124)

    def test_euler17_03(self):
        self.assertEqual(sf.euler17(342), 6117)

    # Test Euler 18, given problem
    def test_euler18_01(self):
        self.assertTrue(type(sf.euler18()) == int)

    def test_euler18_02(self):
        self.assertTrue(sf.euler18() == 1074)

    # Test Euler 19
    def test_euler19_01(self):
        self.assertTrue(type(sf.euler19()) == int)

    def test_euler19_02(self):
        self.assertTrue(sf.euler19() == 171)

    def test_euler19_03(self):
        self.assertEqual(sf.euler19(2001), 173)


if __name__ == "__main__":
    unittest.main()
