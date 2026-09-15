def is_fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n


mnozhyna = set(range(1, 51))

fib_chysla = {x for x in mnozhyna if is_fibonacci(x)}

print("Множина:", mnozhyna)
print("Числа Фібоначчі:", fib_chysla)
print("Кількість чисел Фібоначчі:", len(fib_chysla))