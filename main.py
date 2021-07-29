num_1 = int(input("Enter your number: "))
num_2 = int(input("Enter 2nd your number: "))
print("+:sum \n-:minus \n*:multiple \n/:divide\n^:power")
status = input("enter your status")
if (status == "+"):
    print(num_1 + num_2)
elif (status == "-"):
    print(num_1 - num_2)
elif (status == "*"):
    print(num_1 * num_2)
elif (status == "/"):
    print(num_1 / num_2)
elif(status=="^"):
    print(num_1 ** num_2)
# elif(status==""):
#    print(num_1 - num_2)
