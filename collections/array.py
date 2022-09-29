
from random import random, randrange
from statistics import mean

import array
# nums=array.array('i',[])
#
# nums.append(5)
# nums.append(9)
# print(nums)
# tmp=input("enter a number")
# tmp=int(tmp)
# nums.append(tmp)
# print(nums)
# str="3"
# nums.append(int(str))
# print(nums)

#Buffer_info(self,/)
# print(nums.buffer_info())

#Byteswap(self,/)
# print(nums.byteswap())

#count(self,v,/)

# nums = array.array('i',[3,5,6,1,2,8,4,1])
# result = nums.count(1)
# print(result)


#extend(self,bb,/)
# arr1=array.array('i',[2,3,4,5,6])
# arr2= array('i',[7,8,9,10])
# arr1.extend(arr2)
# print(arr1)


#Index(self,v,start=0, stop=9223372036854775807,/)
# nums= array.array('i',[3,4,3,1,2,6,7,8,2,10])
# tmp=11
# result=nums.index(tmp,0, len(nums)) #ValueError: array.index(x): x not in array
# print(result)


# nums=array.array('i',[8,6,7,8,5,2,3,1])
# tmp=20
# result=nums.count(tmp)
# if result>0:
#     result2= nums.index(tmp,0,len(nums))
#     print("{} found at {}".format(tmp,result2))
#
# else:
#     print("{} found at {}".format(tmp))

#Random number
# print(random()) #0.7212299263280593
# print(random())
# nums=randrange(100)
# print(nums)
# print(randrange(0, 22))


# #Looping
# for i in range(0,4):
#     print(randrange(5, 10), end=' ')

# ages=array.array('i',[])
# for i in range(0,12):
#         ages.append(randrange(17,23))
# print(ages)
# print(len(ages))
# print(max(ages))
# print(min(ages))
# print(sum(ages)/len(ages)) #print(mean(ages))
#
#
#
# tmp = input("Enter age to find:")
# tmp=int(tmp)
# count = ages.count(tmp)
# if count>0:
#     print("{} found {} time(s)".format(tmp,count))
# else:
#     print("{}  not found ".format(tmp))

# sorting array element(asc/desc)
nums=array.array('i',[4,5,1,2,6,0,-1])
print(nums.sort())
# nested loop with value compare and swap
