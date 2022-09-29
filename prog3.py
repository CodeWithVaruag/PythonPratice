sid=input("Enter a sid : ")
name=input("Enter a name :")
sub1=input("Enter a marks in subject1  :")
sub2=input("Enter a marks in subject2 : ")
sub3=input("Enter a marks in subject3 : ")
a=int(sub1)
b=int(sub2)
c=int(sub3)
total=a+b+c
average=total/3
print("total marks of {} is {}".format(name,total))
print("average is {} ".format(average))


if a>=40 and b>=40 and c>=40:
    result="pass"
else:
    result="fail"

    print(result)
