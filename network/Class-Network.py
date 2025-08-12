clas="."
while clas!="-":
    clas=input(" ΔΩΣΕ ΙΡ : ")
    byt=[]
    def synart(x):
        if x>=0 and x<=127:
            print("CLASS A")
        elif x>=128 and x<=191:
            print("CLASS B")
        elif x>=192 and x<=223:
            print("CLASS C")
        elif x>=224 and x<=239:
            print("CLASS D")
        elif x>=240 and x<=255:
            print("CLASS E")   
    for i in clas:
        if i != ".":
            byt.append(i)
        else:
            break
    if len(byt)==1:
        byte=byt[0]
        byte=int(byte)
        synart(byte)  
    elif len(byt)==2:
         byte=byt[0]+byt[1]
         byte=int(byte)
         synart(byte)
    elif len(byt)==3:
        byte=byt[0]+byt[1]+byt[2]
        byte=int(byte)
        synart(byte)
    
    
