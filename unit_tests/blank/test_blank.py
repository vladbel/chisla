"""
pylint C0111: Missing module docstring (missing-docstring)
"""
import unittest


class TestBlank(unittest.TestCase):
    """
    pylint C0111: Missing class docstring (missing-docstring)
    """

    def test_blank_1(self):
        """
        pylint C0111: Missing class docstring (missing-docstring)
        """
        i = 1
        self.assertTrue(i == 1)


    def test_blank_2(self):
        """
        pylint C0111: Missing class docstring (missing-docstring)
        """
        i = 1
        self.assertTrue(i == 1)

if __name__ == '__main__':
    unittest.main()
