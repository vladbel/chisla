import unittest
import env
import source.foo as sf

class TestDataProviderSimple(unittest.TestCase):

    def test_data_provider_simple(self):      
        f = sf.Foo()
        result = f.foo()
        self.assertTrue (result=="foo")


if __name__ == '__main__':
    unittest.main()
