# The prime factors of 13195 are 5,7,13 and 29.
# What is the largest prime factor of the number 600851475143?


#SOLUTION-1
import math 
def maxPrimeFactors (n): 
    maxPrime = -1

    while n % 2 == 0: 
        maxPrime = 2
        n >>= 1    

    for i in range(3, int(math.sqrt(n)) + 1, 2): 
        while n % i == 0: 
            maxPrime = i 
            n = n / i 

    if n > 2: 
        maxPrime = n 
    return int(maxPrime) 

n = 600851475143
print(maxPrimeFactors(n)) 

#SOLUTION-2


def prime_check(x): 
    is_Prime = True

    for i in range(2, int(math.sqrt(x)) + 1): 
        if x % i == 0: 
            is_Prime = False
            continue
    return is_Prime
number= 600851475143
biggest_prime=1
for i in range(2, int(math.sqrt(number))): 
        if number % i == 0 and prime_check(i):
            biggest_prime = i

print(biggest_prime)