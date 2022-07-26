#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N. Факториал

num=int(input("write a number"))
x=1
if num==0 or num==1:
    print(1)
elif num>1:
    for y in range(1,num+1):
       x=y*x
print(x)