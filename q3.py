def wordCount(t):
text = open("sample.txt", "r") #open text file
d = dict() #make a dictoionary as the question requires
for line in text: 
     line = line.strip() 
     words = line.split(" ")

     #start for each loop
     for word in words: 
         if word in d: #does this word already exist in the dictionary?
              d[word] = d[word] + 1
        else: 
            d[word] = 1 # put new word into dictoionary
  

for key in list(d.keys()): #print out the  key and value
    print(key, ":", d[key]) 
