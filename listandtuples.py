list = []
list.append(input("enter 1st number: "))
list.append(input("enter 2nd number: "))
list.append(input("enter 3rd number: "))
list.append(input("enter 4rth number: "))
list.append(input("enter 5th number: "))
list.append(input("enter 6th number: "))
list.append(input("enter 7th number: "))
clist = list.copy()
clist.reverse()
if(list == clist):
    print("palindrome")
else:
    print("not palindrome")