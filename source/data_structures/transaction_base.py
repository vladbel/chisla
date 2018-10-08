"""
Data provider base
"""

# import datetime as dt
# import decimal as dcml

class TransactionBase:
    """
    Transaction base
    """
    ticker = None


    def __init__(
            self,
            ticker: str):
        """
        Init
        """
        self.ticker = ticker
        # self.date = date
        # self.price = price
        # self.number_of_units = number_of_units

        #total = price * number_of_units
