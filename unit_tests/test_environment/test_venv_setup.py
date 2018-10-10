"""
Attempt to test if virtual environment set-up is correct
"""
import unittest
import numpy as np
import pandas as pd

class TestVenvSetup(unittest.TestCase):
    """
    Attempt to test if virtual environment set-up is correct
    """

    def test_can_import_pandas(self):
        """
        Can import pandas
        """
        self.assertTrue(pd is not None)

    def test_can_import_numpy(self):
        """
        Can import numpy
        """
        self.assertTrue(np is not None)

if __name__ == '__main__':
    unittest.main()
