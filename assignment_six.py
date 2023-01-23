#Reads any file called "readme.txt" and returns the line, word, and character count

def lines():
    f = open('readme.txt', 'r')                 #Open file
    contents = f.readlines()                    #Read lines in file
    f.close                                     #Close file
    lines=len(contents)                         #Assigns the number of lines to lines variable
    print("Lines:      ",lines)                 #Prints lines variable

def words():
    f = open('readme.txt', 'r')                 #Open file
    contents = f.read()                         #Read file
    f.close                                     #Close file
    contents = contents.split()                 #Splits the text into words in a list
    words=len(contents)                         #Assigns the number of words to words variable
    print("Words:      ",words)                 #Prints words variable

def characters()
    f = open('readme.txt', 'r')                 #Open file
    contents = f.read()                         #Read file
    f.close                                     #Close file
    characters=len(contents)-lines+1            #The len function counts newline characters (\n) that are normally invisible, so by subtracting the number of lines and adding one I get only the number of visible characters. This does include spaces.
    print("Characters: ",characters)            #Prints character variable

lines()
words()
characters()