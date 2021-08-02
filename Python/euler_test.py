from typing import List
import euler_funcs as euler
import unittest


class TestEuler1(unittest.TestCase):
    def setUp(self) -> None:
        self.num = euler.euler1()

    def test_euler1_01(self):
        self.assertTrue(type(self.num) == int)

    def test_euler1_02(self):
        self.assertEqual(self.num, 233168)

    def test_euler1_03(self):
        self.assertEqual(euler.euler1(10), 23)


class TestEuler2(unittest.TestCase):
    def setUp(self) -> None:
        self.num = euler.euler2()

    def test_euler2_01(self):
        self.assertTrue(type(self.num) == int)

    def test_euler2_02(self):
        self.assertEqual(self.num, 4613732)

    def test_euler2_03(self):
        self.assertEqual(euler.euler2(10), 10)


class TestEuler3(unittest.TestCase):
    def setUp(self) -> None:
        self.num = euler.euler3()

    def test_euler3_01(self):
        self.assertTrue(type(self.num) == int)

    def test_euler3_02(self):
        self.assertEqual(self.num, 6857)

    def test_euler3_03(self):
        self.assertEqual(euler.euler3(1234567), 9721)

    def test_euler3_04(self):
        self.assertEqual(euler.euler3(0), 0)


class TestEuler4(unittest.TestCase):
    def setUp(self) -> None:
        self.num = euler.euler4()

    def test_euler4_01(self):
        self.assertTrue(type(self.num) == int)

    def test_euler4_02(self):
        self.assertEqual(self.num, 906609)


class TestEuler5(unittest.TestCase):
    def setUp(self) -> None:
        self.num = euler.euler5()

    def test_euler5_01(self):
        self.assertTrue(type(self.num) == int)

    def test_euler5_02(self):
        self.assertTrue(self.num == 232792560)

    def test_euler5_03(self):
        self.assertEqual(euler.euler5(10), 2520)


class TestEuler6(unittest.TestCase):
    def setUp(self) -> None:
        self.num = euler.euler6()

    def test_euler6_01(self):
        self.assertTrue(type(self.num) == int)

    def test_euler6_02(self):
        self.assertTrue(self.num == 25164150)

    def test_euler6_03(self):
        self.assertEqual(euler.euler6(10), 2640)


class TestEuler7(unittest.TestCase):
    def setUp(self) -> None:
        self.num = euler.euler7()

    def test_euler7_01(self):
        self.assertTrue(type(self.num) == int)

    def test_euler7_02(self):
        self.assertTrue(self.num == 104743)

    def test_euler7_03(self):
        self.assertEqual(euler.euler7(10), 29)


class TestEuler8(unittest.TestCase):
    def setUp(self) -> None:
        self.num = euler.euler8()

    def test_euler8_01(self):
        self.assertTrue(type(self.num) == int)

    def test_euler8_02(self):
        self.assertTrue(self.num == 23514624000)

    def test_euler8_03(self):
        self.assertEqual(euler.euler8(4), 5832)


class TestEuler9(unittest.TestCase):
    def setUp(self) -> None:
        self.num = euler.euler9()

    def test_euler9_01(self):
        self.assertEqual(type(self.num), int)

    def test_euler9_02(self):
        self.assertTrue(self.num == 31875000)

    def test_euler9_03(self):
        self.assertEqual(euler.euler9(12), 60)


class TestEuler10(unittest.TestCase):
    def setUp(self) -> None:
        self.num = euler.euler10()

    def test_euler10_01(self):
        self.assertTrue(type(self.num) == int)

    def test_euler10_02(self):
        self.assertEqual(self.num, 142913828922)

    def test_euler10_03(self):
        self.assertEqual(euler.euler10(10), 17)


class TestEuler11(unittest.TestCase):
    """Test largest product in a grid

    Even though problem data is given, size to multiply can change
    """

    def setUp(self) -> None:
        self.num = euler.euler11()

    def test_euler11_01(self):
        self.assertTrue(type(self.num) == int)

    def test_euler11_02(self):
        self.assertEqual(self.num, 70600674)

    def test_euler11_ex(self):
        self.assertEqual(euler.euler11(5), 3318231678)


class TestEuler12(unittest.TestCase):
    def setUp(self) -> None:
        self.num = euler.euler12()

    def test_euler12_01(self):
        self.assertTrue(type(self.num) == int)

    def test_euler12_02(self):
        self.assertTrue(self.num == 76576500)

    def test_euler12_03(self):
        self.assertEqual(euler.euler12(5), 28)


class TestEuler13(unittest.TestCase):
    def setUp(self) -> None:
        self.num = euler.euler13()

    def test_euler13_01(self):
        self.assertTrue(type(self.num) == int)

    def test_euler13_02(self):
        self.assertTrue(self.num == 5537376230)

    def test_euler13_03(self):
        self.assertEqual(euler.euler13(5), 55373)


class TestEuler14(unittest.TestCase):
    def setUp(self) -> None:
        self.num = euler.euler14()

    def test_euler14_01(self):
        self.assertTrue(type(self.num) == int)

    def test_euler14_02(self):
        self.assertTrue(self.num == 837799)

    def test_euler14_03(self):
        self.assertEqual(euler.euler14(20), 18)


class TestEuler15(unittest.TestCase):
    def setUp(self) -> None:
        self.num = euler.euler15()

    def test_euler15_01(self):
        self.assertTrue(type(self.num) == int)

    def test_euler15_02(self):
        self.assertTrue(self.num == 137846528820)

    def test_euler15_03(self):
        self.assertEqual(euler.euler15(10), 184756)


class TestEuler16(unittest.TestCase):
    def setUp(self) -> None:
        self.num = euler.euler16()

    def test_euler16_01(self):
        self.assertTrue(type(self.num) == int)

    def test_euler16_02(self):
        self.assertTrue(self.num == 1366)

    def test_euler16_03(self):
        self.assertEqual(euler.euler16(100), 115)


class TestEuler17(unittest.TestCase):
    def setUp(self) -> None:
        self.num = euler.euler17()

    def test_euler17_01(self):
        self.assertTrue(type(self.num) == int)

    def test_euler17_02(self):
        self.assertTrue(self.num == 21124)

    def test_euler17_03(self):
        self.assertEqual(euler.euler17(342), 6117)


class TestEuler18(unittest.TestCase):
    # given a predefined set of paths
    def setUp(self) -> None:
        self.num = euler.euler18()

    def test_euler18_01(self):
        self.assertTrue(type(self.num) == int)

    def test_euler18_02(self):
        self.assertTrue(self.num == 1074)


class TestEuler19(unittest.TestCase):
    def setUp(self) -> None:
        self.num = euler.euler19()

    def test_euler19_01(self):
        self.assertTrue(type(self.num) == int)

    def test_euler19_02(self):
        self.assertEqual(self.num, 171)

    def test_euler19_03(self):
        self.assertEqual(euler.euler19(2001), 173)


class TestEuler20(unittest.TestCase):
    def setUp(self) -> None:
        self.num = euler.euler20()

    def test_euler20_type(self):
        self.assertEqual(type(self.num), int)

    def test_euler20_val(self):
        self.assertEqual(self.num, 648)

    def test_euler20_ex(self):
        self.assertEqual(euler.euler20(10), 27)


class TestEuler21(unittest.TestCase):
    def setUp(self) -> None:
        self.num = euler.euler21()

    def test_euler21_type(self):
        self.assertEqual(type(self.num), int)

    def test_euler21_val(self):
        self.assertEqual(self.num, 31626)

    def test_euler21_ex(self):
        self.assertEqual(euler.euler21(10), 0)


class TestEuler22(unittest.TestCase):
    # given a data file, so no extra
    def setUp(self) -> None:
        self.num = euler.euler22()

    def test_euler22_type(self):
        self.assertEqual(type(self.num), int)

    def test_euler22_val(self):
        self.assertEqual(self.num, 871198282)


class TestEuler23(unittest.TestCase):
    def setUp(self) -> None:
        self.num = euler.euler23()

    def test_euler23_type(self):
        self.assertEqual(type(self.num), int)

    def test_euler23_val(self):
        self.assertEqual(self.num, 4179871)

    def test_euler23_ex(self):
        self.assertEqual(euler.euler23(1000), 240492)


class TestEuler24(unittest.TestCase):
    def setUp(self) -> None:
        self.num = euler.euler24()

    def test_euler24_type(self):
        self.assertEqual(type(self.num), int)

    def test_euler24_val(self):
        self.assertEqual(self.num, 2783915460)

    def test_euler24_ex(self):
        self.assertEqual(euler.euler24(100), 123495786)


class TestEuler25(unittest.TestCase):
    def setUp(self) -> None:
        self.num = euler.euler25()

    def test_euler25_type(self):
        self.assertEqual(type(self.num), int)

    def test_euler25_val(self):
        self.assertEqual(self.num, 4782)

    def test_euler25_ex(self):
        self.assertEqual(euler.euler25(3), 12)


class TestEuler26(unittest.TestCase):
    def setUp(self) -> None:
        self.num = euler.euler26()

    def test_euler26_type(self):
        self.assertEqual(type(self.num), int)

    def test_euler26_val(self):
        self.assertEqual(self.num, 983)

    def test_euler26_ex(self):
        self.assertEqual(euler.euler26(493), 491)


class TestEuler27(unittest.TestCase):
    def setUp(self) -> None:
        self.num = euler.euler27()

    def test_euler27_type(self):
        self.assertEqual(type(self.num), int)

    def test_euler27_val(self):
        self.assertEqual(self.num, -59231)

    def test_euler27_ex(self):
        self.assertEqual(euler.euler27(543), -21629)


class TestEuler28(unittest.TestCase):
    def setUp(self) -> None:
        self.num = euler.euler28()

    def test_euler28_type(self):
        self.assertEqual(type(self.num), int)

    def test_euler28_val(self):
        self.assertEqual(self.num, 669171001)

    def test_euler28_ex(self):
        self.assertEqual(euler.euler28(56789), 122097603702357)


class TestEuler29(unittest.TestCase):
    def setUp(self) -> None:
        self.num = euler.euler29()

    def test_euler29_type(self):
        self.assertEqual(type(self.num), int)

    def test_euler29_val(self):
        self.assertEqual(self.num, 9183)

    def test_euler29_ex(self):
        self.assertEqual(euler.euler29(204), 39339)


class TestEuler30(unittest.TestCase):
    # this function won't take a param, due to specifically calculated limit
    def setUp(self) -> None:
        self.num = euler.euler30()

    def test_euler30_type(self):
        self.assertEqual(type(self.num), int)

    def test_euler30_val(self):
        self.assertEqual(self.num, 443839)

    def test_euler30_ex(self):
        self.assertEqual(euler.euler30(4), 19316)


class TestEuler31(unittest.TestCase):
    # this function won't take a param, due to specifically calculated limit
    def setUp(self) -> None:
        self.num = euler.euler31()

    def test_euler31_type(self):
        self.assertEqual(type(self.num), int)

    def test_euler31_val(self):
        self.assertEqual(self.num, 73682)

    def test_euler31_ex(self):
        self.assertEqual(euler.euler31(10), 11)


class TestEuler32(unittest.TestCase):
    # this function won't take a param, due to specifically calculated limit
    def setUp(self) -> None:
        self.num = euler.euler32()

    def test_euler32_type(self):
        self.assertEqual(type(self.num), int)

    def test_euler32_val(self):
        self.assertEqual(self.num, 45228)

    def test_euler32_ex(self):
        self.assertEqual(euler.euler32(10), 11)


class TestEuler33(unittest.TestCase):
    # this function won't take a param, due to specifically calculated limit
    def setUp(self) -> None:
        self.num = euler.euler33()

    def test_euler33_type(self):
        self.assertEqual(type(self.num), int)

    def test_euler33_val(self):
        self.assertEqual(self.num, 100)


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
