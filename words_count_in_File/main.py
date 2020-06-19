import os
def countWords(fileName):
    numwords = 0
    numchars = 0
    numlines = 0

    with open(fileName, 'r') as file:
        for line in file:
            print(line)
            wordlist = line.split()      #Splits at space so we remain with only words
            numlines += 1                #program iter
            numwords += len(wordlist)    #We get no. of words 
            numchars += len(line)        #We get no of characters present

    print ("Words: ", numwords)
    print ("Lines: ", numlines)
    print ("Characters: ", numchars)

if __name__ == '__main__':
    print(os.getcwd(),'\myfile','is the location of the file')
    countWords('myfile.txt')
    
    
 """
 myfile.txt
We all know that IoT is changing industries across the board â€“ from agriculture to healthcare
to manufacturing and everything in between â€“ but what is IoT, exactly? Working for an Internet of Things (IoT) company,
I get asked that question all the time and, over that time, Iâ€™ve worked hard to boil 
it down to something anyone can understand. Hereâ€™s everything you need to know about the internet of things.

"""
"""
OUTPUT:
C:\Users\Vishal \myfile is the location of the file
Words:  71
Lines:  1      #txt files are single line by default
Characters:  415

"""
    
