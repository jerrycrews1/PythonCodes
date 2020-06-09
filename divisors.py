def divisors(num):
    list_of_divisors = [i for i in range(2, num) if (num % i == 0) & (num != i)]
    if not list_of_divisors:
        list_of_divisors.append(f'{num} is prime')
    print(list_of_divisors)


divisors(10)
divisors(5)
divisors(10002)
