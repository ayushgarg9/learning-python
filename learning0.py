str1 = input()
count = 0
for i in range(len(str1)):
        count += 1  
if str1[0] == '-':
    print(count-1)
else: print(count)