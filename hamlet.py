def gettext():    
    infile=open("D:/python/practice/36/hamlet.txt",'r').read().lower()
    for ch in '!"#$%&()*+,-./:<=>?@[\\}^_`{|}~':
        infile = infile .replace(ch," ")
    return infile
hamlettex=gettext()
words= hamlettex.split()
counts={}
excludes=['the','and']
for word in words:
    counts[word]=counts.get(word,0)+1
for i in range(len(excludes)):
    t=excludes[i]
    del counts[t]
list2= list(counts.items())
list2.sort(key=lambda x:x[1],reverse=True)

for i in range(10):
    
    word,count=list2[i]
    print("{0:<10}{1:>5}".format(word,count))
