import sys
import os

# append module root directory to sys.path

# shall point to base workspace dir ('chisla')
path =  os.path.dirname(
            os.path.dirname(
                os.path.dirname(
                    os.path.abspath(__file__)
                )
            )
        )

path += '/source/data_providers'

if not any(path == s for s in sys.path):
    print('')
    print('**************************************************')
    print('Add path to module under test')
    print(path)
    print('to sys.path')
    print('**************************************************')
    print('')
    sys.path.append(path)
else:
    print('')
    print('Path ' + path + ' already present in sys.path')

#print(sys.path)