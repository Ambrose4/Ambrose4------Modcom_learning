# function - a function perform a specific/related task
# A bigger program can be split into small function
# A function split a big code to small portion
# Functions make code easy to understand/manage
# We create a function using "def" keyword followed by 
# function name, folowed by brackets/parenthesis


def converter():
    money = float(input("Enter Money in USD:"))
    answer = money * 110
    print("Your Money in USD", money)
    print("Your Money in KES", answer)


def area():
    radius = float(input("Enter Radius:"))
    answer = 3.14 * radius * radius
    print("Your Area is", answer)


# create a function find simple interest. PRT/100

def SInterest():
    p = float(input("Enter Principal:"))
    r = float(input("Enter Rate:"))
    t = float(input("Enter Time:"))
    answer = p * r * t / (100)
    print("Your Simple Interest is", answer)

# Function must be called
# caller function use function name followed ()
converter()
area()
SInterest()
