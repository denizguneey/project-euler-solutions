#The sum of the squares of the first ten natural numbers is,
#1^2+2^2+...+10^2=385.
#The square of the sum of the first ten natural numbers is,
#(1+2+...+10)^2=55^2=3025.
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 
#3025-385=2640.
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum. 

#SOLUTION-1
sum_of_squares=0
square_of_sum=0

sum=0

for i in range(1,101):
    sum +=i
    sum_of_squares += i*i
result = sum*sum- sum_of_squares
print(result)

#SOLUTION-2
square_sum, sum_square = 0,0
for i in range(1,101):
    square_sum += i**2
    sum_square += i
print(sum_square**2 - square_sum)