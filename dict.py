#!/usr/bin/env python3

import sys
# print(sys.version)

dict1={'first':'breyer',
    'last':'muth',
    'age':22,
    'city':'colorado springs',
    'car':'grand prix',}

print(f"{dict1}\n")
print("Users name is", dict1['first'].title(), dict1['last'].title(), ", age is ",dict1['age'], ".\n")

dict2={
    'mender':21,
    'breyer':21,
    'phteven':3,
    'kaley':00,
    }

col_width=max(len(key) for key in dict2) *2
#print(col_width)

print(f"\tName:".ljust(col_width), "Favorite #:".ljust(col_width))
for key, value in sorted(dict2.items()):
    print(f"\t{(key.title()).ljust(col_width)} {str(value).ljust(col_width)}")

tmp_set={*()} # Empty set
print("\nThe favorite numbers are:")
for num in dict2.values():
    tmp_set.add(num)
print(tmp_set)

