# message = input("Enter a message \t")
# listofmessages=message.split( )
# i=0
# for i in range(len(listofmessages)):
#     if(len(listofmessages[i])>3):
#         eb_word = listofmessages[i]
#         eb_word[0]=eb_word[] 

# For 1 word
# def encyption_part1(message):
#     return message[-1]+ message[1:-1]+message[0]
# message_word=input("Enter the message \n\n")
# length=len(message_word)
# if(length>3):
#     message_word = encyption_part1(message_word)
#     random_wordslist=("arg","pre","neg","gie","lim")
#     for i in random_wordslist:
#         message_result=f"{i}{message_word}{i}"
# print(message_result)  
# For long string  
def encyption_part1(message):
     return message[-1]+ message[1:-1]+message[0]

message_word=input("Enter the message to be encrypted :")
random_wordslist=("arg","pre","neg","gie","lim")
temp_message=message_word.split()

message_result=[]
j=0
for i in range(0,len(temp_message)):
     if(len(temp_message[i])<=3):
          m=temp_message[i]
          message_result.append(m[::-1])
          continue
     message_word1=encyption_part1(temp_message[i])
     message_result.append(f"{random_wordslist[i]}{message_word1}{random_wordslist[i]}")
     j+=1
result = ' '.join(message_result)
print(result)

