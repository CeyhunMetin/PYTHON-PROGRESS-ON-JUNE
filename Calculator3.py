print ("""



Welcome to Calculator 3.0


""")
a= float (input("Please enter first number:"))
b= float (input("Please enter second number:"))

operation=input("Which operation would you like to do?(+,-,*,/):")

def acc(a,b):
    return a+b

def sub(a,b):
    return a-b

def mltp(a,b):
    return a*b

def dvd(a,b):
    return (a/b)

if (operation == "+"):
    print(acc(a,b))

elif (operation=="-"):
    print(sub(a,b))

elif (operation == "*"):
    print(mltp(a,b))

elif (operation == "/"):
    print(dvd(a,b))
   

else:
    print ("Wrong operation entered.")      

print ("www.github.com")
