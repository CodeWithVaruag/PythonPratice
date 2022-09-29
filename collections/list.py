# ccllections
# list
# any value any numbers
# numbers only - any numbers -array
# any type values: any numbers -list
import sys
from array import array
from statistics import mean

# declare
list1= [2,3,5,9,55,23,59,565,45,2,36]
# print(type(list1))
# print(id(list1))
# print(len(list1))
# print(list1)
# print(sys.getsizeof(list1))
# print(sum(list1))
# print(min(list1))
# print(max(list1))
# print(mean(list1))
# arr1=array('i',[])
# list2=[True,False,True,False,56,23]
# list1=list(arr1)
# print(type(list1))
print(list1)


for item in list1:
    print(item)

start=0
while(start<=len(list1)-1):
    print(list1[start],end=' ')
    start+=1