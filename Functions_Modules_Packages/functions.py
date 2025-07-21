#EXERCISES
#FUNCTIONS

"""Q1 Write a function to return the sum of all numbers in a list.
Sample List: (8, 2, 3, 0, 7)
Expected Output: 20"""

def sumlst(lst):
    s=0
    for i in lst:
        s+=i
    return s
samplelst=[8,2,3,0,7]
print(f"Output Sum: {sumlst(samplelst)}")

"""Q2 Write a function to return the reverse of a string.
Sample String: "1234abcd"
Expected Output: "dcba4321"""

def reverse(inputstr):
    reversestr=inputstr[::-1]
    return reversestr
inputstr=input()
print(f"Reverse string: {reverse(inputstr)}")

"""Q3 Write a function to calculate and return the factorial of a number (a non-negative integer)."""

def fact(n):
    if n==0:
        return 1
    else:
        return fact(n-1)*n
n=int(input("Enter no.: "))
print(f"Factorial of {n} = {fact(n)}")

"""Q4 Write a function that accepts a string and prints the number of upper case letters and lower case letters in it."""

def upperandlowercase(inputstr):
    uc=0
    lc=0
    for i in inputstr:
        if i.islower():
            lc+=1
        elif i.isupper():
            uc+=1
    print(f"No. of lower case letters: {lc}")
    print(f"No. of upper case letters: {uc}")
inputstr=input("Enter string: ")
upperandlowercase(inputstr)

"""Q5 Write a function to print the even numbers from a given list. List is passed to the function as an argument.
Sample List: [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result: [2, 4, 6, 8]"""

def even(lst):
    evenlst=[]
    for i in lst:
        if i%2==0:
            evenlst.append(i)
    print(f"Output: {evenlst}")
lst=[1,2,3,4,5,6,7,8,9]
even(lst)

"""Q6 Write a function that takes a number as a parameter and checks whether the number is prime or not."""

def isprime(n):
    sqt=int(n**0.5)
    for i in range(2,sqt+1):
        if n%i==0:
            return False
    return True
n=int(input("Enter no.: "))
if isprime(n):
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")