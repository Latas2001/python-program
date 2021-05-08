def unique(l):
    s=[0]
    for i in range(1,len(l)):
        s=s*l[i]
        return s
    l=[int(i) for i in input().split()]
    z=unique(l)
    print(z)
    
