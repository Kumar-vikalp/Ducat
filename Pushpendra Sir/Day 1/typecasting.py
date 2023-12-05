#typecasting = converting one datatype to another is known as typecasting
#two types of typecasting

# implicit
#typecasting that occurs automatically

x=10
y=4
print("value of x is",x,"data type is",type(x))
print("value of y is",y,"data type is",type(y))
z=x/y
print("value of z is",z,"data type is",type(z))

#output
``` 
value of x is 10 data type is <class 'int'>
value of y is 4 data type is <class 'int'>
value of z is 2.5 data type is <class 'float'>
```

# explicit
#to convert any data forefully

x="56"
print("value of x is",x,"data type is",type(x))
y=int(x)
print("value of y is",y,"data type is",type(y))

#output
``` 
value of x is 56 data type is <class 'str'>
value of y is 56 data type is <class 'int'>
```
