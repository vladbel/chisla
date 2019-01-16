"""Module docstring"""
import unittest

# standard lib modules
import decimal as dcml

# module under test
import data_structures.transaction_base as tb
import data_structures.position_base as pb


class TestPositionBase(unittest.TestCase):
    """
    Unit tests for PositionBase
    """

    def test_valid_position_instantiation(self):
        """--- valid position instance can be created ---"""
        position = pb.PositionBase(
            ticker="abc")

        self.assertTrue(position.ticker == "abc")

    def test_apply_transaction_to_position(self):
        """--- valid position instance can be created ---"""
        position = pb.PositionBase(
            ticker="abc")

        transaction = tb.TransactionBase(
            ticker="abc",
            unit_price=dcml.Decimal(11.01),
            number_of_units=2)

        self.assertTrue(position.apply_tansaction(transaction))


if __name__ == '__main__':
    unittest.main()
