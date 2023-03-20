# function can have parameters
# below base and height are parameters with no values
def area(base, height):
    #base = 3
    #height = 8
    answer = 0.5 * base * height
    print("Your Area is", answer)

# when calling the function provide values for base and height
# below we re use area() 4 times,but with different base and height
area(base=4, height=8)
area(base=1, height=6)
area(base=5, height=10)
area(base=40, height=30)
