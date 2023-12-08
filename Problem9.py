#A Pythagorean triplet is a set of three natural numbers, a<b<c, for which, 
#a^2+b^2=c^2
#There exists exactly one Pythagorean triplet for which a+b+c=1000.
#Find the pruduct abc.


done=False

for a in range(1,1000):
    for b in range(1,1000-a):
        c=1000-a-b
        if c*c == a*a + b*b:
            print(a*b*c)
            print(a,b,c)
            done=True
            break
    if done:
        break
    
