class Library:
    def __init__(self):
        self.numofbooks = 0
        self.books=[]
    def addBook(self,book):
        self.books.append(book)
        self.numofbooks=len(self.books)
    def show(self):
        print(f"The number of books are {self.numofbooks}")
        if(self.numofbooks==len(self.books)):
            print("You have committed an error in your entry")
        else:
            print("You have done perfect entry")
    def show_eachbook(self):
        print(f"The books are \n {self.books}")
    def show_allbook(self):
        for book in self.books:
            print(book, end="\t")


Library1 = Library()
Library1.addBook("Harry potter")
Library1.show()

Library2 = Library()
Library2.addBook("The Alchemist")
Library2.show()
Library3 = Library()
Library3.addBook("Sherlock Holmes")
Library3.show()

while(True):
    inputlib = int(input("If you want to get the details of the book .Press \t1\t2\t3\n"))
    if(inputlib == 1):
        Library1.show_eachbook()
        break
    elif(inputlib ==2):
        Library2.show_eachbook()
        break
    elif(inputlib ==3):
        Library3.show_eachbook()
        break
    else: 
        print("Write proper instructions")
        




    
        
