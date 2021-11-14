def prime_sum(n: int):
    # Takes the sum of all primes up to n

    # Sieve of Eratosthenes
    prime_list = [True for i in range(n)]    
    p = 2

    while (p ** 2 <= n):
        if prime_list[p] == True:
            for i in range(p ** 2, n, p):
                prime_list[i] = False
        p += 1
    
    prime_list[0] = False
    prime_list[1] = False

    # Sum primes
    prime_sum = 0
    for i, prime in enumerate(prime_list):
        if prime:
            prime_sum += i
    
    return prime_sum


print(prime_sum(2000000))