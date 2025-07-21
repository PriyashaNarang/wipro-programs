# EXERCISES
# Q1. Write a program to check if a given number is Positive, Negative or Zero.
n=int(input("Enter no.: "))
if n>0:
    print(f"{n} is a positive no.")
elif n<0:
    print(f"{n} is a negative no.")
else:
    print(f"{n} is equal to 0")

# Q2. Write a program to check if a given number is odd or even.
n=int(input("Enter no.: "))
if n%2==0:
    print(f"{n} is an even no.")
else:
    print(f"{n} is an odd no.")

# Q3. Given two non-negative values, print true if they have the same last digit, such as with 27 and 57.
n1=int(input("Enter first no.: "))
n2=int(input("Enter second no.: "))
rem1=n1%10
rem2=n2%10
if rem1==rem2:
    print("true")
else:
    print("false")

# Q4. Write a program to print numbers from 1 to 10 in a single row with one tab space.
for i in range(1,11):
    print(i,end=" ")

# Q5. Write a program to print even numbers between 23 and 57. Each number should be printed in a seperate row.
for i in range(23,57):
    if i%2==0:
        print(i)

# Q6. Write a program to check if a given number is prime or not.
n=int(input("Enter no.: "))
sqt=int(n**0.5)
for i in range(2,sqt+1):
    if n%i==0:
        print(f"{n} is not a prime no.")
        break
else:
    print(f"{n} is a prime no.")

# Q7. Write a program to print prime numbers between 10 and 99.
for i in range(10,99):
    sqt=int(i**0.5)
    for j in range(2,sqt+1):
        if i%j==0:
            break
    else:
        print(i)

# Q8. Write a program to print the sum of all the digits of a given number.
n=int(input("Enter no.: "))
t=n
s=0
while t!=0:
    rem=t%10
    s=s+rem
    t=t//10
print(f"Sum of digit of {n} = {s}")

# Q9. Write a program to reverse a given number and print.
n=int(input("Enter no.: "))
t=n
rev=0
while t!=0:
    rem=t%10
    rev=(rev*10)+rem
    t=t//10
print(f"Reverse of {n} = {rev}")

# Q10. Write a program to find if the given number is palindrome or not.
n=int(input("Enter no.: "))
t=n
rev=0
while t!=0:
    rem=t%10
    rev=(rev*10)+rem
    t=t//10
if rev==n:
    print(f"{n} is a palindromic no.")
else:
    print(f"{n} is not a palindromic no.")
