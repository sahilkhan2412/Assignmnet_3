a=input("Enter a number:")
num=int(a)

def factorial(num):
    if num==1:
        return 1
    else:
        return num*factorial(num-1)
result=factorial(num)
print("Factorial of ",num,"is:",result)