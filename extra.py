# 1. Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи

n = int(input('Input your number: '))
arr = [0, 1]

def fibo(n):
    for i in range(n):
        arr.append(arr[i] + arr[i + 1])
    return arr
    
print(fibo(n))