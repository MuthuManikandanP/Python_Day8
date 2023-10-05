#Make a mini calculator. Get input for 2 numbers a and b. Get input from user whether to add/sub/mul/div. If user selects add then add the two number and Print the result.


a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
op=input("add/sub/mul/div:")
if(op=="add"):
    print(a+b)
elif(op=="sub"):
    print(a-b)
elif(op=="mul"):
    print(a*b)
elif(op=="div"):
    print(a/b)
else:
    print(" Invalid operation")
