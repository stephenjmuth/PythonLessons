programmers=['don','zach','tony','neil','sree',]
print(programmers)
print()
print(f"Print the last 3 programmers: \t{programmers[-3:]}")
print(f"Print the last 3 programmers: \t{programmers[:3]}")
print(f"Print the 2nd and 3rd: \t\t{programmers[1:3]}")

print(f"\nThe first 3 Programmers names are:")
for programmer in programmers[:3]: #Looping through a slice.
	print(programmer.title(),end=' ')

# DeepCopy a list by slicing the entire thing.
print(f"\n")
slice=programmers[:] #This is easier than looping/appending.
#slice=[]
#for programmer in programmers[:]:
#	slice.append(programmer)
print(slice)

print(f"\nThe ID of programmers is: \t{id(programmers)}")
print(f"The ID of slice is: \t\t{id(slice)}")