text=open("about.txt","r")
text=text.read()
text=text.split(" ")

worddict={}
wordsw6l=[]
highest=0

for i in text:
    i=i.lower()
    if i not in worddict:
        worddict[i]=1
    else:
        worddict[i]+=1

    lcount=0
    if ',' in i:
        i.replace(',','')
    if '.' in i:
        i.replace('.','')
    for j in i:
        lcount=lcount+1
    if lcount>=6:
        wordsw6l.append(i)

for i in worddict:
    if worddict[i]>highest:
        highest=worddict[i]
        maxkey=i

print("The words with 6 or more letters are: ")
for i in wordsw6l:
    print(i)

print("The most frequent word is",maxkey)
