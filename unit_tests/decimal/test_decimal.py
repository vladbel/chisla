"""Module docstring"""
import unittest
import decimal as dcml

class TestDecimal(unittest.TestCase):
    """Class docstring bbb"""

    def test_addition_1(self):
        """Function docstring"""
        value_1 = dcml.Decimal('100')
        value_2 = dcml.Decimal('0.001')
        expected_sum = dcml.Decimal('100.001')
        calculated_sum = value_1 + value_2
        self.assertTrue(expected_sum == calculated_sum)

    def test_addition_2(self):
        """Function docstring"""
        dcml.getcontext().prec = 6
        value_1 = dcml.Decimal(100)
        value_2 = dcml.Decimal(0.001)

        expected_sum = dcml.Decimal('100.001')

        calculated_sum = value_1 + value_2
        self.assertTrue(expected_sum == calculated_sum)

    def test_addition_3(self):
        """this will fail - not enough precision"""
        dcml.getcontext().prec = 6
        value_1 = dcml.Decimal(100)
        value_2 = dcml.Decimal(0.0001)

        expected_sum = dcml.Decimal('100.0001')

        calculated_sum = value_1 + value_2 # 100.000
        self.assertTrue(expected_sum > calculated_sum)

    def test_multiplication_1(self):
        """Function docstring"""
        dcml.getcontext().prec = 6

        value_1 = dcml.Decimal(10000)
        value_2 = dcml.Decimal(0.0001)

        expected_result = dcml.Decimal('1')
        calculated_result = value_1 * value_2

        self.assertTrue(
            expected_result == calculated_result,
            "expected: " + str(expected_result) + "; actual: " + str(calculated_result))

    def test_decimal_to_int_multiplication(self):
        value_1 = 2
        value_2 = dcml.Decimal(11.01)
        result = dcml.Decimal(value_1) * value_2
        result = result.quantize(dcml.Decimal('0.01'))
        self.assertTrue(result == dcml.Decimal('22.02'))




if __name__ == '__main__':
    unittest.main()
