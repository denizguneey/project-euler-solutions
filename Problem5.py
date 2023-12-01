#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import math
import functools

def gcd(x,y):
    return math.gcd(x,y)
def lcm(x,y):
    return (x*y) // gcd(x,y)

list = range(1,21)

result = functools.reduce(lcm,list)
print(result)