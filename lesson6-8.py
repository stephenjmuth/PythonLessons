#!/usr/bin/env python3

#variables:
i=0

pets=[
    {'type':'dog','color':'brown','owner':'joey','bites':0},
    {'type':'bird','color':'grey','owner':'sarah','bites':1},
    {'type':'bear','color':'black','owner':'grizzly adams','bites':0},
    {'type':'cat','color':'calico','owner':'anna','bites':1}
    ]

for elem in pets:
    i+=1
    teeth="bites" if elem['bites']==1 else "doesn't bite"
    print(f"\t{i}. {elem['owner'].title()} has a {elem['color']} {elem['type']} that {teeth}.")
i=0 # reset i to 0 for future use.
