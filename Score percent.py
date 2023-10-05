#Get a input for score percentage. Only If the percentage is greater than 70, get input for his name, department and location. Then print you are elgibile. If not print you are not eligible.

score=int(input("Enter the Score Percent:"))
if(score>=70):
    name=input("enter the name:")
    dep=input("enter the dep:")
    loc=input("enter the loc:")
    print("ELIGIBLE")
else:
    print("NOT ELIGIBLE")
