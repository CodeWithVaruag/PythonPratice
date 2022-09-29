import array
nums=array.array('i',[])
a=int(input("enter a number : "))
nums.append(a)


b=(input("do you want to add more numbers (y/n) : "))
while b=="y":
    a = int(input("enter a number :"))
    nums.append(a)
    print(nums)
    b = (input("do you want to add more numbers (y/n) : "))
if b=="n" :
    print(nums)