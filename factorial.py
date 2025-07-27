#BY LOOPS
def fac(a):
    fac1 =1
    for i in range(1,a+1):
        fac1 *=i
    print(fac1)

fac(5)

#BY RECURSION
def fac_(n):
    if(n==0 or n==1):
        return 1
    else:
        return fac_(n-1)*n

print(fac_(5))