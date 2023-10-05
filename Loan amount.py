# Get input for salary and age.
# If salary greater than or equal to 20000 or age less than or equal to 25, get input for required loan amount. If not print you are not eligible for loan. 
# If required loan amount is less than or equal to 50,000 print You are eligible for loan. If it is greater than 50,000 print maximum loan amount is 50000.

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

