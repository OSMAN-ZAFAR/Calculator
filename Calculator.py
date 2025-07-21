while True:
 print("Hey there is your personal AI calculator")
 print("kindly choose the number for the desire operation") 
 print(". 1 for Addition")
 print(". 2 for Subtraction")
 print(". 3 for Multiplication")
 print(". 4 for Division")
 a = int(input("Your selected number =  "))
 if a == 1:
    x= int(input("Enter first number: "))
    y= int(input("Enter second number: "))
    print("Answer = ", x+y)
 elif a == 2:
    x= int(input("Enter first number: "))
    y= int(input("Enter second number: "))
    print("Answer = ", x-y)
 elif a == 3:
    x= int(input("Enter first number: "))
    y= int(input("Enter second number: "))
    print("Answer = ", x*y)
 elif a == 4:
    x= int(input("Enter first number: "))
    y= int(input("Enter second number: "))
    print("Answer= ", x/y) 
 else:
    print("your choice is invalid ") 
 re =input("Do you want to retry? yes or no   ")
 if re != "yes":
  break