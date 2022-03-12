def fib(n):
    mas = [0, 1]
    for i in range(n-2):
        s = mas[i] + mas[i+1]
        mas.append(s)
    return str(mas[-1])
print(fib(20))
