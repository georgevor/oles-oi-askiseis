import math
b=[]
m=[]
with open("this.txt","r")as f:
    data=f.read()
    newstring=''
    for char in data:
            b.append(ord(char))
for i in b:
   m.append(str(bin(i)[2:]))

s=''
f=''
bi=[]
for j in m:
    s=j[:2]
    f=j[-2]+j[-1]
    a=s+f
    bi.append(a)

g=[]
for i in range(0,len(bi),4):
    
    if i<len(bi)-4:
       g1=bi[i]+bi[i+1]+bi[i+2]+bi[i+3]
       g.append(g1)

d=[]
for i in g:
    d.append(int(i,2))


n=0
z=0
d3=0
d5=0
d7=0
d1=0
for i in d:
    n+=1
    if i%2==0:
        z+=1
    if i%3==0:
        d3+=1
    if i%5==0:
        d5+=1
    if i%7==0:
        d7+=1
posz=(z/(float(n))*100)
pos3=(d3/(float(n))*100)
pos5=(d5/(float(n))*100)
pos7=(d7/(float(n))*100)

print('to pososto ton arithmon pou einai zigoi  einai',posz)
print('to pososto ton arithmon pou diairoude akribos me to 3 einai',pos3)
print('to pososto ton arithmon pou diairoude akribos me to 5 einai',pos5)        
print('to pososto ton arithmon pou diairoude akribos me to 7 einai',pos7)
