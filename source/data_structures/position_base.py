"""
Position base
"""

import data_structures.transaction_base as tr

class PositionBase:
    """
    Position  base
    """

    ticker = None

    def __init__(self,
                 ticker: str):
        """
        Init transaction
        """
        self.ticker = ticker

    def apply_tansaction(self,
                         transaction: tr.TransactionBase) -> bool:
        """
        Apply transaction
        """
        return self.ticker == transaction.ticker
