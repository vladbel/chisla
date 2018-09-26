"""Module docstring"""
import unittest

# appends path to module under test to PYTHONPATH
# import unit_tests.test_data_provider_simple as TestDataProviderSimple


# module under test
import source.data_providers.data_provider_simple as dps

class TestDataProviderSimple(unittest.TestCase):
    """Class docstring"""

    def test_data_provider_simple(self):
        """method docstring"""
        data_provider = dps.DataProviderSimple()
        result = data_provider.get_data()
        self.assertTrue(isinstance(result, list))
        self.assertTrue(result[0] == 0)


if __name__ == '__main__':
    unittest.main()
