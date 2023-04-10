n=int(input("enter the number"))
temp=n
reversed=0
while temp>0:
    rem=temp%10
    temp//=10
    reversed=reversed*10+rem
if n==reversed:
    print("palindrome number")
else:
    print("not palindrome number")



