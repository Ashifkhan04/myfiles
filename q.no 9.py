num=int(input("enter you no:"))
rev=0
num1=num
while num1!= 0:
    digit=num1%10
    num1=num1//10
    rev=rev*10+digit
if rev == num:
    print(num,"is a palindrome.")
else:
    print(num,"is a palindrome.")
