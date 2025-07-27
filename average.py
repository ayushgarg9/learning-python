# average of first n natural numbers
n = int(input("enter n: "))

def avg_(n):
    sum = 0
    i = 0 
    while i<=n:
        sum += i
        i += 1
    avg = sum/n
    print(avg)
    return avg

avg_(n)
