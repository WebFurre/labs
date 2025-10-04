num=float(input("Введите число: "))

while num<1 or int(num)!=num:
    print("число должно быть натуральным!!!!!!")
    num=float(input("Введите число: "))
num=int(num)

for i in range(1,num+1):
    print(i)