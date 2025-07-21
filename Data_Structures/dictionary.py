#EXERCISES
#DICTIONARY
#Q1 WAP to add a key and a value to a dictionary.
dictreq={0:10,1:20}
dictreq[2]=30
print(dictreq)

#Q2 WAP to concatenate the following dictionaries to create a new one.
dict1={1:10,2:20}
dict2={3:30,4:40}
dict3={5:50,6:60}
overalldict={}
for i in dict1:
    overalldict[i]=dict1[i]
for i in dict2:
    overalldict[i]=dict2[i]
for i in dict3:
    overalldict[i]=dict3[i]
print(f"Concatenated dictionary: {overalldict}")

#Q3 WAP to check if a given key already exists in the dictionary.
key=int(input("Enter key:"))
demo={1:20,2:30,3:40}
keyslst=demo.keys()
if key in keyslst:
    print(f"{key} is present")
else:
    print(f"{key} is not present")

#Q4 WAP to iterate over a dictionary using for loop and print all the keys alone, all the values alone and both keys and values.
dict1={'a':1,'b':2,'c':3,'d':4,'e':5}
print("Keys:")
for i in dict1.keys():
    print(i,end=" ")
print()
print("Values:")
for i in dict1.values():
    print(i,end=" ")
print()
print("Both keys and values:")
for i,j in dict1.items():
    print(f"{i}:{j}")

#Q5 WAP to prepare a dictionary where keys are numbers from 1 to 15 and values are square of those numbers.
square_dict={}
for i in range(1,16):
    square_dict[i]=i*i
print(square_dict)

#Q6 WAP to sum all the values in a dictionary considering all values are of Int type.
dict1={'a':1,'b':2,'c':3,'d':4,'e':5}
sum=0
for i in dict1.values():
    sum+=i
print(f"Sum of values: {sum}")
