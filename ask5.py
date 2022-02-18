from collections import Counter
l=[]
l2=[]
with open("two_cities_ascii.txt","r")as f:
    data=f.read()
    validLetters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩαβγδεζηθικλμνξοπρστυφχψω"
    newString=''
    for char in data:
        if char == '\n':
            newString += '\n'
        if char in validLetters:
            newString += char.lower()           
x=newString.split()
Co=Counter(x)
most_occur=Co.most_common(10)
print("oi 10 diasimoteres lexeis einai oi ",most_occur)
s=''
for i in x:
    s+=i[:2]
    s+='\n'
s1=s.split()

C=Counter(s1)
m=C.most_common(3)
print("oi 3 dimofilesteroi sindiasmoi 2 arxikon gramaton einai ",m)

    
a=''
for f in x:
    if len(f)>3:
       a+=f[:3]
       a+='\n'
a1=a.split()

ca=Counter(a1)
mo=ca.most_common(3)
print("oi 3 dimofilesteroi sindiasmoi 3on arxikon gramaton einai ",mo)
