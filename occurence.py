word=["hi","good","go","bye","check","hello","go","come","hi"]
b=[]
for x in range(len(word)):
    a=word.count("hi")
    if a>1:
        b+=word[x]
    b=word.count("good")
    if b>1:
        b+=word[x]
    c=word.count("go")
    if c>1:
        b+=word[x]
    d=word.count("bye")
    if d>1:
        b+=word[x]
    e=word.count("check")
    if e>1:
        b+=word[x]
print("the number of times hi repeated is",a)
print("the number of times good repeated is",b)
print("the number of times go repeated is",c)
print("the number of times bye repeated is",d)
print("the number of times check repeated is",e)
prprint(word)

'''list=["hi","good","go","bye","check","hello","go","come","hi"]
cnt=0
for i in lst:
c=lst.count(i)
cnt+=1
if(cnt>1 and lst.index(i)>c):
	continue
print(i,c) 
'''