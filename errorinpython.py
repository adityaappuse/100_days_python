
while True:
    takeitbitch = input("Type either a number or quit to continue \n")
    try:
        if(takeitbitch=="quit"):
            print("Perfectly valid request")
            break
        takeitbitch==int(takeitbitch)
        print(f"The number here is perfectly valid and the number is {takeitbitch}")
    except ValueError:
        print("Type a number or quit whoreassbitch")
    finally:
        print("What the actual fuck?hehe")