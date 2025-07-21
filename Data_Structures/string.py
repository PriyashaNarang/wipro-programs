#EXERCISES
#STRING
#Q1 WAP to count the number of upper and lower case letters in a string.
str1=input("Enter the string: ")
uc=0
lc=0
for i in str1:
    if i.islower():
        lc+=1
    elif i.isupper():
        uc+=1
print(f"No. of lowercase letters: {lc}")
print(f"No. of uppercase letters: {uc}")

#Q2 WAP to check whether a given string is palindrome or not.
str2=input("Enter the string: ")
str3=str2[::-1]
if str2==str3:
    print(f"{str2} is a palindrome.")
else:
    print(f"{str2} is not a palindrome")

#Q3 Given a string, return a new string made of n copies of the first 2 chars of the original string where n is the length of the string. The string length will be >= 2.
str4=input("Enter the string: ")
n=len(str4)
reqstr=str4[0:2]
ans=reqstr*n
print(f"Output string: {ans}")

#Q4 Given a string, if the first or last character is 'x', return the string without those 'x' characters, else return the string unchanged.
str5=input("Enter string: ")
if str5[0]=='x' and str5[-1]=='x':
    print(f"Output string: {str5[1:-1]}")
elif str5[0]=='x':
    print(f"Output string: {str5[1::]}")
elif str5[-1]=='x':
    print(f"Output string: {str5[0:-1]}")
else:
    print(f"Output string: {str5}")

#Q5 Given a string and an integer n, return a string made of n repetitions of the last n characters of the string. You may assume that n is between 0 and the length of the string inclusive.
str6=input("Enter string: ")
n=int(input("Enter number: "))
l=len(str6)
begin=l-n
reqstr=str6[begin::]
ans=n*reqstr
print(f"Output String: {ans}")