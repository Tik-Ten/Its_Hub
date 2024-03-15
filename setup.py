import shutil
import sys
src = r"src/Its_Hub.py"
dst = sys.argv[1] # Python libraries address
dst = rf"{dst}"
print("dst = " + dst)
print("Start copying...")
shutil.copy(src, dst)
print("Copy ended. Now, you can use Its_Hub library :)")