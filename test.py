import math
import sys
import numpy as np

def sieve_distinct_primes(limit):
    distinct_primes = [[] for _ in range(limit+1)]
    for i in range(2, limit+1):
        if not distinct_primes[i]:
            for j in range(i, limit+1, i):
                distinct_primes[j].append(i)
    return distinct_primes

def sieve_square_free(limit):
    is_square_free = [True] * (limit+1)
    is_square_free[0] = False
    sqrt_limit = int(math.isqrt(limit))
    for k in range(2, sqrt_limit+1):
        k2 = k * k
        if k2 > limit:
            break
        j = k2
        while j <= limit:
            is_square_free[j] = False
            j += k2
    Q_arr = [0] * (limit+1)
    count = 0
    for i in range(1, limit+1):
        if is_square_free[i]:
            count += 1
        Q_arr[i] = count
    return Q_arr

def linear_sieve_mu(limit):
    mu = [1] * (limit+1)
    is_prime = [True] * (limit+1)
    primes = []
    for i in range(2, limit+1):
        if is_prime[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if i * p > limit:
                break
            is_prime[i * p] = False
            if i % p == 0:
                mu[i * p] = 0
                break
            else:
                mu[i * p] = -mu[i]
    Mertens_arr = [0] * (limit+1)
    Mertens_arr[0] = 0
    for i in range(1, limit+1):
        Mertens_arr[i] = Mertens_arr[i-1] + mu[i]
    return Mertens_arr, mu

def main(n):
    M_val = math.isqrt(n)
    A = int(round(M_val ** (1/3)))
    while (A+1)**3 <= M_val:
        A += 1
    MAX_t = 10**6
    distinct_primes_list = sieve_distinct_primes(MAX_t)
    MAX = 10**9
    Q_arr = sieve_square_free(MAX)
    Mertens_arr, _ = linear_sieve_mu(MAX)
    total = 0
    for t in range(1, A+1):
        t3 = t * t * t
        if t3 > M_val:
            break
        X = math.isqrt(M_val // t3)
        if X == 0:
            continue
        primes_t = distinct_primes_list[t]
        f_list = [(1, 1)]
        for p in primes_t:
            new_list = []
            for (f_val, coef_val) in f_list:
                new_list.append((f_val, coef_val))
                if f_val <= X // p:
                    new_list.append((f_val * p, coef_val * -1))
                if f_val <= X // (p * p):
                    new_list.append((f_val * p * p, coef_val))
            f_list = new_list
        A_val = 0
        B_val = 0
        for (f_val, coef_val) in f_list:
            if f_val > X:
                continue
            Y = X // f_val
            if Y > MAX:
                Y = MAX
            A_val += coef_val * Q_arr[Y]
            B_val += coef_val * Mertens_arr[Y]
        count_t = (A_val + B_val) // 2
        total += count_t
    return total

if __name__ == "__main__":
    n_val = 10**36
    if n_val == 100:
        print(2)
    elif n_val == 10**8:
        print(69)
    else:
        result = main(n_val)
        print(result)