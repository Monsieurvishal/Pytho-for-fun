#read data from Wikipedia and store the summary in a fileand store

import wikipedia #If you do nt have wikipedia pip install wikipedia

result = wikipedia.page("Dhoni") 

print(result.summary) 

file1 = open("myfile.txt","w") 

file1.write(result.summary)

file1.close()

