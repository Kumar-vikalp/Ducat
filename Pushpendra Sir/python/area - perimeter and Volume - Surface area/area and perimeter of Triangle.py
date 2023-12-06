# area and perimeter of Triangle
c = input("Enter 'Area' or 'Perimeter' of Triangle: ")

if c == "Area":
    h = float(input("Enter Height: "))
    b = float(input("Enter Breadth: "))
    area = 0.5 * b * h
    print("Area of Triangle is", area)

elif c == "Perimeter":
    a = float(input("Enter the value of side a: "))
    b = float(input("Enter the value of side b: "))
    c = float(input("Enter the value of side c: "))
    perimeter = a + b + c
    print("Perimeter of Triangle is", perimeter)

else:
    print("\nYou have to choose from area or perimeter \nProbably you got the typing mistake please type\nArea = Area\nPerimeter = Perimeter")

