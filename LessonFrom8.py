#!/usr/bin/env python3

from funcs import func1
from funcs import func12

int1,int2=1,2
var1="val1"
list1=[1,2,3,]
list2=[2,3,4,]

#################################################
### Define functions ### Define functions ### Define functions ###
#################################################
"""
def func1(func_var1):
    print(f"\t\tCall func1 - print func_var1: {func_var1}")
    func_var2=func_var1*2
    print(f"\t\tCreate func_var2(*2) and print: {func_var2}")
    return func_var2
def func12(func_var11,func_var12):
    print(func_var11,func_var12)
    func_var22=func_var11*2
    func_var23=func_var12*2
    return func_var22,func_var23
"""
##################################################
### Code starts here ### Code starts here ### Code starts here ###
##################################################
print("Initial print of variables:")
print(f"\t1. Print var1: {var1}")
print(f"\t2. Print list1: {list1}")
print(f"\t3. Print list2: {list2}")
print(f"\t4. Print int1 & int2: {int1} | {int2}")

# Function calls:
print(f"\nRunning function calls here:")
var2=func1(var1)    #Call func1 and pass it var1 - returns func_var2/assigns to var2
list3=func1(list1)    #Call func1 and pass it list1 - returns func_var2/assigns to list3
int2=func1(int1)    #Call func1 and pass it list1 - returns func_var2/assigns to list3
int11,var11=func12(int1,var1)

print(f"\nReturn from function calls, printing returned values:")
print(var2) #Print value returned from func1
print(list3) #Print value returned from func1
print(int2) #Print value returned from func1
print(int11,var11,"print int11 and var11")
