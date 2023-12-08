#The sum of the primes below 10 is 2+3+5+7=17.
#Find the sum of all the primes below two million.

import math
prime_list=[]
prime_list.append(2)

n=2

while True:
    is_prime=True
    for i in prime_list:
        if i>int(math.sqrt(2*n-1)):
            break
        if (2*n-1) % i==0:
            is_prime=False
            break
    if is_prime:
        prime_list.append(2*n-1)
    n+=1
    if 2*n-1>=1000:
        break
print(sum(prime_list))