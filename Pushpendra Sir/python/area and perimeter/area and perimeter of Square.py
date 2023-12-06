# area and perimeter of Square
s=int(input("enter side:"))
a="area of Square is",s*s
p="Perimeter of Square is",4*s
c=input("enter what u want Area/Perimeter of Square: ")
if c=="Area":
    print(a)
elif c=="Perimeter":
    print(p)
else:
    print ("\nyou have to choose from area/Perimeter \nprobably you got the typing mistake plz type\nArea = Area\nPerimeter = Perimeter")
