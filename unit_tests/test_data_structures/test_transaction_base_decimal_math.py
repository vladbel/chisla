"""Module docstring"""
import unittest

# standard lib modules
import decimal as dcml

# module under test
import data_structures.transaction_base as tb


class TestTransactionBaseDecimalMath(unittest.TestCase):
    """
    Unit tests for TransactionBase
    """

    def test_01(self):
        """---- 20.05 * 2 = 40.10 ---"""
        transaction = tb.TransactionBase(
            ticker="abc",
            unit_price=dcml.Decimal('20.05'),
            number_of_units=2)
        self.assertTrue(transaction.total_cost == dcml.Decimal('40.10'))

    def test_02(self):
        """---- 20.005 * 2 = 40.01 ---"""
        transaction = tb.TransactionBase(
            ticker="abc",
            unit_price=dcml.Decimal('20.005'),
            number_of_units=2)
        self.assertTrue(transaction.total_cost == dcml.Decimal('40.01'))

    def test_03(self):
        """---- 20.009 * 2 = 40.02 ---"""
        transaction = tb.TransactionBase(
            ticker="abc",
            unit_price=dcml.Decimal('20.009'),
            number_of_units=2)
        self.assertTrue(transaction.total_cost == dcml.Decimal('40.02'))

    def test_04(self):
        """---- 1000000000.009 * 2 = 2000000000.02 ---"""
        transaction = tb.TransactionBase(
            ticker="abc",
            unit_price=dcml.Decimal('1000000000.009'),
            number_of_units=2)
        self.assertTrue(transaction.total_cost == dcml.Decimal('2000000000.02'))

    def test_05(self):
        """---- 0.509 * 2 = 1.02 ---"""
        transaction = tb.TransactionBase(
            ticker="abc",
            unit_price=dcml.Decimal('0.509'),
            number_of_units=2)
        self.assertTrue(transaction.total_cost == dcml.Decimal('1.02'))

    def test_06(self):
        """---- 5.5029 * 2 = 11.01 ---"""
        transaction = tb.TransactionBase(
            ticker="abc",
            unit_price=dcml.Decimal('05.5029'),
            number_of_units=2)
        self.assertTrue(transaction.total_cost == dcml.Decimal('11.01'))

    def test_07(self):
        """---- 5.5029 * 2 = 11.01 ---"""
        transaction = tb.TransactionBase(
            ticker="abc",
            unit_price=dcml.Decimal('05.5029'),
            number_of_units=2)
        self.assertTrue(transaction.total_cost == dcml.Decimal('11.01'))

    def test_08(self):
        """---- 0.33 * 3 = 0.99 ---"""
        transaction = tb.TransactionBase(
            ticker="abc",
            unit_price=dcml.Decimal('0.33'),
            number_of_units=3)
        self.assertTrue(transaction.total_cost == dcml.Decimal('0.99'))

    def test_09(self):
        """---- 0.3333 * 3 = 1.00 ---"""
        transaction = tb.TransactionBase(
            ticker="abc",
            unit_price=dcml.Decimal('0.3333'),
            number_of_units=3)
        self.assertTrue(transaction.total_cost == dcml.Decimal('1.00'))

    def test_10(self):
        """---- 0.3033 * 3 = 0.91 ---"""
        transaction = tb.TransactionBase(
            ticker="abc",
            unit_price=dcml.Decimal('0.3033'),
            number_of_units=3)
        self.assertTrue(transaction.total_cost == dcml.Decimal('0.91'))

    def test_11(self):
        """---- 20 * 3 = 60.00 ---"""
        transaction = tb.TransactionBase(
            ticker="abc",
            unit_price=dcml.Decimal('20'),
            number_of_units=3)
        self.assertTrue(transaction.total_cost == dcml.Decimal('60.00'))

    def test_12(self):
        """---- 0.0033 * 3 = 0.01 ---"""
        transaction = tb.TransactionBase(
            ticker="abc",
            unit_price=dcml.Decimal('0.0033'),
            number_of_units=3)
        self.assertTrue(transaction.total_cost == dcml.Decimal('0.01'))

    def test_13(self):
        """---- 0.0003 * 3 = 0.00 ---"""
        transaction = tb.TransactionBase(
            ticker="abc",
            unit_price=dcml.Decimal('0.0003'),
            number_of_units=3)
        self.assertTrue(transaction.total_cost == dcml.Decimal('0.00'))

    def test_14(self):
        """---- 0.0025001 * 2 = 0.01 ---"""
        transaction = tb.TransactionBase(
            ticker="abc",
            unit_price=dcml.Decimal('0.0025001'),
            number_of_units=2)
        self.assertTrue(transaction.total_cost == dcml.Decimal('0.01'))

    def test_15(self):
        """---- 1.0025 * 2 = 2.01 ---"""
        transaction = tb.TransactionBase(
            ticker="abc",
            unit_price=dcml.Decimal('1.0025'),
            number_of_units=2)
        self.assertTrue(transaction.total_cost == dcml.Decimal('2.01'))

    def test_16(self):
        """---- 1.0024 * 2 = 2.00 ---"""
        transaction = tb.TransactionBase(
            ticker="abc",
            unit_price=dcml.Decimal('1.0024'),
            number_of_units=2)
        self.assertTrue(transaction.total_cost == dcml.Decimal('2.00'))

if __name__ == '__main__':
    unittest.main()
