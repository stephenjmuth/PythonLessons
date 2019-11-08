from string import ascii_lowercase
print(ascii_lowercase)
letters=ascii_lowercase
LenOfAlphabet=len(letters)
print(LenOfAlphabet)
alphabet=list(letters)
print(alphabet)
i=0
for letter in letters:
	spaces=' '*i
	print(f"{spaces}{letter}")
	i+=1
