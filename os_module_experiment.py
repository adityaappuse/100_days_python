import os 
files=os.listdir(r"C:\Users\adity\Documents\experiment")
i=0
for file in files:
    if file.endswith(".png"):
        i=i+1
        print(file)
        old_path=os.path.join(r"C:\Users\adity\Documents\experiment",file)
        new_path=os.path.join(r"C:\Users\adity\Documents\experiment",f"{i}.png")
        os.rename(old_path,new_path)
        
