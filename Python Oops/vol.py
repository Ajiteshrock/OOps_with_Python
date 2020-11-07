t = int(input())
while(t):
    n = int(input())
    max = 0
    vol=0
    for i in range(n,1,-1):
        vol = n**3 - (i-1)**3
        #print(vol)
        if(max<vol):
            max=vol
            #print(max)
    print(max)
    t-=1