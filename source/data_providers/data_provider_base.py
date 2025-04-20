"""
Data provider base
"""

class DataProviderBase:
    """
    Data provider base
    """

    result = None
    source = "undefined"

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def get_source (self)-> str:
        """Source"""
        return self.source

    def get_data(self) -> list:
        """ Get data from data provider"""
        return self.result
