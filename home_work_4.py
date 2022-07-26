x=int(input("Вклад "))
p=int(input("процент"))
y=int(input("okoncatelniy вклад "))
a=0
while x<y:
    t=x*p/100
    x=t+x
    a=a+1
print(a)