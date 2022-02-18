

with open("two_cities_ascii.txt","r")as f:
    data=f.read()
    validLetters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩαβγδεζηθικλμνξοπρστυφχψω"
    newString =''
    for char in data:
        if char == '\n':
            newString += '\n'
        if char in validLetters:
            newString += char
x=newString.split()
a = []
s = ''
maxL = 0
words = 0
for i in range (0, len(x)-1, 2):
    s += x[i]
    s += x[i+1]
    if(len(s) != 20):
        words += 2
        if(len(x[i])>maxL):
            maxL = len(x[i])
        if(len(x[i+1])>maxL):
            maxL = len(x[i+1])    
        a.append(x[i])
        a.append(x[i+1])
    s = ""    
size = []
print (maxL)
size = [0 for x in range(maxL)]
for i in range(len(a)):
    size[len(a[i])-1] += 1
        
for i in range(maxL):
    print("Le3eis twn ", (i+1), " gramatwn ", size[i], " me pososto ", (size[i]/(float(words)))*100)                                       
      
      
      
   
           
    
                
    

