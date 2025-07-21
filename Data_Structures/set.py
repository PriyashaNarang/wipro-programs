#EXERCISES
#SET
#Q1 WAP to remove a given item from the set.
st={1,2,3,4,7,5}
n=int(input("Enter item to be removed: "))
print(f"Before removing: {st}")
st.remove(n)
print(f"After removing: {st}")

#Q2 WAP to create an intersection of sets.
st1={1,2,3,4,5}
st2={1,3,5,7,9}
intersectset=st1.intersection(st2)
print(intersectset)

#Q3 WAP to create an union of sets.
st1={1,2,3,4,5}
st2={1,3,5,7,9}
unionset=st1.union(st2)
print(unionset)

#Q4 WAP To find the maximum and minimum values in a set.
st1={1,2,4,3,7,5,8,6}
print(f"Minimum value: {min(st1)}")
print(f"Maximum value: {max(st1)}")