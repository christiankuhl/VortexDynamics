#!/usr/bin/env python3.6

import sys
import os
from importlib import import_module

try:
    demo_name = sys.argv[1]
except IndexError:
    demo_name = "sym3_unitdisk"

file_name = "demos/{}.py".format(demo_name)
if not os.path.isfile(file_name):
    raise Exception("File {} not found!".format(file_name))
else:
    import_module("demos.{}".format(demo_name))
