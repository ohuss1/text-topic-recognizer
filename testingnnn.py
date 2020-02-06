
#stri = "this is string example....wow!!! this is really string babloo is blk"
#print(stri)
#print (str.replace(stri, ' is ' , " "))
#stopwords
f = open("minimal-stop.txt","r")#storing stopwords to string
stopwords_list=[]
for line in f:
    stopwords_list.append(line)

def rowparser(row):
    row = row.replace('"', '').replace("\\n","").replace("\\N","").replace("'", '').replace("[","").replace("]","")
    return row
stopwords_list=rowparser(str(stopwords_list))
#print(stopwords_list)
f.close()
m = open("fish.txt","r")
fish=""
for line in m:
    fish=fish+(line)
#testing print(fish)
fishn=(str.replace(fish,",", " "))
fishn=(str.replace(fish,", ", " "))

fishn=(str.replace(fish,".", ""))
fishn=(str.replace(fishn,".\n", " "))
fishn=(str.replace(fishn,"-", " "))
fishn=(str.replace(fishn,",",""))
fishn = fishn.strip(',')
fishn = fishn.strip('.')

#to test print(fishn)

#print(fish==fishn) To test
#1-removed special characters
#2-now remove non nouns
nouns=fishn
fishsplit=fishn.split()#storing words without spaces in list
for word in fishsplit:
    if word in stopwords_list:
        nouns=(str.replace(nouns,(" "+(word)+" ")," "))
#print("nouns: "+nouns)
newnouns=nouns.lower()#now use this to count frequency
#testingprint(newnouns)
#3-word count
nsplit=newnouns.split()
countword={}
for word in nsplit:
    countword.setdefault(word,0)
    countword[word]=countword[word]+1
# testing print(countword)
print("topic is related to the follwing words")
for wordfreq in countword:
    if (int(countword.get(wordfreq))) > 1:
        highfreq = countword[wordfreq]
        
        print ((wordfreq)+": "+(str(highfreq)))






