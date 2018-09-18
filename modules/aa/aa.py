import sys
import os
import env

print (sys.path)

import bb_dir.bb_file as b

b_instance = b.BB1()

print (b_instance.b())