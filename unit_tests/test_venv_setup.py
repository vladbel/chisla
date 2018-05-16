import unittest
import numpy as np
import pandas as pd

class TestVenvSetup(unittest.TestCase):

    def test_can_import_pandas(self):
        
        self.assertTrue ( pd is not None)

    def test_can_import_numpy(self):
        
        self.assertTrue ( np is not None)

if __name__ == '__main__':
    unittest.main()
