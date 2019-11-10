#!/usr/bin/env python3

import sys
# print(sys.version)

# Extract keys from dict.
def key_extractor(dict):
    for entry in dict.items():
        for key in entry:
            print(key)
#            key_dict.append(key)
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
    print(f"\n\t{i}. {person['first'].title()} {person['last'].title()}")
    i+=1
print("="*len(string1))

more_peoples={
    'monkey':['christian','muth','3','colorado springs','none','95',],
    'TT':['trevor','muth','3','colorado springs','none','yellow',],
    }

print(f"\n{more_peoples}")

key_dict={}
key_extractor(peoples[0])
# print(sublist[0])
