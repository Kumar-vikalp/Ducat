# area and perimeter of rectangle
l=int(input("enter length:"))
w=int(input("enter widhth:"))
a="area of rectangle is",l*w
p="Perimeter of rectangle is",2*l+w
c=input("enter what u want A-rea/Perimeter of rectangle: ")
if c=="Area":
    print(a)
elif c=="Perimeter":
    print(p)
    
else:
    print ("\nyou have to choose from area/Perimeter \nprobably you got the typing mistake plz type\nArea = Area\nPerimeter = Perimeter")
