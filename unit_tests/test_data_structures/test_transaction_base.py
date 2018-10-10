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
        """
        Valid transaction shall have
        is_valid == True
        """
        transaction = tb.TransactionBase(
            ticker="abc",
            unit_price=dcml.Decimal(11.01),
            number_of_units=2)

        self.assertTrue(transaction.is_valid)
        self.assertTrue(transaction.ticker == "abc")

    def test_invalid_if_empty_string_provided_as_ticker(self):
        """
        Transaction is invalid if empty ticker provided
        is.valid == False
        """
        transaction = tb.TransactionBase(
            ticker="",
            unit_price=dcml.Decimal(11.01),
            number_of_units=2)

        self.assertFalse(transaction.is_valid)

    def test_invalid_if_int_provided_as_ticker(self):
        """
        Transaction is invalid if empty ticker provided
        is.valid == False
        """
        transaction = tb.TransactionBase(
            ticker=2,
            unit_price=dcml.Decimal(11.01),
            number_of_units=2)

        self.assertFalse(transaction.is_valid)

    def test_invalid_if_nonpositive_number_of_units_provided(self):
        """
        Transaction is invalid if non-positive number of
        units provided

        is_valid == False
        """
        transaction = tb.TransactionBase(
            ticker="abc",
            unit_price=dcml.Decimal(11.01),
            number_of_units=0)

        self.assertFalse(transaction.is_valid)

    def test_invalid_if_float_provided_as_number_of_units(self):
        """Transaction is invalid if float provided as number_of_units"""
        transaction = tb.TransactionBase(
            ticker="abc",
            unit_price=dcml.Decimal(11.01),
            number_of_units=1.1)

        self.assertFalse(transaction.is_valid)
        self.assertTrue(transaction.number_of_units is None)


if __name__ == '__main__':
    unittest.main()
