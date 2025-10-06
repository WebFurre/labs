def max_of_two(x, y):
    if x>=y:
        return x
    else:
        return y

x=int(input("Введите первое число: "))
y=int(input("Введите второе число: "))
print("Большее число:", max_of_two(x,y))

