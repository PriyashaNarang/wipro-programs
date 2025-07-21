#MINI PROJECT
"""Q1 Your friend has sent you a text file containing a task. He sent a secret message
with a time value by the place and time where you have to go and meet him.
He challenges you to find it out without seeing the content of the file, so he
gave this one to find. Let’s surprise him by breaking the challenge with our
python code.
Hints to find the secret message:
1. The number of lines in the file tells you the meeting time.
   Note: See number of lines = 20.
   If the number of lines exceeds 12, you need to convert it to 12 hour
   format. For example,
     • If the number of lines is 16, then the meeting time is 4 PM.
     • If the number of lines is 10, then the meeting time is 10 AM.
2. The word appearing for the maximum number of times tells you the
   meeting place.
   Note: Meeting place will be a street name.
   For example,
     • If the word Oxford appears for the maximum number of times,
       the meeting place is Oxford Street.
     • If the word Park appears for the maximum number of times, then
       meeting place is Park Street.
Sample Input 1:
Sample.txt
Cricket, a bi-national park game played between two teams of 11 street park
players and five each park and another five in a bi-lane. Started only with
a tennis ball, now park experimenting real ball cricket on broad training.
The participants are now even paying the ball while on the grass value even
in the parks, with the bowling park targeting either of the 3 stumps with one
ball, one park player (like any park day). Teams end up breaking the
boundaries, when the ball hits the park and dodging a fielder, and by the fielding
park when the ball hits by the bat, and ball returns to the park. When the
goals have been eliminated, the innings end and the teams park ride.
Sample output 1:
Meeting time: 9 AM
Meeting place: Park Street
Explanation: Number of lines is 9. The word park appears for the maximum of
13 times.

Sample Input 2:
Sample.txt
Royal Enfield is an Indian Apollo motorcycle manufacturing brand with tag of
Apollo. Apollo motorcycles brand is considered manufacturer of
Apollo Bullet motorcycle. Apollo brand includes: Apollo Interceptor,
Apollo Meteor and Apollo Himalayan. It is now a Apollo subsidiary Eicher Motors Limited, an
Indian Motors firm. It is now a Apollo subsidiary Eicher Motors Limited, an
Indian Motors firm. The company makes Apollo Royal Enfield Bullet, and
other single-cylinder and twin-cylinder Apollo motorcycles. First produced Apollo In 1905, 
Royal Enfield is oldest motorcycle Apollo brand world still production, with Bullet model enjoying 
longest motorcycle Apollo production run of all time. In 1990, Royal Enfield collaborated with Eicher 
Apollo Group, an automotive company Apollo India, and merged with it 1994. Apart from bikes, Eicher 
Apollo Group is involved in the production and sales Apollo commercial vehicles and automotive gears. 
Although Apollo Royal Enfield experienced difficulties 1990s, and ceased Apollo motorcycles production 
at one year factory 2002, by 2014 Apollo company opened a new primary Apollo factory Apollo Chennai suburbs 
of Oragadam on strength of increased demand for its Apollo motorcycles. This was followed in Apollo 2017 
by inauguration another new factory of a similar scale to facility in Apollo Oragadam 
(capacity 600,000 vehicles per year) at Vallam Apollo Vadagal. The original factory at Apollo 
Tiruvottiyur became secondary, and continues to produce some limited-run motorcycle models.
Sample output 2:
Meeting time: 8 PM
Meeting place: Apollo Street
Explanation: Number of lines is 20 and converting it to 12 hour format we get 8 PM. 
The word Apollo appears for the maximum of 25 times."""

f=open('sample.txt','r')
lst=f.readlines()
time=len(lst)
if time<=12:
    print(f"Meeting time: {time} A.M.")
else:
    print(f"Meeting time: {12-time} P.M.")
count={}
for i in lst:
    reqlst=i.split(" ")
    for j in reqlst:
        if count.get(j)!=None:
            count[j]+=1
        else:
            count[j]=1
maxm=0
ans=""
removedwords=['the','The','is','Is','I','in','am','at','with','It']
for i,j in count.items():
    if j>maxm and i not in removedwords:
        maxm=j
        ans=i
ans=ans.capitalize()
print(f"Meeting place: {ans} Street")