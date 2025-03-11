import random
list_of_game_option=[
                        ["D","W","L"],
                        ["L","D","W"],
                        ["W","L","D"]
                    ]
def convertuserchoice_to_numbers(choice):
  
    if(choice == "s"):
        return 0
    elif(choice == "p"):
        return 1
    elif(choice == "sc"):
        return 2
    else:
        return ValueError
    
while(True):
    listofchoicescomp = [0,1,2]
    computer_choice =  random.choice(listofchoicescomp)
    user_choice = input("What is your choice?\n You can put \nS for stone \tp for paper \tsc for scissors\n")
    choice1 = convertuserchoice_to_numbers(user_choice)
    print(choice1)
    print(computer_choice)
    result = (list_of_game_option[choice1][computer_choice])    
    if(result == "W"):
        print("You have won!!!")
        break
    elif(result == "L"):
        print("You have lost, retry!!!")
    elif(result == "D"):
        print("You have not reached a conclusion ,Retry")