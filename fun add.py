def solve_me_first(m,n):
    m=int(input("Enter the value of a: "))
    n=int(input("Enter the second number: "))
    res=solve_me_first(m,n)
    print(res)
    return m+n;
