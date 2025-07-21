#EXERCISES
#TUPLE
#Q1 WAP to print the 4th element from first and fourth element from last in a tuple.
tup=(1,2,3,4,5,6,7,8,9,10)
ele1=tup[3]
ele2=tup[-4]
print(f"Fourth element from first: {ele1}")
print(f"Fourth element from last: {ele2}")

#Q2 WAP to check whether an element exists in a tuple or not.
tup=(1,2,3,4,5,6,7,8,9,10)
n=int(input("Enter number to be checked: "))
if n in tup:
    print(f"{n} exists in {tup}")
else:
    print(f"{n} does not exist in {tup}")

#Q3 WAP to convert a list into a tuple.
lst=[1,2,3,4,5]
print(f"List: {lst}")
tup=tuple(lst)
print(f"Tuple: {tup}")

#Q4 WAP to find an index of an item in a tuple.
tup=(1,2,3,4,5,6,7,8,9,10)
n=int(input("Enter element: "))
print(f"{n} is present at {tup.index(n)}")

#Q5 WAP to replace last values of tuples in a list to 100.
lst=[(10,20,40),(40,50,60),(70,80,90)]
reqlst=list(lst[2])
reqlst[2]=100
reqtup=tuple(reqlst)
lst.pop()
lst.append(reqtup)
print(lst)