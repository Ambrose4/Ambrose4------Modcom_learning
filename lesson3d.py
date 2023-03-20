#lets do BMI
#below BMI is a loop of 5 times
#any code written the for loop,loops th specified number of times
#Any code inside the for loop must be indented

for value in range(1,6):
    weight = float(input("Enter your weight in Kgs:"))
    height = float(input("Enter your height in Meters:"))

    bmi = weight/(height * height)
    print("Your BMI",bmi)

    if bmi < 0:
        print("Error,please check your inputs,Enter Non Negative")

    elif bmi > 40:
        print("Invalid BMI,Try Again")

    elif bmi < 18.5:
        print("Under Weight")    

    elif bmi >= 18.5 and bmi < 22.9:
        print("Normal")   

    elif bmi >= 23 and bmi < 24.9:
        print("Overweight")     

    elif bmi >= 25 and bmi < 29.9:
        print("Pre.Obess")     

    elif bmi >= 30 and bmi < 34.9:
        print("Obess class 1")     

    elif bmi >= 35 and bmi < 39.9:
        print("Obess class 2")

    else:
        print("Obess class 3")         

# more on for loops and while loops
