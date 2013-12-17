text_file = open("write_it.txt", "w")
text_file.write("Line 1\n")
text_file.write("This is line 2\n")
text_file.write("That makes this line 3\n")
text_file.close()

f = open('write_it.txt',"r")
for i in range(3):
         print str(i) + ': ' + f.readline(),

f.close()