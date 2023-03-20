#while loop
#function
#while loop
#below is where the loop stars
#while will work if value < 10 is true

value = 1 
while value < 10:
    print("Value is", value)
    weight = float(input("Enter your weight in Kgs:"))
    height = float(input("Enter your height in Meters:"))
    bmi = weight/(height * height)
    print("Your BMI",bmi)

    value = value + 1 # update value every loop-increameant