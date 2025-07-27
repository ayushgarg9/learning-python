list = [1,2,3,4,5,6,7,8,9]
for i in list:
    print(i)


num = (1,4,9,16,25,36,49,64,81,100)
x = 49
index = 0
for n in num:
    if(n == x):
        print("number found at",index)
        
    index += 1