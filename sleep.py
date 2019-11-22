

# import only system from os 
from os import system, name 

# import sleep to show output for some time period 
from time import sleep 

# define our clear function 
def clear(): 

	# for windows 
	if name == 'nt': 
		_ = system('cls') 

	# for mac and linux(here, os.name is 'posix') 
	else: 
		_ = system('clear') 

while True:
    # print out some text 
    for i in range(1,11):
        print('hello geeks\n') 
        sleep(2)

    # sleep for 2 seconds after printing output 
    sleep(2) 

    # now call function we defined above 
    clear() 
    sleep(2)

"""
import time
for i in reversed(range(1,11)):
    print(i)
    time.sleep(1)"""