list1 = list[input()]
target1= int(input("enter target:"))
#output = [0,3]
def twosum(list,target):
    for i in range(len(list)):
        for j in range(i+1,len(list)+1):
            if list[i]+list[j]==target:
                return[i,j]
        return []
print(twosum(list1,target1))