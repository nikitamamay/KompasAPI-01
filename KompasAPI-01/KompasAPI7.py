

from win32com.client import gencache

for key, value in vars(gencache.EnsureModule("{69AC2981-37C0-4379-84FD-5DD2F3C0A520}", 0, 1, 0)).items():
    if key.startswith("__"):
        continue

    globals()[key] = value

