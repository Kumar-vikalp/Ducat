# area and perimeter of Circle
r=int(input("enter radius:"))

pi=3.141592653589793

a="area of Circle is",pi*(r*r)
p="Perimeter of Circle is",2*pi*r

c=input("enter what u want area/Perimeter of Circle: ")

if c=="Area":
    print(a)
elif c=="Perimeter":
    print(p)
    
else:
    print ("\nyou have to choose from area/Perimeter \nprobably you got the typing mistake plz type\nArea = Area\nPerimeter = Perimeter")

    
