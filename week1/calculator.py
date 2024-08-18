import math as p
#that are intiger value
x =int(input("What's x "))
y =int(input("Whats Y "))
#z=int(x)+int(y)
#print(z)
print(x+y)
#we can make it with float
m= float(input("What is your X"))
q=float(input("What is your Y"))
print(m+q)\
#we can use round tho nearest value
k=float(input("What is x"))
j=float(input("What is x"))
f=round(k+j)
print(f"{f:,}")
# if we use ":," then its give us a , in thousend like 1,000 insted of 1000
x =int(input("What's x "))
y =int(input("Whats Y "))
z=x/y
print(f"{z:.2f}")

def main():
    x=int(input("What's x?" ))
    print("x squared is", squared(x))
def squared(o):
    #return o*o
#another way we can fix this thing up is
    return pow(o,2)
main()
