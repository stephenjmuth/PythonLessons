
# Vars:
i=0
yes=('YES','Yes','yes','Y','y',)
response="yes"

while response in yes:
    num = int(input("Please enter a number? "))
    if num%10==0:
        print("You entered a number that is a multiple of 10.")
    else:
        print("Your number is not a multiple of 10.")
    print("\nNow lets print all of the numbers up to yours:")
    while i<num:
        print(i,end=' ')
        i+=1
    response=input("\nWould you like to continue?")
    i=0
    if response not in yes:
        pass
