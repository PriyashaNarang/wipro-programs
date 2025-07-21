#EXERCISES
#Q1 Write a program to read the entire content from a txt file and display it to the user.
f=open('file1.txt','r')
content=f.read()
print(content)
f.close()

#Q2 Write a program to read first n lines from a txt file. Get n as user input.
n=int(input("Enter the number of lines to be read: "))
f=open('file1.txt','r')
content=f.readlines()
l=len(content)
if l<n:
    print("Enter valid number of lines")
else:
    for i in content[:n]:
        print(i,end='')
f.close()

#Q3 Write a program to accept input from user and append it to a txt file.
f=open('file1.txt','a')
text=input("Enter text to be appended in file: ")
f.write(text)
f.close()

#Q4 Write a program to read contents from a txt file line by line and store each line into a list.
f=open('file1.txt','r')
lst=[]
while True:
    l=f.readline()
    if not l:
        break
    lst.append(l)
print(lst)

#Q5 Write a program to find the longest word from the txt file contents, assuming that the file will have only one longest word in it.
f=open('file1.txt','r')
lst=f.readlines()
maxm=0
ans=""
for i in lst:
    reqlst=i.split(" ")
    for j in reqlst:
        if maxm<len(j):
            maxm=len(j)
            ans=j
print(f"Longest string: {ans}")

#Q6 Write a program to count the frequency of a user entered word in a txt file.
f=open('file1.txt','r')
inputword=input("Enter word whose frequency you want to get: ")
lst=f.readlines()
count=0
for i in lst:
    reqlst=i.split(" ")
    for j in reqlst:
        if j==inputword:
            count+=1
print(f"Frequency of {inputword}: {count}")