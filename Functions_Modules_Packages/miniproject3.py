#MINI PROJECT
"""Q1 Write a Python function that accepts a hyphen-separated sequence of colors as input and returns the colors in a hyphen-separated sequence after sorting them alphabetically.
Constraint: All the colors will be completely in either lower case or upper case.
Sample input 1:
green-red-yellow-black-white
Sample output 1:
black-green-red-white-yellow

Sample input 2:
PINK-BLUE-TAN-PURPLE
Sample output 2:
BLUE-PINK-PURPLE-TAN"""

def sortcolors(inputstr):
    colorlst=inputstr.split("-")
    colorlst.sort()
    ans="-".join(colorlst)
    return ans
inputstr=input()
print(f"Output: {sortcolors(inputstr)}")

"""Q2 Create a Python module with the following functions:
Function Name	                                          Task
ispalindrome(name)	Given the user name as input, this function should tell us whether the name is a palindrome or not.
count_the_vowels(name)	Given the user name as input, this function should tell us how many vowels are present in it.
frequency_of_letters(name)	Given the user name as input, this function should tell us how many times each letter appears in the name.
Note: name will be completely in either lower case or upper case.
Import the module in another Python script and test the functions by passing appropriate inputs.
Sample input 1:
bob
Sample output 1:
Yes it is a palindrome.
No of vowels: 1
Frequency of letters: b-2, o-1

Sample input 2:
marcel bentok tanaka
Sample output 2:
No it is not a palindrome.
No of vowels: 7
Frequency of letters: m-1, a-4, r-1, c-1, e-2, l-1, b-1, n-2, t-2, o-1, k-2"""

#MODULE.py
def ispalindrome(name):
    reversename=name[::-1]
    if name==reversename:
        print("Yes it is a palindrome.")
    else:
        print("No it is not a palindrome.")
    
def count_the_vowels(name):
    v=0
    for i in name:
        if i in ['a','A','e','E','I','i','o','O','u','U']:
            v+=1
    print(f"No of vowels: {v}")

def frequency_of_letters(name):
    count={}
    for i in name:
        if count.get(i) is None:
            count[i]=1
        else:
            count[i]+=1
    print("Frequency of letters: ",end="")
    for key,value in count.items():
        print(f"{key}={value}",end=", ")

#Pythonscript.py
import module as m
name=input()
m.ispalindrome(name)
m.count_the_vowels(name)
m.frequency_of_letters(name)