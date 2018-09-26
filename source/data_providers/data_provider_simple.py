"""
Simple data provider
"""
import source.data_providers.data_provider_base as dpb

class DataProviderSimple(dpb.DataProviderBase):
    """
    Simple data provider
    """

    def __init__(self):
        """
        Init for test purpose
        """
        self.result = [0, 1, 2, 3]
