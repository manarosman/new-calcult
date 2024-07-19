num1=float(input('Enter num1 :  '))
num2=float(input('Enter num2 :  '))
p= input()
def g(x,y):
    return x+y
def a(x,y):
    return x-y
def b(x,y):
    return x/y
def c(x,y):
    return x*y
if p == '+':
    print(g(num1,num2))
elif p =='-':
    print(a(num1,num2))
elif p =='/':
    print(b(num1,num2))   
elif p =='*':
    print(c(num1,num2))     

