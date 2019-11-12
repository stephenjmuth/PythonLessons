i=0
sandwich_orders=['italian','pastrami','ham and cheese','turkey club','blt','pastrami','ham','pb&j','pastrami',]
finished_sandwiches=[]

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    print("The deli has run out of Pastrami. Removing Pastrami sandwich from orders.")

while sandwich_orders:
    current_sandwich=sandwich_orders.pop()
    print(f"Currently making {current_sandwich}.")
    finished_sandwiches.append(current_sandwich)
print("\nThe following sandwiches have been made:")
for finished_sandwich in finished_sandwiches:
    i+=1
    print(f"\t{i}. {finished_sandwich.upper() if len(finished_sandwich)==3 else finished_sandwich.title()}")