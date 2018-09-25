import unittest
import decimal as dcml


class TestDecimal(unittest.TestCase):

    def test_addition_1(self): 
        
        value_1 = dcml.Decimal ('100')
        value_2 = dcml.Decimal ('0.001')
        expected_sum = dcml.Decimal ('100.001')

        calculated_sum = value_1 + value_2
        self.assertTrue( expected_sum == calculated_sum)

    def test_addition_2(self): 
        
        dcml.getcontext().prec = 6
        value_1 = dcml.Decimal (100)
        value_2 = dcml.Decimal (0.001)

        expected_sum = dcml.Decimal ('100.001')

        calculated_sum = value_1 + value_2
        self.assertTrue( expected_sum == calculated_sum)

    def test_addition_3(self): 
        
        # this will fail - not enough precision
        dcml.getcontext().prec = 6
        value_1 = dcml.Decimal (100)
        value_2 = dcml.Decimal (0.0001)

        expected_sum = dcml.Decimal ('100.0001')

        calculated_sum = value_1 + value_2 # 100.000
        self.assertTrue( expected_sum > calculated_sum)


if __name__ == '__main__':
    unittest.main()
