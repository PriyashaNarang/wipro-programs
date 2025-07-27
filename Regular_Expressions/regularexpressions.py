# EXERCISES
# Q1 Write a program to find check if a string has only octal digits. Given string ['789','123','004']
import re
lst=['789','123','004']
reg=r'^[0-7]+$'
for i in lst:
    res=re.match(reg,i)
    if res:
        print(f"{i} contains only octal digits")
    else:
        print(f"{i} does not contain all octal digits")

""" Q2 Extract the user id, domain name and suffix from the following email addresses.
emails = zuck@facebook.com  
sunder33@google.com  
jeff42@amazon.com"""

import re
emails=['zuck@facebook.com','sunder33@google.com','jeff42@amazon.com']
for i in emails:
    patt=r'^([\w\d]+)@([\w\d]+).([\w]+)$'
    res=re.match(patt,i)
    if res:
        userid,domain,suffix=res.groups()
        print(f"Userid: {userid}, Domain: {domain}, Suffix: {suffix}")

""" Q3 Split the following irregular sentence into proper words
sentence = A, very   very; irregular_sentence  
# Expected output: A very very irregular sentence"""

import re
sentence ="A, very   very; irregular_sentence"
patt=r'[,;_\s]+'
repl=' '
res=re.sub(patt,repl,sentence)
print(res) 

""" Q4 Clean up the following tweet so that it contains only the user’s message. That is, remove all URLs, hashtags, mentions, punctuations, RTs and CCs.
tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
Desired output:
'Good advice What I would do differently if I was learning to code today'
"""
import re
sentence="Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats"
patt3=r'[@#]\w+'
res=re.sub(patt3,'',sentence)
patt1=r'[^\w\s]+'
res=re.sub(patt1,'',res)
patt2=r'\bRT\b|\bcc\b|\brt\b|\bCC\b'
res=re.sub(patt2,'',res)
patt4=r'http[\w]+'
res=re.sub(patt4,'',res)
patt5=r'[\s]+'
res=re.sub(patt5,' ',res)
print(res)

""" Q5 Extract all the text portions between the tags from the following HTML page:
URL: https://raw.githubusercontent.com/selva86/datasets/master/sample.html
Given Code:
import requests
r = requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html")
html_text = r.text  # HTML text is contained here
Desired Output:
['Your Title Here', 
 'Link Name', 
 'This is a Header', 
 'This is a Medium Header', 
 'This is a new paragraph! ', 
 'This is a another paragraph!', 
 'This is a new sentence without a paragraph break, in bold italics.']"""

import requests
import re
url = "https://raw.githubusercontent.com/selva86/datasets/master/sample.html"
response = requests.get(url)
html = response.text
html = re.sub(r'\s+', ' ', html)
matches = re.findall(r'>([^<]+)<', html)
output = [text.strip() for text in matches if text.strip()]
print(output)

""" Q6 Given the below list of words, identify the words that begin and end with the same character.
Word List:
words = ['civic', 'trust', 'widows', 'maximum', 'museums', 'aa', 'as']
"""
import re
words = ['civic', 'trust', 'widows', 'maximum', 'museums', 'aa', 'as']
pattern = r'^(.).*\1$'
result = [word for word in words if re.match(pattern, word, re.IGNORECASE)]
print(result)