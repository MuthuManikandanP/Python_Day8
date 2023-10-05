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
