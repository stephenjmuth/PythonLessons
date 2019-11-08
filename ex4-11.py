pizzas=['cheese','peperoni','sausage & onion','snakes & lizzards',]
for pizza in pizzas:
	print(f"I like {pizza} pizza.")
print()
print("I really love pizza!")

#Update of 4-11
friend_pizzas=pizzas[:]

pizzas.append("veggie")
friend_pizzas.append("white")

i=0
print(f"\nMy favorite pizzas are:")
for pizza in pizzas:
	i=i+1
	print(f"\t{i}. {pizza.title()}")

i=0
print(f"\nMy friends favorite pizzas are:")
for pizza in friend_pizzas:
	i=i+1
	print(f"\t{i}. {pizza.title()}")