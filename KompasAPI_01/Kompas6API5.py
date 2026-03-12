
from win32com.client import gencache

for key, value in vars(gencache.EnsureModule("{0422828C-F174-495E-AC5D-D31014DBBE87}", 0, 1, 0)).items():
    if key.startswith("__"):
        continue

    globals()[key] = value

