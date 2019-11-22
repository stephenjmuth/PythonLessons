

# Set vars, lists, etc:
i=0

###################
### Define functions: ###
###################
def display_message():
    name=input("Please enter your name: ")
    print(f"Good {tod} {name.title()}.")
    return name

### To do - write a function to set tod message. Ex: morning if between these hours. afternnon if ...
def tod_func():
    tod="morning"
    return tod

def fav_book(name):
    book_title=input("What is your favorite book: ")
    print(f"{name.title()}'s favorite book is {book_title.title()}.")
    return book_title

###################
### To do - write a function to upper case abreviations - not contain vowels. 
###################

#Call func 
tod=tod_func()
name=(display_message())

fav_book_title=(fav_book(name)) # call fav book func and store title
