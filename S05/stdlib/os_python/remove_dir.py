import os
import glob


dirs = glob.glob("./dir*")
for d in dirs:
    os.rmdir(d)
