class Libaray:
    def __init__(self,booklist,name):
        self.booklist=booklist
        self.name=name
        self.lendDict={}

    def display(self):
        print(f"Welcome to our {self.name} Library")
        print("Lists of Books available in library")
        for book in self.booklist:
            print(book)

    def lend(self,book,user):
            if book in self.booklist:
                if book not in self.lendDict.keys():
                    self.lendDict.update({book:user})
                    print("Lender Book Database has been updated")
                else:
                     print(f"Book is already being used by {self.lendDict[book]}")
            else:
                 print("This Book is not in Booklist. PLEASE enter correct book")

    def add(self,book):
        self.booklist.append(book)
        print("Book has been added to  the book list")

    def return_book(self,book):
        if book in self.booklist:
           self.lendDict.pop(book)
           print("Successfully Return")
        else:
            print("PLEASE enter the correct book name you want to return.")

if __name__ == '__main__':
    Veer=Libaray(["Python","c++","Java"],"Veer")
    while(True):
        print("Welcome to Library Managment System \nPRESS 1 for Display Book List \nPRESS 2 for Lend Book\nPRESS 3 for Add Book\nPRESS 4 for Return Book")
        user_choice=input()
        if user_choice not in ["1","2","3","4"]:
            print("Please enter a valid option")
            continue
        else:
            user_choice=int(user_choice)

        if user_choice==1:
            Veer.display()

        elif user_choice==2:
            book=input("Enter Book you want to lend")
            user=input("Enter user name")
            Veer.lend(book,user)

        elif user_choice==3:
            book=input("Enter the book you want to add")
            Veer.add(book)

        elif user_choice==4:
            book=input("Enter the book you want to return")
            Veer.return_book(book)

        else:
            print("Not a valid option")

        print("PRESS c to continue and q for quit or exit")
        user_choice2=""
        while(user_choice2!="c" and user_choice2!="q"):
             user_choice2=input()
             if user_choice2=="c":
                 continue
             elif user_choice2=="q":
                 exit()
