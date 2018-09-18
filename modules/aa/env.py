import sys
import os


print(sys.path)

# append module root directory to sys.path
path =  os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)
            )
        )

print(path)

if not any(path == s for s in sys.path):
    sys.path.append(path)


print(sys.path)
