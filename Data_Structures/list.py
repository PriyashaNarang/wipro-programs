# EXERCISES
# LIST
#Q1 WAP to create a list of 5 integers and display the list items. Access individual elements through index.
lst=list(map(int,input().strip().split(" ")))
print("List elements are as follows: ")
for i in range(5):
    print(lst[i])

#Q2 WAP to append a new item to the end of list.
n=int(input("Enter element to be appended:"))
lst.append(n)
print(lst)

#Q3 WAP to reverse the order of items in the list.
lst.reverse()
print(lst)

#Q4 WAP to print the number of occurrences of a specified element in the list.
n=int(input("Enter the specified element: "))
print(lst.count(n))

#Q5 WAP to append the elements of list1 to list2 in the front.
lst1=[1,2,3,4]
lst2=[5,6,7]
for i in reversed(lst1):
    lst2.insert(0,i)
print(lst2)

#Q5 WAP to insert a new element before the second element in the existing list.
lst=[1,3,4,5]
print(lst)
lst.insert(1,2)
print(lst)

#Q6 WAP to remove an element from the specified index in the list.
lst=[1,2,3,4,5,6,7]
n=int(input("Specify the index to be removed:"))
print(lst)
lst.pop(n)
print(lst)

#Q7 WAP to remove the first occurrence of the specified element from the list.
lst=[1,1,2,3,1,4,5]
print(lst)
lst.remove(1)
print(lst)