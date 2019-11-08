
import random

# Initialize variables
loop_var1=0
num_list1=[]
num_list2=[]

# Loop to create 2 lists of 20 random 2 digit numbers.
while loop_var1 <=39:
    var1=random.randint(10,99)
    if (loop_var1%2)==0:
        num_list1.append(var1)
        loop_var1+=1
    else:
        num_list2.append(var1)
        loop_var1+=1

print("The 20 random 2 digit numbers generated for list 1 are:")
print(f"{num_list1}\n")
print("The 20 random 2 digit numbers generated for list 2 are:")
print(f"{num_list2}\n")

# Initialize variables:
hit_list1=0
hit_list2=0
hit_both=0
miss=0
loop_var2=0

while loop_var2 <= 89:
    var1=random.randint(10,99)
    if var1 in num_list1 and var1 in num_list2:
        hit_list1+=1
        hit_list2+=1
        hit_both+=1
        loop_var2+=1
    elif var1 in num_list1:
        hit_list1+=1
        loop_var2+=1
    elif var1 in num_list2:
        hit_list2+=1
        loop_var2+=1
    else:
        miss+=1
        loop_var2+=1

print(f"{hit_list1} numbers of the 90 generated hit num_list1.")
print(f"{miss} numbers of the 90 generated missed num_list.\n")

below=0
above=0
for num in num_list1:
    if num <= 49:
        below+=1
    else:
        above+=1

print(f"{below} of the 2 digit numbers generated were below 50.")
print(f"{above} of the 2 digit numbers generated were 50 or above.")