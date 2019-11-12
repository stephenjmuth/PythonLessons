

# Simple list(elements) and dict(items(key:value)).
simple_list=[1,2,3]
simple_dict={'first':'stephen','last':'muth'}

### Access one item from each. 
# Access list[element0]
access_list=simple_list[0]
print(access_list)
# Access dict[item key] - this produces the value.
access_dict=simple_dict['first']
print(access_dict)

### Simple list of dicts. 
# Each dict is a list element made of key:value pairs. 
list_of_dicts=[
    {'first':'john','last':'doe'},
    {'first':'jane','last':'doa'}
    ]

### Access
# Access first list element.
access_lod=list_of_dicts[0]
print(access_lod)
# Access first item of first element - access is sequential - list
access_ld=list_of_dicts[0]['first']
print(access_ld)

### Accessing via for loops.
# Access each element of a list via for loop.
print("Print all nums from simple list (no cr):")
for num in simple_list:
    print(num,end=' ')
print("\n") # print a blank line for readability.

# Access each value of dict via item key with for loop. 
print("Print all values in simple dict (no cr):")
for key,value in simple_dict.items():
    print(value,end=' ')
print("\n") # print a blank line for readability.

# Accessing dict in list with for loop.
print("Print both dicts in list:")
for dict in list_of_dicts:
    print(dict)
print("\n") # print a blank line for readability.

# Accessing values of dict items in list with for loops.
print("\nPrint all values from both dicts in the list with for loop (no cr):")
for elem in list_of_dicts:
    for key,value in elem.items():
        print(value,end=' ')
print("\n") # print a blank line for readability.

for elem in list_of_dicts:
    print(elem['first'].title(), elem['last'].title())
print("\n") # print a blank line for readability.

# extract keys from a dict and create a new dict with values set to 'none'.
temp_dict={}
for key,value in list_of_dicts[0].items():
        temp_dict[key]='none'
print(temp_dict)
