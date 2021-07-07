from euler_funcs import *
import unittest

class TestEuler(unittest.TestCase):
    #Test Euler 1
        def test_euler1_01(self):
            self.assertTrue(type(euler1()) == int)

        def test_euler1_02(self):
            self.assertTrue(euler1() == 233168)

        def test_euler1_03(self):
            self.assertEqual(euler1(10), 23)

    #Test Euler 2
        def test_euler2_01(self):
            self.assertTrue(type(euler2()) == int)

        def test_euler2_02(self):
            self.assertTrue(euler2() == 4613732)

        def test_euler2_03(self):
            self.assertEqual(euler2(10), 10)

    #Test Euler 3
        def test_euler3_01(self):
            self.assertTrue(type(euler3()) == int)

        def test_euler3_02(self):
            self.assertTrue(euler3() == 6857)

        def test_euler3_03(self):
            self.assertEqual(euler3(1234567), 9721)

        def test_euler3_04(self):
            self.assertEqual(euler3(0), 0)

    #Test Euler 4
        def test_euler4_01(self):
            self.assertTrue(type(euler4()) == int)

        def test_euler4_02(self):
            self.assertTrue(euler4() == 906609)

    #Test Euler 5
        def test_euler5_01(self):
            self.assertTrue(type(euler5()) == int)

        def test_euler5_02(self):
            self.assertTrue(euler5() == 232792560)

        def test_euler5_03(self):
            self.assertEqual(euler5(10), 2520)
    
    #Test Euler 6
        def test_euler6_01(self):
            self.assertTrue(type(euler6()) == int)

        def test_euler6_02(self):
            self.assertTrue(euler6() == 25164150)

        def test_euler6_03(self):
            self.assertEqual(euler6(10), 2640)

    #Test Euler 7
        def test_euler7_01(self):
            self.assertTrue(type(euler7()) == int)

        def test_euler7_02(self):
            self.assertTrue(euler7() == 104743)

        def test_euler7_03(self):
            self.assertEqual(euler7(10), 29)

    #Test Euler 8
        def test_euler8_01(self):
            self.assertTrue(type(euler8()) == int)

        def test_euler8_02(self):
            self.assertTrue(euler8() == 23514624000)

        def test_euler8_03(self):
            self.assertEqual(euler8(4), 5832)

    #Test Euler 9
        def test_euler9_01(self):
            self.assertTrue(type(euler9()) == int)

        def test_euler9_02(self):
            self.assertTrue(euler9() == 31875000)

        def test_euler9_03(self):
            self.assertEqual(euler9(12), 60)

    #Test Euler 10
        def test_euler10_01(self):
            self.assertTrue(type(euler10()) == int)

        def test_euler10_02(self):
            self.assertTrue(euler10() == 142913828922)

        def test_euler10_03(self):
            self.assertEqual(euler10(10), 17)

if __name__ == "__main__":
        unittest.main()
