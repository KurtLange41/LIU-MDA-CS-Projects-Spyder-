#Assignment 8

#
#Bubble Sort#
#

import time,re,random
def bubble_sort(arr):
    for x in range(1,len(arr),1):
        for y in range(len(arr)-x):
            if arr[y]>arr[y+1]:
                arr[y],arr[y+1]=arr[y+1],arr[y]

def openFile(s):
    myFile = open(s,"rt")
    return myFile      
 
def processSort(filePath):
    wordList=[]
    
    fileName = filePath
    myFile = openFile(fileName) 
    
    for line in myFile: 
        
        wordsInLine=re.split("\s+",line)
        for word in wordsInLine:  
            if word not in wordList and word not in(""," ",",","\t","\n","\r"):
                wordList.append(word)
    myFile.close()
    wordList.sort()
  
    start=time.time()
    bubble_sort(wordList)
    end=time.time()
    print("Execution Time Elapsed Alpha: {}\n".format(
        (end-start, 10)))
   
    wordList.sort(reverse= True)
    start=time.time()
    bubble_sort(wordList)
    end=time.time()
    print("Execution Time Elapsed Reverse: {}\n".format(
        (end-start, 10)))
    
    random.shuffle(wordList)
    start=time.time()
    bubble_sort(wordList)
    end=time.time()
    print("Execution Time Elapsed Shuffle: {}\n".format(
        (end-start, 10)))

def main():
    print("Bubble Sort - 10 Word List:")
    fileName = "C:\\Users\\kurtl\\OneDrive\\Documents\\10words.txt"
    processSort(fileName)
    print("Bubble Sort - 100 Word List:")
    fileName = "C:\\Users\\kurtl\\OneDrive\\Documents\\100words.txt"
    processSort(fileName)
    print("Bubble Sort - 1000 Word List:")
    fileName= "C:\\Users\\kurtl\\OneDrive\\Documents\\1000word.txt"
    processSort(fileName)
    print("Bubble Sort - 10000 Word List:")
    fileName="C:\\Users\\kurtl\\OneDrive\\Documents\\10000words.txt"    
    processSort(fileName)


if __name__=='__main__':
    main()
    
#
#Insertion Sort #
#    
import time,re,random
def insertion_sort(arr):
    for x in range(1,len(arr)):
        position=x
        currentValue=arr[x]
        while position>0 and arr[position-1]>currentValue:
            
            arr[position]=arr[position-1]
            
            position -=1
        
        arr[position]=currentValue

def openFile(s):
    myFile = open(s,"rt")
    return myFile      
 
def processSort(filePath):
    lines=[]
    wordList=[]
    
    fileName = filePath
    myFile = openFile(fileName) 
    
    for line in myFile: 
        
        wordsInLine=re.split("\s+",line)
        for word in wordsInLine: 
            if word not in wordList and word not in(""," ",",","\t","\n","\r"):
                wordList.append(word)
    myFile.close() 
    wordList.sort()
  
    start=time.time()
    insertion_sort(wordList)
    end=time.time()
    print("Elapsed Execution Time Alpha: {}\n".format(
        (end-start, 10)))
   
    wordList.sort(reverse = True)
    start=time.time()
    insertion_sort(wordList)
    end=time.time()
    print("Elapsed Execution Time Reverse: {}\n".format(
        (end-start, 10)))
    
    random.shuffle(wordList)
    start=time.time()
    insertion_sort(wordList)
    end=time.time()
    print("Elapsed Execution Time Shuffle: {}\n".format(
        (end-start, 10)))

def main():
    print("Insertion Sort - 10 Word List:")
    fileName = "C:\\Users\\kurtl\\OneDrive\\Documents\\10words.txt"
    processSort(fileName)
    print("Insertion Sort - 100 Word List:")
    fileName = "C:\\Users\\kurtl\\OneDrive\\Documents\\100words.txt"
    processSort(fileName)
    print("Insertion Sort - 1000 Word List:")
    fileName = "C:\\Users\\kurtl\\OneDrive\\Documents\\1000word.txt"
    processSort(fileName)
    print("Insertion Sort - 10000 Word List:")
    fileName = "C:\\Users\\kurtl\\OneDrive\\Documents\\10000words.txt"   
    processSort(fileName)
   

if __name__=='__main__':
    main()   
    
#
#Merge Sort #
#     
import time,re,random
def mergeSort(arr):
    if len(arr)>1:
        mid=int(len(arr)/2)
        leftSide=arr[:mid]
        rightSide=arr[mid:]
        mergeSort(leftSide)
        mergeSort(rightSide)

        i,j,k=0,0,0

        while i<len(leftSide) and j<len(rightSide):          
            if leftSide[i]<rightSide[j]:
                arr[k]=leftSide[i]
                i+=1
            else:
                arr[k]=rightSide[j]
                j+=1
            k+=1
        
        while i < len(leftSide):
                arr[k]=leftSide[i]
                i=i+1
                k=k+1

        while j < len(rightSide):
            arr[k]=rightSide[j]
            j=j+1
            k=k+1
    
def openFile(s):
    myFile = open(s,"rt")
    return myFile      
 
def processSort(filePath):
    lines=[]
    wordList=[]
    
    fileName = filePath
    myFile = openFile(fileName)
    
    for line in myFile: 
        
        wordsInLine=re.split("\s+",line)
        for word in wordsInLine:  
            if word not in wordList and word not in(""," ",",","\t","\n","\r"):
                wordList.append(word)
    myFile.close() 
    wordList.sort()
  
    start=time.time()
    mergeSort(wordList)
    end=time.time()
    print("Elapsed Execution Time Alpha: {}\n".format(
        (end-start, 10)))
   
    wordList.sort(reverse= True)
    start=time.time()
    mergeSort(wordList)
    end=time.time()
    print("Elapsed Execution Time Reverse: {}\n".format(
        (end-start, 10)))
    
    random.shuffle(wordList)
    start=time.time()
    mergeSort(wordList)
    end=time.time()
    print("Elapsed Execution Time Shuffle: {}\n".format(
        (end-start, 10)))

def main():
    print("Merge Sort - 10 Word List:")
    fileName = "C:\\Users\\kurtl\\OneDrive\\Documents\\10words.txt"
    processSort(fileName)
    print("Merge Sort - 100 Word List:")
    fileName = "C:\\Users\\kurtl\\OneDrive\\Documents\\100words.txt"
    processSort(fileName)
    print("Merge Sort - 1000 Word List:")
    fileName = "C:\\Users\\kurtl\\OneDrive\\Documents\\1000word.txt"
    processSort(fileName)
    print("Merge Sort - 10000 Word List:")
    fileName = "C:\\Users\\kurtl\\OneDrive\\Documents\\10000words.txt"      
    processSort(fileName)
   

if __name__=='__main__':
    main()

#
#Shell Sort #
#       
    
import re,time,random
def shell_sort(arr):
    global sublistcount
    sublistcount = int(len(arr)/2)
    
    while sublistcount > 0:
        for start in range(sublistcount):
            gap_insertion_sort(arr,start,sublistcount)

        sublistcount = int(sublistcount / 2)

def gap_insertion_sort(arr,start,gap):
    for i in range(start+gap,len(arr),gap):

        currentvalue = arr[i]
        position = i

        while position>=gap and arr[position-gap]>currentvalue:
            arr[position]=arr[position-gap]
            position = position-gap
        
        arr[position]=currentvalue
 
def openFile(s):
    myFile = open(s,"rt")
    return myFile      
 
def processSort(filePath):
    lines=[]
    wordList=[]
    
    fileName = filePath
    myFile = openFile(fileName) 
    
    for line in myFile: 
        
        wordsInLine=re.split("\s+",line)
        for word in wordsInLine:  
            if word not in wordList and word not in(""," ",",","\t","\n","\r"):
                wordList.append(word)
    myFile.close() 
    wordList.sort()
  
    start=time.time()
    shell_sort(wordList)
    end=time.time()
    print("Elapsed Execution Time Alpha: {}\n".format(
        (end-start, 10)))
   
    wordList.sort(reverse= True)
    start=time.time()
    shell_sort(wordList)
    end=time.time()
    print("Elapsed Execution Time Reverse: {}\n".format(
        (end-start, 10)))
    
    random.shuffle(wordList)
    start=time.time()
    shell_sort(wordList)
    end=time.time()
    print("Elapsed Execution Time Shuffle: {}\n".format(
        (end-start, 10)))

def main():
    print("Shell Sort - 10 Word List:")
    fileName = "C:\\Users\\kurtl\\OneDrive\\Documents\\10words.txt"
    processSort(fileName)
    print("Shell Sort - 100 Word List:")
    fileName = "C:\\Users\\kurtl\\OneDrive\\Documents\\100words.txt"
    processSort(fileName)
    print("Shell Sort - 1000 Word List:")
    fileName = "C:\\Users\\kurtl\\OneDrive\\Documents\\1000word.txt"
    processSort(fileName)
    print("Shell Sort - 10000 Word List:")
    fileName = "C:\\Users\\kurtl\\OneDrive\\Documents\\10000words.txt"      
    processSort(fileName)
   
if __name__=='__main__':
    main()
    
    
    
    
    
    
    