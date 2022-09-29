
dict1={"id":1,"name":"gaurey"}
dict2={"id":1,"address":"satdobato","email":"gauravdahal321@gmail.com"}
print(help(dict))

dict2={"id":2,"address":"koteshowr","email":"kmahancyhainara@gmail.com"}
print(dict1)
dict1.clear()
print(dict1)

dict3=dict2 #copy by refernce(address)
print(dict3)

print(id(dict2))
print(id(dict3))

dict4=dict3.copy() #allocte diffrent memory adress(copy by value)
print(dict4)
print(id(dict4))

print(dict2["id"])
print(dict2.get("id"))
result=dict2.items()
# print(result[0]) error

for item in result:
    print("{} = {}".format(item[0],item[1]))

print(dict2.keys())

for i in dict2.keys() :
  print(dict[i])


dict2={"id":1,"address":"satdobato","email":"gauravdahal321@gmail.com"}
print(dict2.popitem())
print(dict2)

dict2={"id":1,"address":"satdobato","email":"gauravdahal321@gmail.com"}
dict2.setdefault("country","nep")
print(dict2)

dict2.setdefault("phone")
print(dict2)

print(dict2.values())

for values in dict2.values():
    print(values)