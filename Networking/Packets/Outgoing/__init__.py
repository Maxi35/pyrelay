import os
import importlib

path = __file__.replace("__init__.py", "")

for file in os.listdir(path):
    if "__" not in file:
        globals()[file[:-3]] = getattr(importlib.import_module(__name__+"."+file[:-3]), file[:-3])
