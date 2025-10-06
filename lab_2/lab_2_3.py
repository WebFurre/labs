def is_prime(number):
    if number<=1:
        return False
    for i in range(2,number):
        if number%i==0:
            return False
    return True

number=int(input("Введите число: "))

if is_prime(number):
    print(f"число {number} - простое")
else:
    print(f"число {number} - не простое")