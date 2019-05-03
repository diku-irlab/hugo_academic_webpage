import subprocess
import glob

for file in glob.glob("bibtex/*"):
    print("academic import --bibtex "+file)
    callProcess = subprocess.call("academic import --overwrite --bibtex "+file, shell=True) # 
    print("---")
