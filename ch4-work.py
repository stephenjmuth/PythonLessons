for num in range(5):
	print(num+1,end=' ')
print("\n")

squares=[]
for num in range(1,11):
	squares.append(num**2)
print(squares)
# squares = [value**2 for value in range(1, 11)] #This is a list comprehension.