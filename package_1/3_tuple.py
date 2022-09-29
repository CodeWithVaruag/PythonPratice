# # declare
# import sys
#
# # tup1=tuple()
# tup1=(2,5,8,15)
# print(tup1)
# print(type(tup1))
# print(id(tup1))
# print(sys.getsizeof(tup1))
# print(len(tup1))
#
# list1=[3,5,8,10,16]
# tup1=tuple(list1) #type conversion list to tuple
# print(tup1)
#
import array

# arr1=array.array('i',[5,6,8,12,10])
# tup1=tuple(arr1)
# print(tup1)
# print(type(tup1))

# indexing and slicing


tup1 = 8, 4, 2, 8, 9, 90, 56
print(type(tup1))
print(tup1[6])
print(tup1[4:6])
print(tup1[-2])

tup2 = tup1[0:len(tup1)]
print(tup2)

# tup1[7]=15
print(tup1)

tup1=8,0,12,34,67,90
print(tup1.index(1,0,len(tup1)))



