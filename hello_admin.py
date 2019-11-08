

# imports
import random 

# Lists of user names:
user_names=['admin','slim','marshal','jackson','martha',]
#user_names=['admin','slim','marshal','jackson','martha','marshal1','marshal2','marshal3','marshal4',]
new_users=['troy','toby','marshal',]

# Define functions:
def num_gen(new_user):
    user_sugg=[]
    loop_var=0
    while loop_var<=2:
        # Create random user id and test for presence in user_names. 
        # <<<=== Also need to check for presence in user_sugg. ===>>>
        i=random.randint(100,999)
        user_test=new_user+str(i)
        if user_test.lower() in user_names:
            # Write failed attempts to a log file here. Future code. 
            with open("log.txt","a") as f:
                f.write(user_test+"\n")
            f.close
            pass
        # If random user id not in user_names append to user_sugg(suggested user list).
        else:
            user_sugg.append(user_test)
            loop_var+=1
    return user_sugg # Return list of 3 random users names.


if user_names:
    for user_name in user_names:
        if user_name=='admin':
            print("Welcome back oh great wizzard of id. Would you like todays report?")
        else:
            print(f"Hello {user_name.title()}, welcome back.")
else:
    print("We need to find some users.")

for new_user in new_users:
    if new_user.lower() in user_names:
        sugg_user=num_gen(new_user) # Run alternate user suggestions and return list to user.
        print("This user name is currently in use. You will need to choose something unique.")
        print(f"Here are 3 suggestions: \n\t1. {sugg_user[0]}\n\t2. {sugg_user[1]}\n\t3. {sugg_user[2]}")
        
        
#        print(sugg_user[0])
        

    else:
        print("The user name you entered is available. You are being added to our list of current users.")
        # Run add user to user_names method and return ID.
        

