import importlib
import math
print(math.pi)

# math.pi = 3.14
importlib.reload(math)
print(math.pi)
# To reload a module, you can use the reload() function from the importlib module.
# This is useful when you're actively developing a module and want to see the changes without restarting the Python interpreter.

# Packages are namespaces that contain multiple modules and subpackages. A package is simply a directory

from numpy import *
