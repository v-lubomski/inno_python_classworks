# Задание 2
# Написать генератор последовательности Фибоначчи.


def fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a+b


print(list(fibonacci(10)))