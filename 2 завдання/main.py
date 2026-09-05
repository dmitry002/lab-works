from function1 import calculate
from function2 import numbers

print("1 - Обчислити значення виразу")
print("2 - Знайти числа, кратні 3, від 30 до 60")

choice = int(input("Ваш вибір: "))

if choice == 1:
    a = float(input("Введіть a: "))
    b = float(input("Введіть b: "))
    x = float(input("Введіть x: "))

    y = calculate(a, b, x)

    print("y =", y)

elif choice == 2:
    result = numbers()

    print("Числа, кратні 3:", result)
    print("Їх кількість:", len(result))

else:
    print("Неправильний вибір")