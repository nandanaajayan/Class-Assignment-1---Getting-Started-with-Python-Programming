#1.
a=input("enter the string 1:")
b=input("enter the string 2:")
if (a==b):
  print("two strings are equal")
else:
  print("two strings are not equal")

  #2.
a=int(input("enter the number 1:"))
b=int(input("enter the number 2:"))
c=a+b
print("sum of",a,"and",b,"=",c)


#3.
a=int(input("enter the number"))
sqrt=a**(1/2)
print("square root of",a,"=",sqrt)

#4.
b=int(input("enter the base"))
h=int(input("enter the height"))
area=1/2*b*h
print("area of traiangle:",area)

#5.
c=int(input("enter the celsius degree"))
f=(c+9/5)+32
print("fahrenheit is",f)

#6.
n=int(input("enter the number"))
if (n<=0):
  if (n==0):
    print("number is zero")
  else:
    print("number is negative")
else:
  print("number is positive")

#7.
a=int(input("enter the 1st number"))
b=int(input("enter the 2nd number"))
c=int(input("enter the 3rd number"))
if (a>=b and a>=c):
  print(a,"is the largest number")
elif (b>=a and b>=c):
  print(b,"is the largest number")
else:
  print(c,"is the largest number")
  
