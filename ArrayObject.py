import array
import sys
# declaring a array
nums=array.array('i',[5,6,2,8,9])
print(type(nums))
print(id(nums))
print(sys.getsizeof(nums))
print(len(nums))  #getting length of array
print(nums[3])
print(nums[0])
print(nums[4])
nums[2]=5               #changing in array
print(nums[2])

del nums[4]
print(nums)
nums.append(11)
print(nums)

print(nums[-1]) #negative indexing is available in python
print(nums[0:5])
print(nums[0:10:2])
print(nums[10:0:-1])
print(nums[:])
print(nums[:5])
print(nums[3::1])
print(dir(array.array))
print(help(array.array))
