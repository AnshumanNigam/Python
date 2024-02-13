# Default Arguments

def name(fname,mname="John",lname="Watson"):
     print("Hello,",fname,mname,lname)
name("Amy")

# Keyword Argument

def name(fname,mname,lname):
     print("Hello,",fname,mname,lname)
name(mname="Manohar",fname="Jaikanth",lname="Shikhare") 

# Required arguments

def name(fname,mname,lname):
     print("Hello,",fname,mname,lname)

name("Peter","Spiderman","Parker")

# Variable-length argument

          # Arbitary argument

def name(*name):
    print("Hello,",name[0],name[1],name[2])
name("James","Spain","Parker")

        #  Keyword arbitary argument

def name(**name):
    print("Hello,", name["fname"],name["mname"],name["lname"])

name(mname="Del",lname="Ray",fname="Lana")



# Return Statements

def name(fname,mname,lname):
    return "Hello,"+fname+" "+mname+" "+lname
print(name("James","Martha","Lewis")) 
