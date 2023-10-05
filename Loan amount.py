salary=int(input("Enter the Salary:"))
age=int(input("Enter the age:"))
if(salary>=20000 or age<=25):
    amt=int(input("Enter the required loan amt:"))
    if(amt>=50000):
       print("THE MAX LOAN AMOUNT IS 50000 ")
    else:
          print("ELIGIBLE")
else:
    print("NOT ELIGIBLE")

