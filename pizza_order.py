#!/usr/bin/env python3

# Variables:
i=0
temp_toppings=[]
temp_crust=''
#string=''

# Lists:
avail_toppings=['Pepperoni','Mushrooms','Onions','Sausage','Bacon','Extra cheese','Black olives','Green peppers','Pineapple','Spinach',]
avail_crust=['thin','regular','deep dish',]
#print(avail_toppings)
#print(avail_crust)

### Func to turn list into formatted string.
def string_list(list):
    string=""
    for top in temp_toppings:
        string += (str(top)+', ')
    return string

print("\nThis is the Papa Stephen John's automated ordering app:")
prompt="\nEnter toppings you'd like added to your pizza, or 'quit' when you're finished. "
while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        if topping.title() in avail_toppings:
            print(f"{topping} has been added to your pizza.")
            temp_toppings.append(topping)
        else:
            print("That topping isn't available. Try again.")

print(f"Pick your crust: \n\t1. {avail_crust[0]}\n\t2. {avail_crust[1]}\n\t3. {avail_crust[2]}")
crust = input("Select crust: ")
if crust==1:
    temp_crust=avail_crust[0]
elif crust==2:
    temp_crust=avail_crust[1]
else:
    temp_crust=avail_crust[2]

print(f"\nYour {temp_crust} pizza with {string_list(temp_toppings)} has been placed in the oven.")
