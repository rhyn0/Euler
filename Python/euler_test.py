from typing import ClassVar, List
import euler_funcs as euler
import unittest


class TestEuler1(unittest.TestCase):
    num = euler.euler1()

    def test_euler1_01(self):
        self.assertTrue(type(TestEuler1.num) == int)

    def test_euler1_02(self):
        self.assertTrue(TestEuler1.num == 233168)

    def test_euler1_03(self):
        self.assertEqual(euler.euler1(10), 23)


class TestEuler2(unittest.TestCase):
    num = euler.euler2()

    def test_euler2_01(self):
        self.assertTrue(type(TestEuler2.num) == int)

    def test_euler2_02(self):
        self.assertTrue(TestEuler2.num == 4613732)

    def test_euler2_03(self):
        self.assertEqual(euler.euler2(10), 10)


class TestEuler3(unittest.TestCase):
    num = euler.euler3()

    def test_euler3_01(self):
        self.assertTrue(type(TestEuler3.num) == int)

    def test_euler3_02(self):
        self.assertTrue(TestEuler3.num == 6857)

    def test_euler3_03(self):
        self.assertEqual(euler.euler3(1234567), 9721)

    def test_euler3_04(self):
        self.assertEqual(euler.euler3(0), 0)


class TestEuler4(unittest.TestCase):
    num = euler.euler4()

    def test_euler4_01(self):
        self.assertTrue(type(TestEuler4.num) == int)

    def test_euler4_02(self):
        self.assertTrue(TestEuler4.num == 906609)


class TestEuler5(unittest.TestCase):
    num = euler.euler5()

    def test_euler5_01(self):
        self.assertTrue(type(TestEuler5.num) == int)

    def test_euler5_02(self):
        self.assertTrue(TestEuler5.num == 232792560)

    def test_euler5_03(self):
        self.assertEqual(euler.euler5(10), 2520)


class TestEuler6(unittest.TestCase):
    num = euler.euler6()

    def test_euler6_01(self):
        self.assertTrue(type(TestEuler6.num) == int)

    def test_euler6_02(self):
        self.assertTrue(TestEuler6.num == 25164150)

    def test_euler6_03(self):
        self.assertEqual(euler.euler6(10), 2640)


class TestEuler7(unittest.TestCase):
    num = euler.euler7()

    def test_euler7_01(self):
        self.assertTrue(type(TestEuler7.num) == int)

    def test_euler7_02(self):
        self.assertTrue(TestEuler7.num == 104743)

    def test_euler7_03(self):
        self.assertEqual(euler.euler7(10), 29)


class TestEuler8(unittest.TestCase):
    num = euler.euler8()

    def test_euler8_01(self):
        self.assertTrue(type(TestEuler8.num) == int)

    def test_euler8_02(self):
        self.assertTrue(TestEuler8.num == 23514624000)

    def test_euler8_03(self):
        self.assertEqual(euler.euler8(4), 5832)


class TestEuler9(unittest.TestCase):
    num = euler.euler9()

    def test_euler9_01(self):
        self.assertEqual(type(TestEuler9.num), int)

    def test_euler9_02(self):
        self.assertTrue(TestEuler9.num == 31875000)

    def test_euler9_03(self):
        self.assertEqual(euler.euler9(12), 60)


class TestEuler10(unittest.TestCase):
    num = euler.euler10()

    def test_euler10_01(self):
        self.assertTrue(type(TestEuler10.num) == int)

    def test_euler10_02(self):
        self.assertEqual(TestEuler10.num, 42913828922)

    def test_euler10_03(self):
        self.assertEqual(euler.euler10(10), 17)


class TestEuler11(unittest.TestCase):
    def test_euler11_01(self):
        self.assertTrue(type(euler.euler11()) == int)

    def test_euler11_02(self):
        self.assertEqual(euler.euler11(), 70600674)


class TestEuler12(unittest.TestCase):
    def test_euler12_01(self):
        self.assertTrue(type(euler.euler12()) == int)

    def test_euler12_02(self):
        self.assertTrue(euler.euler12() == 76576500)

    def test_euler12_03(self):
        self.assertEqual(euler.euler12(5), 28)


class TestEuler13(unittest.TestCase):
    def test_euler13_01(self):
        self.assertTrue(type(euler.euler13()) == int)

    def test_euler13_02(self):
        self.assertTrue(euler.euler13() == 5537376230)

    def test_euler13_03(self):
        self.assertEqual(euler.euler13(5), 55373)


class TestEuler14(unittest.TestCase):
    def test_euler14_01(self):
        self.assertTrue(type(euler.euler14()) == int)

    def test_euler14_02(self):
        self.assertTrue(euler.euler14() == 837799)

    def test_euler14_03(self):
        self.assertEqual(euler.euler14(20), 18)


class TestEuler15(unittest.TestCase):
    def test_euler15_01(self):
        self.assertTrue(type(euler.euler15()) == int)

    def test_euler15_02(self):
        self.assertTrue(euler.euler15() == 137846528820)

    def test_euler15_03(self):
        self.assertEqual(euler.euler15(10), 184756)


class TestEuler16(unittest.TestCase):
    def test_euler16_01(self):
        self.assertTrue(type(euler.euler16()) == int)

    def test_euler16_02(self):
        self.assertTrue(euler.euler16() == 1366)

    def test_euler16_03(self):
        self.assertEqual(euler.euler16(100), 115)


class TestEuler17(unittest.TestCase):
    def test_euler17_01(self):
        self.assertTrue(type(euler.euler17()) == int)

    def test_euler17_02(self):
        self.assertTrue(euler.euler17() == 21124)

    def test_euler17_03(self):
        self.assertEqual(euler.euler17(342), 6117)


class TestEuler18(unittest.TestCase):
    def test_euler18_01(self):
        self.assertTrue(type(euler.euler18()) == int)

    def test_euler18_02(self):
        self.assertTrue(euler.euler18() == 1074)


class TestEuler19(unittest.TestCase):
    def test_euler19_01(self):
        self.assertTrue(type(euler.euler19()) == int)

    def test_euler19_02(self):
        self.assertEqual(euler.euler19(), 171)

    def test_euler19_03(self):
        self.assertEqual(euler.euler19(2001), 173)


class TestEuler20(unittest.TestCase):
    def test_euler20_type(self):
        self.assertEqual(type(euler.euler20()), int)

    def test_euler20_val(self):
        self.assertEqual(euler.euler20(), 648)

    def test_euler20_ex(self):
        self.assertEqual(euler.euler20(10), 27)


class TestEuler21(unittest.TestCase):
    def test_euler21_type(self):
        self.assertEqual(type(euler.euler21()), int)

    def test_euler21_val(self):
        self.assertEqual(euler.euler21(), 31626)

    def test_euler21_ex(self):
        self.assertEqual(euler.euler21(10), 0)


class TestEuler22(unittest.TestCase):
    def test_euler22_type(self):
        self.assertEqual(type(euler.euler22()), int)

    def test_euler22_val(self):
        self.assertEqual(euler.euler22(), 871198282)


class TestEuler23(unittest.TestCase):
    num = euler.euler23()

    def test_euler23_type(self):
        self.assertEqual(type(TestEuler23.num), int)

    def test_euler23_val(self):
        self.assertEqual(TestEuler23.num, 4179871)

    def test_euler23_ex(self):
        self.assertEqual(euler.euler23(1000), 240492)


class TestEuler24(unittest.TestCase):
    num = euler.euler24()

    def test_euler23_type(self):
        self.assertEqual(type(TestEuler24.num), int)

    def test_euler23_val(self):
        self.assertEqual(TestEuler24.num, 2783915460)

    def test_euler23_ex(self):
        self.assertEqual(euler.euler24(100), 123495786)


def run_classes(classes: List):
    # Run only the tests in the specified classes

    loader = unittest.TestLoader()

    suites_list = [loader.loadTestsFromTestCase(cls) for cls in classes]

    big_suite = unittest.TestSuite(suites_list)

    runner = unittest.TextTestRunner()
    runner.run(big_suite)


if __name__ == "__main__":
    unittest.main()
    # run_classes([TestEuler1])
