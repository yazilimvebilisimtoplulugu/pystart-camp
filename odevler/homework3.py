list1=[]
numbers=int(input("enter the first number"))
list1.append(numbers)
numbers1=int(input("enter the second number"))
list1.append(numbers1)
numbers2=int(input("enter the third number"))
list1.append(numbers2)
print(numbers, numbers1, numbers2)
numbers3=int(input("enter the forth number"))
list1.append(numbers3)
list1.sort()
print(list1)
k1=min(list1)
k2=max(list1)
average=(numbers+ numbers1 +numbers2+ numbers3)/4
print(k1, k2, average)
list1.sort()
list1.pop(0)
print(list1)
newaverage= list1[0] + list1[1] + list1[2]
final=newaverage/3
print(final)