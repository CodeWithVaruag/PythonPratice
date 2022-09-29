z=input("enter value between 1 to 7 : ")
value=int(z)
# if(value==1):
#     print("sunday")
# elif(value==2):
#     print("monday")
# elif(value==3):
#     print("tuesday")
# elif(value==4):
#     print("wednesday")
# elif(value==5):
#     print("thrusday")
# elif(value==6):
#     print("friday")
# elif(value==7):
#     print("saturday")
# else:
#     print("out of range")


if(value<=7) and (value>=1):
    match value:
        case 1:
            print("sunday")
        case 2:
            print("monday")
        case 3:
            print("tuesday")
        case 4:
            print("wednesday")
        case 5:
            print("thrusday")
        case 6:
            print("friday")
        case 7:
            print("saturday")
else:
    print("out of range")

