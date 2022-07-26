#Задана последовательность натуральных чисел, завершающаяся числом 0. Требуется определить значение второго по величине элемента в этой последовательности, то есть элемента, который будет наибольшим, если из последовательности удалить наибольший элемент.
num=input("write a numbers")
arr=list(map(int,num.split()))
print(arr)
for j in range(len(arr)-1):
    for y in range(len(arr)-1):
        if arr[y]>arr[y+1]:
            temp=arr[y+1]
            arr[y+1]=arr[y]
            arr[y]=temp
print((arr[len(arr)-2]))
