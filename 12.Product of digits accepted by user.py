n=int(input("enter the number"))
p=2
i=n
while n>0:
    p=p*(n%10)
    n=n//10
    print(p)

mulpication
# n=int(input("no"))
# i=0
# while i<=n:
#     j=1
#     while j<=10:
#         print(i,"*",j,"=",i*j)
#         j=j+1
#     i=i+1
#     print()

# n=int(input("enter the number"))
# p=1
# while n>0:
#     p=p*(n%10)
#     n=n//10
#     print(p)

# n=int(input("enter the number"))
# sum=0
# while n>0:
#     a=n%10
#     sum=sum*a
#     n=n//10
# print(sum)