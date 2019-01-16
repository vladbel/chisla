"""Module docstring"""
import unittest

# standard lib modules
import decimal as dcml

# module under test
import data_structures.transaction_base as tb


class TestTransactionBase(unittest.TestCase):
    """
    Unit tests for TransactionBase
    """

    def test_valid_transaction_instantiation(self):
        """--- valid transaction instance can be created ---"""
        transaction = tb.TransactionBase(
            ticker="abc",
            unit_price=dcml.Decimal(11.01),
            number_of_units=2)

        self.assertTrue(transaction.is_valid)
        self.assertTrue(transaction.ticker == "abc")

    def test_invalid_if_empty_string_provided_as_ticker(self):
        """--- invalid if empty ticker provided ---"""
        transaction = tb.TransactionBase(
            ticker="",
            unit_price=dcml.Decimal(11.01),
            number_of_units=2)

        self.assertFalse(transaction.is_valid)

    def test_invalid_if_int_provided_as_ticker(self):
        """--- invalid if empty ticker provided ---"""
        transaction = tb.TransactionBase(
            ticker=2,
            unit_price=dcml.Decimal(11.01),
            number_of_units=2)

        self.assertFalse(transaction.is_valid)

    def test_invalid_if_nonpositive_number_of_units_provided(self):
        """--- invalid if non-positive number of units provided ---"""
        transaction = tb.TransactionBase(
            ticker="abc",
            unit_price=dcml.Decimal(11.01),
            number_of_units=0)

        self.assertFalse(transaction.is_valid)

    def test_invalid_if_float_provided_as_number_of_units(self):
        """--- invalid if float provided as number_of_units ---"""
        transaction = tb.TransactionBase(
            ticker="abc",
            unit_price=dcml.Decimal(11.01),
            number_of_units=1.1)

        self.assertFalse(transaction.is_valid)
        self.assertTrue(transaction.number_of_units is None)

    def test_invalid_if_float_provided_as_unit_price(self):
        """--- invalid if float provided as unit_price ---"""
        transaction = tb.TransactionBase(
            ticker="abc",
            unit_price=11.01,
            number_of_units=2)

        self.assertFalse(transaction.is_valid)
        self.assertTrue(transaction.unit_price is None)

    def test_valid_total_price_shall_be_set_for_valid_transaction(self):
        """---- Total price shall be set for valid transaction ---"""
        transaction = tb.TransactionBase(
            ticker="abc",
            unit_price=dcml.Decimal(11.01),
            number_of_units=2)
        self.assertTrue(transaction.total_cost == dcml.Decimal('22.02'))

if __name__ == '__main__':
    unittest.main()
