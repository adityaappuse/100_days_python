listofquestions=["What is the capital of Peru?","What is the largest living animal?","""If you suffer from arachnophobia,
 what animal are you scared of?"""]
listofoptions=[["Lima", "Egypt ", "India ," "USA"],["telephant","giraffe","blue whale","great white shark"],["water","situations","height","spider"]]
listofanswers=["Lima","blue whale","spider"]
print("You can become a billionaire")
j=0
i=0
for i in range(len(listofquestions)):
    print(" Here is your question")
    print(listofquestions[i],"\n",listofoptions[i],"\n")
    answer_one=int(input())
    if(listofoptions[i][answer_one-1] in listofanswers[i]):
        print("You have got the right answer!!!")
        j+1
    else: 
        print("You have fucked up sorry, hehe")
        break
    i+=1
    j+=1
if(j>=3):
    print("Lucky bastard You have got the money!!!Fuck Yeah")
