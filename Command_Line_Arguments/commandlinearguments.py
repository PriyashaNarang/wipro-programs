#EXERCISES
#Q1 WAP to accept two numbers as command line arguments and display their sum.

from sys import argv
a=int(argv[1])
b=int(argv[2])
s=a+b
print(f"Sum: {s}")

#Q2 Write a program to accept a welcome message through command line arguments and display the file name along with the welcome message.

from sys import argv
print(f"Filename: {argv[0]}")
print(f"Welcome message: {argv[1]}")

#Q3 Write a program to accept 10 numbers through command line arguments and calculate the sum of prime numbers among them.

def prime(n):
    if n<=1:
        return False
    sqt=int(n**0.5)
    for i in range(2,sqt+1):
        if n%i==0:
            return False
    else:
        return True
from sys import argv
numbers=argv[1::]
s=0
for i in numbers:
    if prime(int(i)):
        s+=int(i)
print(f"Sum of prime no.'s: {s}")