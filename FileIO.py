f=open("txtfile.txt","w")
lines=["Hellooo!!","My name is"," Anshuman"," Nigam"]
index=0
for line in lines:
     if(index>0):
          f.write(line)
     else:
         f.write(line+"\n")
    
     index+=1


f.close()