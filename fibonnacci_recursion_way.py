def fibonnacci(n):
    if(n==1):
        return 0
        print(i)
    elif(n==2):
        return 1
    elif(n>2):
        return fibonnacci(n-1)+fibonnacci(n-2)
fib_count=2
while(fib_count!=0):
    if(fib_count==0):
        break
    fib_count=int(input("Enter the value to which we need to count the fibonnacci series :"))
    print(fibonnacci(fib_count))
    print("To exit just press 0")



    