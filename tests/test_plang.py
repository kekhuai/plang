import unittest

from plang import plang


class TestPlangMethod(unittest.TestCase):

    def test_invalid_parameter(self):
        with self.assertRaises(TypeError):
            plang.to_thai('any string')

    def test_small_number(self):
        self.assertEqual(plang.to_thai(0), 'ศูนย์')
        self.assertEqual(plang.to_thai(1), 'หนึ่ง')
        self.assertEqual(plang.to_thai(2), 'สอง')
        self.assertEqual(plang.to_thai(3), 'สาม')
        self.assertEqual(plang.to_thai(4), 'สี่')
        self.assertEqual(plang.to_thai(5), 'ห้า')
        self.assertEqual(plang.to_thai(6), 'หก')
        self.assertEqual(plang.to_thai(7), 'เจ็ด')
        self.assertEqual(plang.to_thai(8), 'แปด')
        self.assertEqual(plang.to_thai(9), 'เก้า')

    def test_ten(self):
        self.assertEqual(plang.to_thai(10), 'สิบ')
        self.assertEqual(plang.to_thai(11), 'สิบเอ็ด')
        self.assertEqual(plang.to_thai(12), 'สิบสอง')
        self.assertEqual(plang.to_thai(20), 'ยี่สิบ')
        self.assertEqual(plang.to_thai(22), 'ยี่สิบสอง')
        self.assertEqual(plang.to_thai(30), 'สามสิบ')

    def test_hundred(self):
        self.assertEqual(plang.to_thai(100), 'หนึ่งร้อย')
        self.assertEqual(plang.to_thai(111), 'หนึ่งร้อยสิบเอ็ด')
        self.assertEqual(plang.to_thai(121), 'หนึ่งร้อยยี่สิบเอ็ด')

    def test_million(self):
        self.assertEqual(plang.to_thai(1000000), 'หนึ่งล้าน')
        self.assertEqual(plang.to_thai(1000001), 'หนึ่งล้านเอ็ด')
        self.assertEqual(plang.to_thai(1000002), 'หนึ่งล้านสอง')
        self.assertEqual(plang.to_thai(1200000), 'หนึ่งล้านสองแสน')

    def test_negative_number(self):
        self.assertEqual(plang.to_thai(-1), 'ลบหนึ่ง')

    def test_more_than_million(self):
        self.assertEqual(plang.to_thai(10000000), 'สิบล้าน')
        self.assertEqual(plang.to_thai(11000000), 'สิบเอ็ดล้าน')
        self.assertEqual(plang.to_thai(11000000), 'สิบเอ็ดล้าน')
        self.assertEqual(plang.to_thai(1000000000), 'หนึ่งพันล้าน')
        self.assertEqual(plang.to_thai(-1000000000), 'ลบหนึ่งพันล้าน')


if __name__ == '__main__':
    unittest.main()
