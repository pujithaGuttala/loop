 #positive integer that is equal to the sum of its proper divisors

num=int(input("enter the number"))
sum=0
for i in range(1,num):
    if num%i==0:
        sum=sum+i
if sum==num:
    print(num, "is perfect number")
else:
    print("it is not perfect number")
