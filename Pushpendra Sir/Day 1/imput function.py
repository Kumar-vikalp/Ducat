# input function is used for user input
# default string
# string uses 1 byte data
# int uses 4 bytes of data
# string(numeric)/float ----> int :-int(data)

x = int(input("enter your number:"))
z=x*x
print("value of z is:",z)


x = input()
print("value of x is",x,"data type is",type(x))
y = int(x)
print("value of y is",y,"data type is",type(y))

