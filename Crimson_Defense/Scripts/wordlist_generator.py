# Stephen 
# It's a mess. I'll clean it up some other time

# file1 = open("wordlist-temp2.txt", "r")
# lines1 = file1.readlines()

# file2 = open("wordlist-temp3.txt", "r")
# lines2 = file2.readlines()

# file3 = open("wordlist-football.txt", "r")
# lines3 = file3.readlines()

# file = open("college-names.txt", "r")
# lines = file.readlines()

# word_list = open("college-names-small.txt", "w")

# symbols = ['', '!', '\"', '#', '$', '%', '&', '\'', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']

# change = False
# edit = False
# for line in lines:
#     for s in symbols:
#         word = ""
#         for i in range(0, len(line)):
#             if line[i] == ' ' and change == False:
#                 word += s
#                 change = True
#                 edit = True
#             else:
#                 word += line[i]
#         if change == True:
#             word_list.write(word)
#             change = False
#     if edit == True:
#         edit == False
#     else:
#         word_list.write(line)

# for line in lines1:
#     word_list.write(line)

# for line in lines2:
#     word_list.write(line)

# for line in lines3:
#     word_list.write(line)

# REPLACE LETTERS WITH SYMBOLS TOO

# a -> @

# l L -> |

# file = open("wordlist-medium.txt", "r")
# lines = file.readlines()

# word_list = open("wordlist-hard.txt", "w")
# file = open("roll-tide2.txt", "r")
# lines = file.readlines()

# word_list = open("roll-tide3.txt", "w")

# # Make one letter capital
# print("Making one letter capital")
# for line in lines:
#     word = ""
#     for i in range(0, len(line)):
#         for j in range(0, len(line)):
#             if i==j: 
#                 word+=line[j].upper() 
#             else: 
#                 word+=line[j].lower()
#     word_list.write(word)        

# # Every other even letter
# print("Making every other even indexed letter capital")
# for line in lines:
#     word = ""
#     for i in range(0, len(line)):
#         if (i % 2) == 0: 
#             word+=line[i].upper() 
#         else:
#             word+=line[i].lower()
#     word_list.write(word)           

# #Every other odd letter
# print("Making every other odd indexed letter capital")
# for line in lines:
#     word = ""
#     for i in range(0, len(line)):
#         if (i % 2) != 0: 
#             word+=line[i].upper() 
#         else:
#             word+=line[i].lower()
#     word_list.write(word)         

# # Make a Group of letters letter capital
# print("Making a group of letters capital")
# for line in lines:
#     word = ""
#     for i in range(0, len(line)):
#         for j in range(0, len(line)):
#             if j >= i: 
#                 word+=line[j].upper() 
#             else: 
#                 word+=line[j].lower()
#     word_list.write(word)

# # Make a Group of letters letter capital in reverse
# print("Making a group of letters capital in reverse")
# for line in lines:
#     word = ""
#     for i in range(0, len(line)):
#         for j in range(0, len(line)):
#             if j <= i: 
#                 word+=line[j].upper() 
#             else: 
#                 word+=line[j].lower()
#     word_list.write(word)

# # Make a Group of letters letter capital 2s
# print("Making a group of 2 letters capital")
# for line in lines:
#     word = ""
#     for i in range(0, len(line)):
#         for j in range(0, len(line)):
#             if j == i and j < len(line)-2: 
#                 word+=line[j].upper()
#                 word+=line[j+1].upper() 
#             else: 
#                 word+=line[j].lower()
#     word_list.write(word)

# # Make a Group of letters letter capital 2s front and back
# print("Making a group of two letters capital at front and back")
# for line in lines:
#     word = ""
#     x = len(line)-2
#     for i in range(0, len(line)):
#         for j in range(0, len(line)):
#             if j == i or j == i+1 and j < len(line)-2: 
#                 word+=line[j].upper()
#             elif j == x:
#                 word+=line[x].upper()
#             elif j == x-1:
#                  word+=line[x-1].upper()
#             else: 
#                 word+=line[j].lower()
#         x = (x-2) % len(line)
#     word_list.write(word)

# # Make a Group of letters letter capital every other 2
# print("Making every other two group of letters capital")
# for line in lines:
#     word = ""
#     for i in range(0, len(line)):
#         x = 0
#         for j in range(0, len(line)):
#             if j == x and x < len(line)-2: 
#                 word+=line[x].upper()
#             elif j == x+1 and x < len(line)-2:
#                 word+=line[x+1].upper()
#                 x = x+3 
#             else: 
#                 word+=line[j].lower()
#     word_list.write(word)

# # Make a Group of letters letter capital every other 2
# print("Making groups of two capital")
# for line in lines:
#     word = ""
#     x = 0
#     for i in range(0, len(line)-2):
#         for j in range(0, len(line)):
#             if j == x and x < len(line)-2: 
#                 word+=line[x].upper()
#             elif j == x+1 and x < len(line)-2:
#                 word+=line[x+1].upper() 
#             else: 
#                 word+=line[j].lower()
#         x = x+1
#     word_list.write(word)

# print("Closing files")
# file.close()
# word_list.close()
# file = open("wordlist-medium.txt", "r")
# lines = file.readlines()

# print("Let's Go")
# word_list = open("wordlist-medium-lnum.txt", "w")
# file = open("roll-tide3.txt", "r")
# lines = file.readlines()

# word_list = open("roll-tide3-lnum.txt", "w")
# # Change letters to numbers 
# # i I for 1??
# print("Changing letters to numbers")
# for line in lines:
#     word = ""
#     for j in range(0, len(line)):
#         if line[j] == 'e' or line[j] == 'E': 
#             word+='3'
#         elif line[j] == 'b' or line[j] == 'B':
#             word+='8'
#         elif line[j] == 's' or line[j] == 'S':
#             word+='5'
#         elif line[j] == 'l' or line[j] == 'L':
#             word+='1'
#         elif line[j] == 'o' or line[j] == 'O':
#             word+= '0'
#         elif line[j] == 'a' or line[j] == 'A':
#             word+= '4'
#         elif line[j] == 't' or line[j] == 'T':
#             word+= '7'
#         elif line[j] == 'g':
#             word+= '9'
#         elif line[j] == 'G':
#             word+='6'
#         else: 
#             word+=line[j]
#     word_list.write(word)

# # Change every other letter that can be changed to number to a number
# print("Changing every other even indexed number letter ")
# change = 0
# for line in lines:
#     word = ""
#     change = 0
#     for j in range(0, len(line)):
#         if (line[j] == 'e' or line[j] == 'E') and ((change % 2) == 0): 
#             word+='3'
#             change += 1
#         elif (line[j] == 'b' or line[j] == 'B') and ((change % 2) == 0):
#             word+='8'
#             change += 1
#         elif (line[j] == 's' or line[j] == 'S') and ((change % 2) == 0):
#             word+='5'
#             change += 1
#         elif (line[j] == 'l' or line[j] == 'L') and ((change % 2) == 0):
#             word+='1'
#             change += 1
#         elif (line[j] == 'o' or line[j] == 'O') and ((change % 2) == 0): 
#             word+= '0'
#             change += 1
#         elif (line[j] == 'a' or line[j] == 'A') and ((change % 2) == 0):
#             word+= '4'
#             change += 1
#         elif (line[j] == 't' or line[j] == 'T') and ((change % 2) == 0):
#             word+= '7'
#             change += 1
#         elif line[j] == 'g' and ((change % 2) == 0):
#             word+= '9'
#             change += 1
#         elif line[j] == 'G' and ((change % 2) == 0):
#             word+='6'
#             change += 1
#         elif line[j] == 'e' or 'E' or 'b' or 'B' or 's' or 'S' or 'l' or 'L' or 'o' or 'O' or 'a' or 'A' or 't' or 'T' or 'g' or 'G':
#             change += 1
#             word+=line[j] 
#         else: 
#             word+=line[j]
#     word_list.write(word)

# # Change every other letter that can be changed to number to a number
# print("Changing every other odd indexed number letter ")
# change = 0
# for line in lines:
#     word = ""
#     change = 0
#     for j in range(0, len(line)):
#         if (line[j] == 'e' or line[j] == 'E') and ((change % 2) == 1): 
#             word+='3'
#             change += 1
#         elif (line[j] == 'b' or line[j] == 'B') and ((change % 2) == 1):
#             word+='8'
#             change += 1
#         elif (line[j] == 's' or line[j] == 'S') and ((change % 2) == 1):
#             word+='5'
#             change += 1
#         elif (line[j] == 'l' or line[j] == 'L') and ((change % 2) == 1):
#             word+='1'
#             change += 1
#         elif (line[j] == 'o' or line[j] == 'O') and ((change % 2) == 1): 
#             word+= '0'
#             change += 1
#         elif (line[j] == 'a' or line[j] == 'A') and ((change % 2) == 1):
#             word+= '4'
#             change += 1
#         elif (line[j] == 't' or line[j] == 'T') and ((change % 2) == 1):
#             word+= '7'
#             change += 1
#         elif line[j] == 'g' and ((change % 2) == 1):
#             word+= '9'
#             change += 1
#         elif line[j] == 'G' and ((change % 2) == 1):
#             word+='6'
#             change += 1
#         elif line[j] == 'e' or 'E' or 'b' or 'B' or 's' or 'S' or 'l' or 'L' or 'o' or 'O' or 'a' or 'A' or 't' or 'T' or 'g' or 'G':
#             change += 1
#             word+=line[j] 
#         else: 
#             word+=line[j]
#     word_list.write(word)

# # Change 2 letter that can be changed to number to a number
# print("Changing 1 number letter for every position. long one")
# change = 0
# edit = False
# for select in range(0,22):
#     for line in lines:
#         word = ""
#         change = 0
#         for j in range(0, len(line)):
#             if (line[j] == 'e' or line[j] == 'E') and (change == select): 
#                 word+='3'
#                 change += 1
#                 edit = True
#             elif (line[j] == 'b' or line[j] == 'B') and (change == select):
#                 word+='8'
#                 change += 1
#                 edit = True
#             elif (line[j] == 's' or line[j] == 'S') and (change == select):
#                 word+='5'
#                 change += 1
#                 edit = True
#             elif (line[j] == 'l' or line[j] == 'L') and (change == select):
#                 word+='1'
#                 change += 1
#                 edit = True
#             elif (line[j] == 'o' or line[j] == 'O') and (change == select): 
#                 word+= '0'
#                 change += 1
#                 edit = True
#             elif (line[j] == 'a' or line[j] == 'A') and (change == select):
#                 word+= '4'
#                 change += 1
#                 edit = True
#             elif (line[j] == 't' or line[j] == 'T') and (change == select):
#                 word+= '7'
#                 change += 1
#                 edit = True
#             elif line[j] == 'g' and (change == select):
#                 word+= '9'
#                 change += 1
#                 edit = True
#             elif line[j] == 'G' and (change == select):
#                 word+='6'
#                 change += 1
#                 edit = True
#             elif line[j] == 'e' or 'E' or 'b' or 'B' or 's' or 'S' or 'l' or 'L' or 'o' or 'O' or 'a' or 'A' or 't' or 'T' or 'g' or 'G':
#                 change += 1
#                 word+=line[j] 
#             else: 
#                 word+=line[j]
#         if edit == True:
#             word_list.write(word)
#             edit = False


# print("Closing files")
# file.close()
# word_list.close()

# file1 = open("wordlist-small-advanced.txt", "r")
# file2 = open("wordlist-small.txt", "r")
# file3 = open("sample.txt", "r")
# file4 = open("myteams.txt", "r")

# lines1 = file1.readlines()
# lines2 = file2.readlines()
# lines3 = file3.readlines()
# lines4 = file4.readlines()

# file = open("master-wordlist.txt", "w")

# print("Copying wordlist-small-advanced to master-wordlist")
# for line in lines1:
#     file.write(line)

# print("Copying wordlist-small to master-wordlist")
# for line in lines2:
#     file.write(line)

# print("Copying sample to master-wordlist")
# for line in lines3:
#     file.write(line)

# print("Copying myteams to master-wordlist")
# for line in lines4:
#     file.write(line)

# file = open("college-small.txt", "r")
# lines = file.readlines()

# print("Let's Go")
# word_list = open("college-small-crazy.txt", "w")

# Add a special character to the end 1 and 2
file = open("roll-tide2.txt", "r")
lines = file.readlines()

word_list = open("roll-tide2-special.txt", "w")
# symbols = ['!', '\"', '#', '$', '%', '&', '\'', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '+', '-', '.', '=', '?', '@', '_', '~', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# for line in lines:
#     for i in range(1,len(line)-1):
#         for s in symbols:
#             word = ""
#             for x in range(0,len(line)):
#                 if x == i:
#                     word += s
#                     word += line[x]
#                 else:
#                     word += line[x]
#             word_list.write(word)

# print("Adding 1, 2, 3 special characters onto the end ")
# wrote = False
# for line in lines:
#     for s in symbols:
#         if wrote == False:
#             word = line.rstrip() + s + '\n'
#             word_list.write(word)
#             wrote = True
#         for c in symbols:
#             word = line.rstrip() + s + c + '\n'
#             word_list.write(word)
#             for d in symbols:
#                 word = line.rstrip() + s + c + d + '\n'
#                 word_list.write(word)
#     wrote = False

# print("Adding 1, 2, 3 special characters onto the beginning")
# wrote = False
# for line in lines:
#     for s in symbols:
#         if wrote == False:
#             word = s + line
#             word_list.write(word)
#             wrote = True
#         for c in symbols:
#             word = s + c + line
#             word_list.write(word)
#             for d in symbols:
#                 word = s + c + d + line
#                 word_list.write(word)
#     wrote = False
    

print("Adding 1, 2, 3, 4 special characters onto the end ")
wrote = False
for line in lines:
    for s in symbols:
        if wrote == False:
            word = line.rstrip() + s + '\n'
            word_list.write(word)
            wrote = True
        for c in symbols:
            word = line.rstrip() + s + c + '\n'
            word_list.write(word)
            for d in symbols:
                word = line.rstrip() + s + c + d + '\n'
                word_list.write(word)
                for e in symbols:
                    word = line.rstrip() + s + c + d + e + '\n'
                    word_list.write(word)
    wrote = False

print("Adding 1, 2, 3, 4 special characters onto the beginning")
wrote = False
for line in lines:
    for s in symbols:
        if wrote == False:
            word = s + line
            word_list.write(word)
            wrote = True
        for c in symbols:
            word = s + c + line
            word_list.write(word)
            for d in symbols:
                word = s + c + d + line
                word_list.write(word)
                for e in symbols:
                    word = s + c + d + e + line
                    word_list.write(word)
    wrote = False
    
print("Adding 1 at beginning and 1 at the end")
wrote = False
for line in lines:
    for s in symbols:
        for c in symbols:
            word = s + line.rstrip() + c + '\n' 
            word_list.write(word)

print("Adding 2 at beginning and 2 at the end")
wrote = False
for line in lines:
    for s in symbols:
        for c in symbols:
            for d in symbols:
                for e in symbols:
                    word = s + d + line.rstrip() + c + e + '\n' 
                    word_list.write(word)



# file.close()
# word_list.close()
# file = open("wordlistNUMS.txt", "r")
# word_list = open("wordlistSPECIALNUM.txt", "w")
# lines = file.readlines()

# print("Opening wordlistNUMS")
# print("writing to wordlistSPECIALNUM")

# print("Adding 1 and then 2 special characters onto the end of words with nums, going to be long")
# special_characters = [ '!', '&', '#', '$', '@', '-', '=', '?', '%', '_']
# for line in lines:
#     for s in special_characters:
#         word = line.rstrip() + s + '\n'
#         word_list.write(word)
#         for c in special_characters:
#             word = line.rstrip() + s + c + '\n'
#             word_list.write(word)


# file1 = open("wordlist.txt", "r")
# file2 = open("wordlistNUMS.txt", "r")
# file3 = open("wordlistSPECIAL.txt", "r")
# file4 = open("wordlistSPECIALNUM.txt", "r")

# lines1 = file1.readlines()
# lines2 = file2.readlines()
# lines3 = file3.readlines()
# lines4 = file4.readlines()

# file = open("master-wordlist.txt", "w")

# for line in lines1:
#     file.write(line)

# for line in lines2:
#     file.write(line)

# for line in lines3:
#     file.write(line)

# for line in lines4:
#     file.write(line)
