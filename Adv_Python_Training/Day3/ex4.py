# area calculation
import math
print('==============================================================')


def calculateCircleArea():
    radious = input('Please enter radious of the circle to calculate area: ')
    if radious.isdigit():
        radious = int(radious)
        area = math.pi*(radious**2)
        print(f'The area of the circle having radious {radious} unit is {area} unit^2')
    else:
        print('Invalid radious value')


def calculateRectangleArea():
    x = input('Enter width of X side of the rectangle: ')
    y = input('Enter width of Y side of the rectangle: ')
    if x.isdigit() and y.isdigit:
        area = int(x) * int(y)
        print(f'Area of the rectangle having height {x} unit and width {y} unit is {area} unit^2')
    else:
        print('Invalid data entered')


def calculateTraingleArea():
    h = input('Enter height of traiangle: ')
    y = input('Enter base of traiangle: ')
    if h.isdigit() and y.isdigit:
        area = (int(h) * int(y))/2
        print(f'Area of the traingle having height {h} unit and base {y} unit is {area} unit^2')
    else:
        print('Invalid data entered')


def calculateArea(choosenFigure=''):
    choosenFigure = choosenFigure.lower()
    if choosenFigure == 'circle':
        calculateCircleArea()
    elif choosenFigure == 'rectangle':
        calculateRectangleArea()
    elif choosenFigure == 'traiangle':
        calculateTraingleArea()
    else:
        print('Wrong input')


def main():
    print("""
        Choose what you want to do
        1. type 1+Enter to calculate area of a circle
        2. type 2+Enter to calculate area of a traiangle
        3. type 3+Enter to calculate area of a rectangle
    """)
    userinput = input()
    if userinput.isdigit():
        if userinput == '1':
            calculateArea('circle')
        elif userinput == '2':
            calculateArea('traiangle')
        elif userinput == '3':
            calculateArea('rectangle')
        else:
            print('Invalid input')
    else:
        print('Invalid input')


main()
print('==============================================================')
