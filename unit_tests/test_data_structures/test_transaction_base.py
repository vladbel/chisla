"""Module docstring"""
import unittest

# standard lib modules
import sys as s
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
        is.valid == True
        """
        transaction = tb.TransactionBase(
            "ticker",
            dcml.Decimal(11.01),
            2)
        self.assertTrue(transaction.is_valid)

    def test_invalid_transaction_shall_raise_exception(self):
        """
        Valid transaction shall have
        is.valid == True
        """
        exception_raised = False
        try:
            transaction = tb.TransactionBase(
                "",
                dcml.Decimal(11.01),
                2)
        except ValueError:
            error_type, error_value, error_traceback = s.exc_info()
            if error_type is ValueError \
                    and error_value.args[0] == "Invalid value for transaction" \
                    and error_traceback is not None:
                exception_raised = True
        finally:
            self.assertTrue(exception_raised)
            self.assertFalse(transaction.is_valid)


if __name__ == '__main__':
    unittest.main()
