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
    for i in range(len(count)):
        if i==len(count)-1:
            print(f"{i}-{count[i]}")
        else:
            print(f"{i}-{count[i]}",end=", ")
