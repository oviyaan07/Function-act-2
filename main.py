def add(num1, num2):
    print (f"number 1: {num1}")
    print (f"number 2: {num2}")
    sum=num1+num2
    return sum
def sub(num1, num2):
    print (f"number 1: {num1}")
    print (f"number 2: {num2}")
    diff=num1-num2
    return diff
def mult(num1, num2):
    print (f"number 1: {num1}")
    print (f"number 2: {num2}")
    pro=num1*num2
    return pro
def div(num1, num2):
    print (f"number 1: {num1}")
    print (f"number 2: {num2}")
    quo=num1/num2
    return quo
num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
s=add(num1, num2)
print ("sum ", s)
d=sub(num1, num2)
print ("difference ", d)
m=mult(num1, num2)
print ("product", m)
di=div(num1, num2)
print ("quo", di)