import os
# f=os.open("myfile.txt",os.O_WRONLY)
# os.write(f,b"Hello World \n This is a new file")
# os.close(f)

g=os.open("myfile.txt",os.O_RDONLY)
contents=os.read(g,1024)
print(contents)
os.close(g)

# os.mkdir("newdir")