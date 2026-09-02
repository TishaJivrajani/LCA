# write a python program that accepts the length of three sides of a traiangle as inputs.
# The program should indicate wether or not the traingle is a right angled triangle using function.

def triangle():

    a = int(input("enter first side of triangle: "))
    b = int(input("enter second side of triangle: "))
    c = int(input("enter third side of triangle: "))

    if a > b and a > c:
        greatest = a

    elif b > a and b > c:
        greatest = b

    elif c > a and c > b:
        greatest = c

    larger_side = greatest*greatest
    if greatest==a:
        if larger_side == b*b + c*c:
            print("RIGHT ANGLED TRIANGLE")
        else:
            print("NOT A RIGHT ANGLED TRAINGLE")
    elif greatest ==b:
        if larger_side == a*a + c*c:
            print("RIGHT ANGLED TRIANGLE")
        else:
             print("NOT A RIGHT ANGLED TRAINGLE")
    elif greatest ==c:
        if larger_side == b*b + a*a:
            print("RIGHT ANGLED TRIANGLE")
        else:
             print("NOT A RIGHT ANGLED TRAINGLE")

triangle()