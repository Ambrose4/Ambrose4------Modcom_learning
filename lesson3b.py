# BMI stands for Body Mass Index
# How do we find BMI
#Formula: weight/height * height



weight = float(input("Enter your weight:"))
height = float(input("Enter your height:"))

bmi = weight/height * height
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

