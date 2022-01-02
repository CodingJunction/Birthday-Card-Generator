name=open("name.txt")
f=open("letter.txt","r")
txt=f.read()
f.close()
for i in name.readlines():
    if "\n" in i:
        ind=i.index("\n")
        
        i=i[0:ind]
    a=txt.replace("[name]",i)
    f=open(f"letter_for_{i}","a") #creating a letter
    f.write(a)
    f.close()

   
        
