import unittest


import sys
import os

print (sys.path)
# # append module root directory to sys.path
# sys.path.append(
#     os.path.dirname(
#         os.path.dirname(
#             os.path.abspath(__file__)
#         )
#     )
# )
# print (sys.path)

import env
import bars.bar as bb

class TestBar(unittest.TestCase):

    def test_bar(self):      
        b = bb.Bar()
        result =b.bar()
        self.assertTrue (result=="bar")


if __name__ == '__main__':
    unittest.main()
