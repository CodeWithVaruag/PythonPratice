from array import array

list1=[1,5,8,45,89,563,5445,10,32,15,15,89]
ar=array('i',[5,89])
# print(list1.count(15))
# print(list1.index(15,0,len(list1)-1))
print(list1)
list1.extend(ar)
print(list1)

list1.insert(3,56)
print(list1)

list1.append(23)
print(list1)

list1.pop()
list1.pop()
list1.pop()
list1.pop()
list1.pop()

print(list1)

list2=[2,10,10,8]
list2.remove(10)
print(list2)

list2.reverse()
print(list2)

list2.sort()
list2.sort(reverse=False)
list2.sort(reverse=True)
arr1=array('i',list2)
print(arr1)
arr1=list(arr1)
print(arr1)