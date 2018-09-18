import unittest
import sys
import os

# append module root directory to sys.path
sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)


import source.data_providers as dp

class TestDataProviderSimple(unittest.TestCase):

    def test_data_provider_simple(self):
        
        data_provider = dp.data_provider_base.DataProviderSimple()
        self.assertTrue (True)


if __name__ == '__main__':
    unittest.main()
