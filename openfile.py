

#Instantiate empty xml list.
xmllist=[]

#Open xml file and read in contents. Print contents.
with open("untitled.txt","r") as f:
	xmllist.append(f.read())
	f.close()
print(xmllist)

#Test to ensure variable type is list and print results.
typetest=type(xmllist)
print(f"\n{typetest}")

#Test that file is open and in read mode.
if f.mode=='r':
	print("File is open and in read mode.")
else:
	print("File is probably in write mode.")

#Append new xml tagged data to list and print results.
xmllist.append("<tag2>text2</tag2>")
print(xmllist)

with open("untitled.txt","w+") as f:
	for element in xmllist:
		f.write(element)
	f.close

#print(cat untitled.txt)


#for element in MyList:
#    print >>MyFile, element
#MyFile.close()