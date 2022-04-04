import re
def openFile(s):
    myFile = open(s,"rt")
    return myFile

def main():
    global uniqueWordsCount,duplicateWordsCount,countWords
    totalWords=0 
    uniqueWordsCount=0
    duplicateWordsCount=0
    line=[]
    wordList=[]
    
    fileName = "C:\\Users\\kurtl\\Downloads\\wordsfile170K.txt" 

    myFile = openFile(fileName) 
    
    for line in myFile:    
 
        WordInLine=re.split("\s+",line)
        for word in WordInLine:
            if word not in wordList and word not in(""," ",",","\t","\n","\r"):
                print(word,end='\n')
                wordList.append(word)  
                uniqueWordsCount+=1              
            else:               
                if len(word)>0 and word not in(""," ",",","\t","\n","\r") and word.isalnum():
                    duplicateWordsCount+=1
                    print("In else for duplicate word:",word)
    
   
    totalWords = uniqueWordsCount + duplicateWordsCount    
    
    myFile.close() 
    print("Total Word Count:",totalWords)
    print("Unique Word Count: ",uniqueWordsCount) 
    print("Duplicate Word Count:",duplicateWordsCount)
    
if __name__ == "__main__":
    main()
