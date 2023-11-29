#Find the largest palindrome made from the product of two 3-digit numbers.

#SOLUTION-1
def check_palindrome(x):
    str_number=str(x)
    reverse_number= str_number[::-1]
    if str_number == reverse_number:
        return True
    else:
        return False
a=0
b=0
big_palindrome=0
for i in range(100,1000):
    for j in range(100,1000):
        if check_palindrome(i*j) and i*j>big_palindrome:
            a=i
            b=j
            big_palindrome =i*j
            
print(big_palindrome)
print(a,b)

#SOLUTION 2
n = 0
for a in range(999, 100, -1):
    for b in range(a, 100, -1):
        x = a * b
        if x > n:
            s = str(a * b)
            if s == s[::-1]:
                n = a * b
print(n)