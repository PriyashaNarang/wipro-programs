n=int(input("Enter the number of lines to be read: "))
f=open('file1.txt','r')
content=f.readlines()
l=len(content)
if l<n:
    print("Enter valid number of lines")
else:
    # for i in content[:n]:
    #     print(i,end='')
    for i in range(n):
        req=f.readline()
        print(req)
f.close()