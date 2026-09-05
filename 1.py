def function(a, b):
    if a > b:
        x = a * b + 1
    elif a == b:
        x = 25
    else:
        x = (a - 5) / b

    return x


a = float(input("Введіть a: "))
b = float(input("Введіть b: "))

x = function(a, b)

print("x =", x)