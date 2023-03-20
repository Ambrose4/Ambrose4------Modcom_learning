# TODO
# 1.Create function to find bmi: weight and height are parameters
# 2.Create a function to convert degree celicius to degree fahreheit

def BMI (weight, height):
    answer = weight/(height * height)
    print("Your BMI",answer)


BMI(weight=90, height=2)
BMI(weight=70, height=1) 
BMI(weight=80, height=1.5)   


def converter (celcius):
    answer = (celcius *1.8) +32
    print("Fahreheit is", answer)

converter(celcius=20)    
