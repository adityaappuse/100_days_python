import win32com.client as wincl

inputlist = []
speaker_number = 1
spk = wincl.Dispatch("SAPI.Spvoice")
vcs = spk.Getvoices()
SVSFlag = 11
print(vcs.Item(speaker_number).GetAttribute ("Name"))
spk.Voice
spk.SetVoice(vcs.Item(speaker_number))
while(True):
    input_name=input("Type the names you want to pass on to voice\n To exit press x")
    if(input_name=="x"):
        break
    inputlist.append(input_name)
print(inputlist)
for names in inputlist:
    spk.Speak(f"{names} is gay")


