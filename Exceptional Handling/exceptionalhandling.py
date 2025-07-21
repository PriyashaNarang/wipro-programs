#EXERCISES
"""Q1 Write a program to accept two numbers from the user and perform division. 
If any exception occurs, print an error message or else print the result."""

try:
    a=int(input("Enter first no.: "))
    b=int(input("Enter second no.: "))
    res=a/b
except Exception as e:
    print(f"Error occurred: {e}")
else:
    print(f"Result of division: {res}")

"""Q2 Write a program to accept a number from the user and check whether it’s prime or not. 
If user enters anything other than number, handle the exception and print an error message."""

def isprime(n):
    sqt=int(n**0.5)
    if n<=1:
        return False
    for i in range(2,sqt+1):
        if n%i==0:
            return False
    return True

try:
    n=int(input("Enter a number: "))
    if isprime(n):
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")
except ValueError:
    print("Invalid value encountered in place of number.")

"""Q3 Write a program to accept the file name to be opened from the user, 
if file exists print the contents of the file in title case or else handle the exception and 
print an error message."""

try:
    filename=input("Enter the file name to be opened: ")
    f=open(filename,'r')
except FileNotFoundError:
    print("File does not exist.")
else:
    while True:
        reqline=f.readline()
        if reqline:
            print(reqline.title(),end='')
        else:
            break

"""Q4 Declare a list with 10 integers and ask the user to enter an index. Check whether the number in 
that index is positive or negative number. If any invalid index is entered, handle the exception and 
print an error message."""

try:
    lst=[1,2,3,4,5,6,7,8,9,10]
    ind=int(input("Enter the index: "))
    ele=lst[ind]
except IndexError:
    print("Invalid index entered.")
else:
    if ind>=0:
        print("Positive index")
    else:
        print("Negative index")
    print(f"Element found at index {ind}: {ele}")