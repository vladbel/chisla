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
        self.validate_ticker()
        # self.date = date
        # self.price = price
        # self.number_of_units = number_of_units

        #total = price * number_of_units

    def validate_ticker(self) -> bool:
        """
        Init
        """
        if self.ticker is None:
            return False
        return True
