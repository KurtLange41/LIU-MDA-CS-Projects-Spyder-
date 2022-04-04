import random,time

def LinearSearch(arr,ele):
    found=[]
    temp=arr
    i=0   
    while i<len(temp):
        if temp[i]==ele:
            found.append(i)
            i+=1
        else:
            i+=1
    if len(found)>0:
        print("found at following position:\n",found)
    else:
        print("Element not found")
    
    return found

#Ordered Linear search
def LinearSearchSorted(arr,ele):
    found=[]
    temp=arr
    i=0
    stopped=False
    
    while i<len(temp):
        if temp[i]==ele and not stopped:
            
            found.append(i)
            i+=1
            
        else:
            if temp[i]>ele:
                stopped=True
                break
            else:
                i+=1
    if len(found)>0:
        print("found at following position:\n",found)
    else:
        print("Element not found")
    
    return found

def CheckIndexHigher(arrList,index):
    i=index+1
    allPositions=[]
    while i<len(arrList) and arrList[index]==arrList[i]:
        allPositions.append(i)
        i+=1
    return allPositions

def CheckIndexLower(arrList,index):
    i=index-1
    allPositions=[]
    while i>=0 and arrList[index]==arrList[i]:
        allPositions.append(i)
        i-=1
    return allPositions


def BinarySearch(arr,ele):
    found=False
    first=0
    last=len(arr)-1
    index=[]
    
    while first <=last and not found:
        mid_term=int((first+last)/2)
        print("Mid term value=",arr[mid_term])
        print("Mid term index=",mid_term)
        
        if arr[mid_term]==ele:
            found=True
            index.append(mid_term)
            indexHigher=CheckIndexHigher(arr,mid_term)  #this function will include all index higher than mid_term
            index.extend(indexHigher) #this function will include all index lower than mid_term
            indexLower=CheckIndexLower(arr, mid_term)
            index.extend(indexLower)            
            break
        else:
            if arr[mid_term] < ele:
                first=mid_term + 1
            else:
                last=mid_term - 1
    return index

def RandomNumberGen(numOfElements,start,end):
    arrList = []
    i=1
    while i<=numOfElements:
        num=random.randint(start, end)
        arrList.append(num)
        i+=1
    return arrList

def BestCase(arr,ele):
    start=time.time()
    print(start)
    found=BinarySearch(arr, ele)
    end=time.time()
    print(end)
    print("Time for execution of program for best case binary search computation: {}".format(
        (end-start, 10)))
    
    if len(found)>0:
        print("found at following position:\n",found)
    else:
        print("Element not found")

def WorstCase(arr,ele):
    start=time.time()
    print(start)
    found=BinarySearch(arr, ele)
    end=time.time()
    print(end)
    print("Time for execution of program for worst case binary search computation: {}".format(
        (end-start, 10)))
    if len(found)>0:
        print("found at following position:\n",found)
    else:
        print("Element not found")
    
def AvgCase(arr,ele):
    start=time.time()
    print(start)
    found=BinarySearch(arr, ele)
    end=time.time()
    print(end)
    print("Time for execution of program for average case binary search computation: {}".format(
        (end-start, 10)))
    if len(found)>0:
        print("found at following position:\n",found)
    else:
        print("Element not found")

def main():
    randomList=RandomNumberGen(2000,1,10000)
    first=0
    last=len(randomList)-1
    mid_term=int((first+last)/2)
    #Sorting the array
    #randomList.sort()
    print(randomList)
    
    print("\nSuggestion:",randomList[mid_term])
    #unordered linear search
    ele=int(input("\nEnter the middle element for linear case:"))
    start=time.time()
    LinearSearch(randomList,ele)
    end=time.time()
    print("\nTime for execution of program for linear search computation: {}".format(
        (end-start, 10)))
    
    #Sorted Linear Search 
    randomList.sort()
    start=time.time()
    print("\nStarting sorted linear search for same element:",ele)
    LinearSearchSorted(randomList,ele)
    end=time.time()
    print("\nTime for execution of program for sorted linear search for {} computation: {}".format(ele,
        (end-start, 10)))
       
    #Binary Search with same element
    print("\nStarting Binary Search of same element:",ele)
    AvgCase(randomList, ele)
    
    #Binary search with first value
    print("\nSuggestion:",randomList[first])
    ele=int(input("Enter first or last element for worst case:"))
    WorstCase(randomList, ele)
    
    # print("Midterm:",mid_term)
    # ele=int(input("Enter the middle element for best case:"))
    # BestCase(randomList, ele)
    
   

if __name__ == "__main__":
    main()