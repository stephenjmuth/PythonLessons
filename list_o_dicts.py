#!/usr/bin/env python3

import sys
# print(sys.version)

# Extract keys from dict, return them in key_dict.
def key_extractor(dict):
    for k,v in dict.items():
        key_dict[k]=''
    return key_dict

peoples=[
    {'userid':'breyer','first':'breyer','last':'muth','age':22,'city':'colorado springs','car':'grand prix','fav_num':'21'},
    {'userid':'mender.muth','first':'mender','last':'bostrom','age':24,'city':'colorado springs','car':'impala','fav_num':'21'},
    {'userid':'s.muth','first':'stephen','last':'muth','age':52,'city':'colorado springs','car':'mustang cobra','fav_num':'3'},
    {'userid':'kaley.muth','first':'kaley','last':'muth','age':18,'city':'phoenix','car':'versa','fav_num':'00'},
    ]

i=1
string1="The current user list is:"
print("="*len(string1))
print(string1)
for person in peoples:
    print(f"\n\t{i}. {person['first'].title()} {person['last'].title()} | User ID: {person['userid']} | Location: {person['city'].title()} | Automobile: {person['car'].title()} | Favorite #: {person['fav_num']}")
    i+=1
print("="*len(string1))

more_peoples={
    'monkey':['christian','muth','3','colorado springs','none','95',],
    'TT':['trevor','muth','3','colorado springs','none','yellow',],
    }

#print(f"testing the state of the variable 'i': {i}") # Are there local variables in Python? What is best practice for iterator? Reset everytime you use it?
i=1
print("Print new users to be added:")
for item in more_peoples:
    print(f"\t{i}. {item} {more_peoples[item]}")

#for i in test_dict : 
#    print(i, test_dict[i]) 
print("="*len(string1))

key_dict={}
key_extractor(peoples[0])
# Print keys extracted by key_extractor. 
print(f"Print extracted keys:\n\t{key_dict}")
print("="*len(string1))
print("Need a function here to join new user data with extracted keys to import into peoples dict.")
print("="*len(string1))

