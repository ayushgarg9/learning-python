#read mode 
#f = open("ayush.txt","r")
#data = f.read()
#f.close()

#write mode 
f = open("ayush.txt","w")
f.write("baa baa black sheep")
f.close()

#append mode
f = open("ayush.txt","a")
f.write("\nbaa baa black sheep")
f.close()

#create new file
f = open("ayush1.txt","a")
f.close()

#finding the even number in file
count = 0
with open("practice.txt","r") as f:
    data = f.read()

    nums = data.split(",")
    for val in nums:
        if(int(val)%2==0):
            count+=1

print(count)