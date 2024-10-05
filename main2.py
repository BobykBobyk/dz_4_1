input1 = input("Your string: ")

list1 = []

for i in input1:
    list1.append(i)

first = list1[0]

list2=[]

for i in list1:
    if i == first:
        list2.append(i)

print(len(list2))
