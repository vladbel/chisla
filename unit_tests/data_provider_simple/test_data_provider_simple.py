import unittest

# appends path to module under test to PYTHONPATH
import env

# module under test
import data_provider_simple as dps

class TestDataProviderSimple(unittest.TestCase):

    def test_data_provider_simple(self):
        
        data_provider = dps.DataProviderSimple()
        result = data_provider.get_data()
        self.assertTrue( isinstance( result, list))
        self.assertTrue (result[0] == 0)


if __name__ == '__main__':
    unittest.main()
