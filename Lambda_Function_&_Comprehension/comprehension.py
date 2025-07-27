# EXERCISES
# Q1 Write a LC (List Comprehension) program to create an output dictionary which contains only the odd numbers that are present in the input list = [1, 2, 3, 4, 5, 6, 7] as keys and their cubes as values.
list_1=[1,2,3,4,5,6,7]
dict1={i:i**3 for i in list_1 if i%2!=0}
print(dict1)

# Q2 Make a dictionary of the 26 English alphabets mapping each with the corresponding integer.
dictreq={chr(i):i-96 for i in range(97,123)}
print(dictreq)