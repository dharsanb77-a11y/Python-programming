def multiply(x):
    return x*3
def add(x):
    return x+10
print(add(multiply(5)))
def square(x):
    return x**2
def mul(x):
    return x*2
def sub(x):
    return x-5
print(sub(mul(square(4))))
def compose(f,g):
    return lambda x:f(g(x))
def add10(x):
    return 10+x
def mul5(x):
    return x*5
def sub3(x):
    return x-3
pr=compose(add10,mul5)
print(sub3(pr(2)))
def greeting(name):
    def message():
        print("Hello ",name)
    return message
pr=greeting("Dharsan")
pr()

def counter():
    count=0
    def increment():
        nonlocal count
        count=count+1
        print(count)
    return increment
md=counter()
for i in range(5):
    md()
def discount(percent):
    def calculate(price):
        return price-((percent/100)*price)
    return calculate
d=discount(10)
print("Remaining: ",d(1000))
m=discount(20)
print("Remaining: ",m(1000))
from functools import partial
def add(a,b):
    return a+b
m=partial(add,100)
print(m(50))
print(m(200))
def power(base,exp):
    return base**exp
sq=partial(power,exp=2)
c=partial(power,exp=3)
print(sq(4))
print(c(4))
def tax(pr,tx):
    return pr*(tx/100)
m=partial(tax,tx=18)
print(m(1000))
print(m(2000))
print(m(5000))
def calculation(mt,a,b):
    return mt(a,b)
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def pro(x,y):
    return x*y
def div(x,y):
    return x//y
choice=int(input("Enter Choice"))
match choice:
    case 1:
        print(calculation(add,2,3))
    case 2:
        print(calculation(sub,5,2))
    case 3:
        print(calculation(pro,2,4))
    case 4:
        print(calculation(div,10,4))
    case _:
        print("Default")
        


        
        
