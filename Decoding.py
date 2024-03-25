#  Coding:
#  if the word contains atleast 3 characters, remove the 
#  first letter and append it at the end now append 
#  three random characters at the starting and the end 
#  else: simply reverse the string

#  Decoding:
#  if the word contains less than 3 characters, reverse it else: 
# remove 3 random characters from start and end. 
# Now remove the last letter and append it to the beginning

#  Your program should ask whether you want to code or decode

word = input("Enter a string: ")
choice=int(input("Enter 1 for Coding and Enter 2 for Decoding"))
choice=True if (choice==1) else False
print(choice)
if(choice):
    listt = list(word)
    if len(word) >= 3:
        r1 = "dsf"
        r2 = "mto"
        first_letter = listt.pop(0)
        listt.append(first_letter)
        coded_word = ''.join(listt)
        final_word = r1 + coded_word + r2
        print(final_word)
    else:
        reversed_word = ''.join(listt[::-1])
        print(reversed_word)
else:
    listt=list(word)
    if(len(word)<3):
        reversed_word = ''.join(listt[::-1])
        print(reversed_word)
    else:
        newlist = word[3:-3]
        first_letter = listt.pop(-1)
        listt.insert(0, first_letter)
        modified_word = ''.join(listt)
        print(modified_word)

