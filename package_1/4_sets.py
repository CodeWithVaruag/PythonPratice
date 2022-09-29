# declare AND INITIALIZE
import sys
from array import array

set1={1,57,8,9,15,12,13}
print(type(set1))
print(len(set1))
print(sys.getsizeof(set1))
print(set1)
# print(set1[2])
# print(set1[:])

arr1=array('i',[5,1,2,3,23,25,89])
list1=[1,5,8,10,45,5,89]


set1=list(set1)
print(set1)

set1=tuple(set1)
print(set1)

# iterating set
set1={1,5,8,10,23,11,25,14}
print(set1)

for item in set1:
    print(item)

# add(),clear(),copy(),pop(),discard(),intersection()




