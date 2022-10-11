import unittest
import bears
import base_convert

class test_cases(unittest.TestCase):
    def test_bear_07_test_value_210(self):
         self.assertTrue(bears.bears(210))

    def test_bear_08_test_all_values_0_to_10000(self):
        values = []
        for val in range(0, 10000):
            if bears.bears(val):
                print(val)

    def test_base16_02(self):
         self.assertEqual(base_convert.convert(11259375, 16), "ABCDEF")

    def test_base_all_01(self):
        for i in range(2,17):
            for j in range(0,min(i,10)):
                self.assertEqual(base_convert.convert(j,i),str(j))
            for k in range(10,i):
                self.assertEqual(base_convert.convert(k,i),chr(65+k-10))

    def test_bear_10_test_all_values_0_to_50000(self):
            values = []
            for val in range(200000, 205000):
                bears.bears(val)