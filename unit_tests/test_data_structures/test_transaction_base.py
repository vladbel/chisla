"""Module docstring"""
import unittest

# module under test
import data_structures.transaction_base as tb



class TestTransactionBase(unittest.TestCase):
    """Class docstring"""

    def test_transaction_price_shall_have_ticker(self):
        """method docstring"""
        transaction = tb.TransactionBase("abc")
        self.assertTrue(transaction.ticker == "abc")


if __name__ == '__main__':
    unittest.main()
