import math
a=input("Enter a number:")
num=int(a)

def calculation(num):
    print("Square root:" , math.sqrt(num))
    print("Logarithm:" ,math.log(num))
    print("Sine:" ,math.sin(num))

print(calculation(num))



