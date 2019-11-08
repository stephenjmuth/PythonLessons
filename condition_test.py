# Conditional_tests.py

# Define functions:
# my_func1 loops over a list testing for and counting digits and returns the total. 
def my_func1(List):
    i=0
    for item in List:
        if item.isdigit():
            i+=1
    return i

# Create lists for eveluation:
L1=['he','she','they','them','us','we',]
L2=['1','eleven','4','7','fourteen','14',]

# Print lists.
print(f"Print list 1: {L1}")
print(f"Print list 2: {L2}\n")

# Condition 1
if L1[0]=='he' and L2[0]=='1':
    print("He is 1.")

# Condition 2
if L2[-1]>='14' or L2[-1]>=14:
    print("The last item in list 2 is 14.")

# Condition 3
if len(L1)==6 and len(L2)==6:
    print("Both lists are 6 characters long.")

# Condition 4
if type(L1[4])==str and type(L2[4])==str:
    print("They are both strings.")

# Condition 5
if L2[2].isdigit():
    print("It's a digit.")

# Call function above and print results.
print(f"\n{my_func1(L1)} of the items in list L1 are numbers.")
print(f"{my_func1(L2)} of the items in list L2 are numbers.")
