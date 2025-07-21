"""Q1 You had saved the items and their price details in a text file, which you purchased yesterday from a nearby super market.
You need to know:
How many items did you purchase?
How many items are free?
What is the total amount you had to pay?
What is the discount amount?
What is the final amount you pay after the discount?
Job:
Try yourself by writing a program code to do this. Include necessary code to handle the possible exceptions.
Note:
Data is stored in a text file Purchase-1.txt.
Each line contains one item’s details.
Item name and price is separated by space.
You have to enter the file name during run time.
Sample input 1:
Purchase-1.txt
Chocolate 50  
Biscuit 35  
Icecream 50
(Blank line)  
Discount 5
Sample output 1:
Enter the file name: Purchase-1  
No of items purchased: 3  
No of free items: 0  
Amount to pay: 135  
Discount given: 5  
Final amount paid: 130

Sample input 2:
Purchase-1.txt
Chocolate 50  
Biscuit 35
Icecream 50  
Rice 100  
Chicken 100  
(Blank Line)  
Perfume Free
(Blank Line)
Soup Free  
(Blank Line)    
Discount 80
Sample output 2:
Enter the file name: Purchase-1  
No of items purchased: 5  
No of free items: 2  
Amount to pay: 485  
Discount given: 80  
Final amount paid: 405
"""

try:
    filename=input("Enter the file name: ")
    actualreq=filename+'.txt'
    f=open(actualreq,'r')
except Exception as e:
    print(f"Error occurred: {e}")
else:
    content=f.readlines()
    total=0
    n=0
    free=0
    dicount=0
    for i in content:
            j=i.split(" ")
            if len(j)<=1:
                continue
            if j[0]=="Discount":
                dicount=j[1]
                continue
            if j[1][0:len(j)].isnumeric():
                n+=1
                total+=int(j[1])
            elif j[1][0:len(j)]!='Free':
                free+=1
    print(f"No of items purchased: {n}")
    print(f"No of free items: {free}")
    print(f"Amount to pay: {total}")
    print(f"Discount given: {dicount}")
    print(f"Final amount paid: {total-int(dicount)}")