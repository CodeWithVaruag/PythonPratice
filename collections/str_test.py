fname = input("enter your name :")

while True:

    if fname.isalpha():
        print("your name is {}".format(fname))
        break

    else:
        print("enter valid name")
        break
