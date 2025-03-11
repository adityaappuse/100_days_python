from pypdf import PdfWriter
import os 
merger = PdfWriter()
inputlist=[]
inputfile=""
files = os.listdir(r"C:\Users\adity\Documents\experiment-pdf")
source = r"C:\Users\adity\Documents\experiment-pdf"
for file in files:
    print(file)
    merger.append(os.path.join(source,file))
        
merger.write("result.pdf")
merger.close()


