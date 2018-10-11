"""
Data provider base
"""

# import datetime as dt
import decimal as dcml

class TransactionBase:
    """
    Transaction base
    """
    is_valid = None
    ticker = None
    unit_price = None
    number_of_units = None
    total_cost = None


    def __init__(
            self,
            ticker: str,
            unit_price: dcml.Decimal,
            number_of_units: int):
        """
        Init transaction
        """
        self.ticker = ticker
        self.unit_price = unit_price
        self.number_of_units = number_of_units

        if self.validate():
            self.total_cost = self.set_total_cost(
                self.unit_price,
                self.number_of_units)

    def set_total_cost(
            self,
            unit_price: dcml.Decimal,
            number_of_units: int) -> dcml.Decimal:
        """
        basic implementation of total cost
        """
        if not self.is_valid:
            return None

        result = unit_price * dcml.Decimal(number_of_units)
        result = result = result.quantize(dcml.Decimal('0.01'))
        return result

    def validate(self) -> bool:
        """
        validate if all components of transaction are set to proper values

        """
        if not isinstance(self.ticker, str) \
                or not self.ticker:
            self.is_valid = False
            self.ticker = None
        elif not isinstance(self.unit_price, dcml.Decimal) \
                or self.unit_price is None \
                or self.unit_price == 0 \
                or self.unit_price < 0:
            self.is_valid = False
            self.unit_price = None
        elif not isinstance(self.number_of_units, int) \
                or self.number_of_units < 1:
            self.is_valid = False
            self.number_of_units = None
        else:
            self.is_valid = True

        return self.is_valid
