import unittest

import plang


class TestPlangMethod(unittest.TestCase):

    def test_invalid_parameter(self):
        with self.assertRaises(TypeError):
            plang.convert_number_to_thai_word('any string')

    def test_small_number(self):
        self.assertEqual(plang.convert_number_to_thai_word(0), 'ศูนย์')
        self.assertEqual(plang.convert_number_to_thai_word(1), 'หนึ่ง')
        self.assertEqual(plang.convert_number_to_thai_word(2), 'สอง')
        self.assertEqual(plang.convert_number_to_thai_word(3), 'สาม')
        self.assertEqual(plang.convert_number_to_thai_word(4), 'สี่')
        self.assertEqual(plang.convert_number_to_thai_word(5), 'ห้า')
        self.assertEqual(plang.convert_number_to_thai_word(6), 'หก')
        self.assertEqual(plang.convert_number_to_thai_word(7), 'เจ็ด')
        self.assertEqual(plang.convert_number_to_thai_word(8), 'แปด')
        self.assertEqual(plang.convert_number_to_thai_word(9), 'เก้า')

    def test_ten(self):
        self.assertEqual(plang.convert_number_to_thai_word(10), 'สิบ')
        self.assertEqual(plang.convert_number_to_thai_word(11), 'สิบเอ็ด')
        self.assertEqual(plang.convert_number_to_thai_word(12), 'สิบสอง')
        self.assertEqual(plang.convert_number_to_thai_word(20), 'ยี่สิบ')
        self.assertEqual(plang.convert_number_to_thai_word(22), 'ยี่สิบสอง')
        self.assertEqual(plang.convert_number_to_thai_word(30), 'สามสิบ')

    def test_hundred(self):
        self.assertEqual(plang.convert_number_to_thai_word(100), 'หนึ่งร้อย')
        self.assertEqual(
            plang.convert_number_to_thai_word(111),
            'หนึ่งร้อยสิบเอ็ด')
        self.assertEqual(
            plang.convert_number_to_thai_word(121),
            'หนึ่งร้อยยี่สิบเอ็ด')

    def test_million(self):
        self.assertEqual(
            plang.convert_number_to_thai_word(1000000),
            'หนึ่งล้าน')
        self.assertEqual(
            plang.convert_number_to_thai_word(1000001),
            'หนึ่งล้านเอ็ด')
        self.assertEqual(
            plang.convert_number_to_thai_word(1000002),
            'หนึ่งล้านสอง')
        self.assertEqual(
            plang.convert_number_to_thai_word(1200000),
            'หนึ่งล้านสองแสน')

    def test_negative_number(self):
        self.assertEqual(plang.convert_number_to_thai_word(-1), 'ลบหนึ่ง')

    def test_more_than_million(self):
        self.assertEqual(
            plang.convert_number_to_thai_word(10000000),
            'สิบล้าน'
        )
        self.assertEqual(
            plang.convert_number_to_thai_word(11000000),
            'สิบเอ็ดล้าน'
        )
        self.assertEqual(
            plang.convert_number_to_thai_word(11000000),
            'สิบเอ็ดล้าน'
        )
        self.assertEqual(
            plang.convert_number_to_thai_word(1000000000),
            'หนึ่งพันล้าน'
        )
        self.assertEqual(
            plang.convert_number_to_thai_word(-1000000000),
            'ลบหนึ่งพันล้าน'
        )


if __name__ == '__main__':
    unittest.main()
