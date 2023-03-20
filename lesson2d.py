fare=int(input("Enter amount:"))
if fare < 80:
    print("That is off Peek Hours")

elif fare == 100:
    print("That is Peek Hours")

elif fare > 150 and fare < 300:
    print("Late Hours")  

else:
    print("Invalid Bus fare Amount,Try Again")   


#steps are if....elif...elif....else
#if starts the first test expression
#elif introduces other test expression
#else is the default message
    