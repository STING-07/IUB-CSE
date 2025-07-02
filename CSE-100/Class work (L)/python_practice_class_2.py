
a = input()

b = input()

print(a , b)

c = a+b

print(c)

a = int (input())

b = int (input())

print(a) , (b)

c = a+b

print(c)

#7

a = int (input())

b = int (input())

div = a/b
fdiv = int(a/b)
exp = a**b

print(div, '\n', fdiv, '\n' , exp)

#8
a = int (input())
b = int (input())

test = a==b

print(test)

#9

a = 5
b = 3

print("before: \na:", a, "b:" , b)

a, b = b, a

print("after:", a, "\nb:" , b)

#11

length = float (input("enter the length:"))
width = float (input("enter the width:"))

area = length * width

print(f"the area is:, {area:.3f}.,")

length = float (input("enter the length:"))
width = float (input("enter the width:"))

area = length * width

print(f"the area of the rectangle is: {area:.3f}.")

#12
r = float (input("enter the radius:"))
pi = 3.1416
area =2*pi*r
print (area)

#13

C = float(input("Enter temperature: "))

print(f"The temperature in fahrenheit:{(C*9/5) + 32} ")

#14

n = int(input("per day comsumption:"))

print(f"total number of cigarettes smoked in a year: {365*n}")
