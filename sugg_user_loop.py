
import random
user="slammer"
user_sugg=[]
loop_var=0

while loop_var <=2:
    i=random.randint(100,999)
    user_sugg.append(user+str(i))
    loop_var+=1
print(user_sugg)


#def my_function():
#    i=5*3
#    return i
#print(my_function())
