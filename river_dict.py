#!/usr/bin/env python3

# Define functions:
def set_creator(dict):
    for river,country in set(river_dict.items()):
        rivers.add(river)
        countrys.add(country)

river_dict={
    'colorado':'usa',
    'amazon':'brazil',
    'mississippi':'usa',
    'ganges':'india',
    'congo':'drc',
    'nile':'egypt',
    'niger':'guinea',
    }
print(river_dict, "\n")

for river,country in river_dict.items():
    print(f"The {river.title()} river runs through {country.upper() if len(country)==3 else country.title()}.")

rivers={*()}
countrys={*()}
set_creator(river_dict)
print(f"\n{len(rivers)} rivers in {len(countrys)} different countrys.\n")
print(f"The list of rivers is: \n\t{str(rivers).title()}")
print(f"The list of countrys is: \n\t{str(countrys).title()}")
