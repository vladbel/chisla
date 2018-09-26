"""
docstring
"""
import sys
import os

# append module root directory to sys.path

# shall point to base workspace dir ('chisla')
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

BASE_DIR += '/source/data_providers'

if not any(BASE_DIR == s for s in sys.path):
    print('')
    print('**************************************************')
    print('Add path to module under test')
    print(BASE_DIR)
    print('to sys.path')
    print('**************************************************')
    print('')
    sys.path.append(BASE_DIR)
else:
    print('')
    print('Path ' + BASE_DIR + ' already present in sys.path')

#print(sys.path)
