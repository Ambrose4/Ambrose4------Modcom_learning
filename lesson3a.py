#consider a primary a primary  school subjects,mark
maths = int(input("What did you get in Maths:"))
eng = int(input("What did you get in English:"))
kisw = int(input("What did you get in Kiswahili:"))
scie = int(input("What did you get in Science:"))
hist = int(input("What did you get in history:"))

#formula adding them up
marks = maths+eng+kisw+scie+hist
print("Your Total Marks is",marks)

#Make Decisons using marks
if marks < 0:
    print("Error,please check your inputs,Enter Non Negative")

elif marks > 500:
    print("Invalid Marks,Try Again")

elif marks < 100:
    print("Failed")        

elif marks >= 100 and marks < 250:
    print("You Have below Average")

elif marks >= 250 and marks < 300:
    print("You get Average")   

elif marks >= 350 and marks < 450:
    print("Above Average")

else:
    print("Great,Perfect marks")         




