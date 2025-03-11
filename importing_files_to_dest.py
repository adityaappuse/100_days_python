import os 
import shutil
files = os.listdir(r"C:\Users\adity\Downloads")
source = r"C:\Users\adity\Downloads"
dest = r"C:\Users\adity\Documents\experiment-pdf"
i=0

for file in files:
    
    if i>5:
        print("The job seems to have completed")
        break
    elif file.endswith(".pdf"):
        shutil.copy(os.path.join(source,file),dest)
    i=i+1




