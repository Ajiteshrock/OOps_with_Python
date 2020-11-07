import math
def isprime(n):
    ct=0
    
    for i in range(2,int(math.sqrt(n)+1)):
        if (n%i)==0:
            ct+=1
        
    if(ct<1):
        return True
    else:
        return False
N = int(input())
l=[]
for i in range(4,N+1):
    if isprime(i)==True:
        l.append(i)

print(l)
