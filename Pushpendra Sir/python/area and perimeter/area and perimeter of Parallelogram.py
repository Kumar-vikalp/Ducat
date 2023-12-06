# area and perimeter of Parallelogram

c = input("Enter 'Area'/'Perimeter' of Parallelogram: ")

if c == "Area":
    h = float(input("Enter Height: "))
    b = float(input("Enter Base : "))
    area = b * h
    print("Area of Parallelogram is", area)

elif c == "Perimeter":
    a = float(input("Enter the value of side a: "))
    b = float(input("Enter the value of side b: "))
    perimeter = 2*a+b
    print("Perimeter of Parallelogram is", perimeter)

else:
    print("\nYou have to choose from area or perimeter \nProbably you got the typing mistake please type\nArea = Area\nPerimeter = Perimeter")

