def tribonacci(signature, n):
    for i in range(n):
        signature.append(sum(signature[-3:]))
    return signature


def fibonacci(signature, n):
    for i in range(n):
        signature.append(sum(signature[-2:]))
    return signature


print(fibonacci([2, 3], 10))
print(tribonacci([0, 0, 1], 10))
print(tribonacci([0, 1, 1], 10))
