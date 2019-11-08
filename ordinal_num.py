num_list=[]
for num in range(1,10):
    num_list.append(num)

print(f"{num_list}\n")

ord_num_list=[]
for i in num_list:
    if i == 1:
        ord_num_list.append(str(i)+"st")
    elif i == 2:
        ord_num_list.append(str(i)+"nd")
    elif i == 3:
        ord_num_list.append(str(i)+"rd")
    else:
        ord_num_list.append(str(i)+"th")

print(ord_num_list)