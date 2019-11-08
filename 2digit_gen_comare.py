
import random

# Initialize variables
loop_var1=0
num_list=[]

# Loop to create 20 random 2 digit numbers.
while loop_var1 <=19:
    var1=random.randint(10,99)
    num_list.append(var1)
    loop_var1+=1
print("The 20 random 2 digit numbers generated are:")
print(f"{num_list}\n")

hit=0
miss=0
loop_var2=0
while loop_var2 <= 89:
    var1=random.randint(10,99)
    if var1 in num_list:
        hit+=1
        loop_var2+=1
    else:
        miss+=1
        loop_var2+=1

print(f"{hit} numbers of the 90 generated hit num_list.")
print(f"{miss} numbers of the 90 generated missed num_list.\n")

below=0
above=0
for num in num_list:
    if num <= 49:
        below+=1
    else:
        above+=1

print(f"{below} of the 2 digit numbers generated were below 50.")
print(f"{above} of the 2 digit numbers generated were 50 or above.")