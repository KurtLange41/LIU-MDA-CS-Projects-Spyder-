def openFile(s,mode):
    myFile = open(s,mode)
    return myFile

def getPrime(num):
    primeList=[]
    for i in range(2,num+1):
        divisorList=[]
        for j in range(1,num+1):
            if j<=i:
                if i%j==0:
                    divisorList.append(j)
        if len(divisorList)<=2:
            primeList.append(i)
    
    print("Prime List Halted at Issued Number:",primeList)
    return primeList


def main():
    global primeList,strList
    primeList=[]
    strList=[]
    count=0
    while True:
        num=int(input("Enter Max Range to ID All Prime Numbers:"))
        if num>0:
            primeList=getPrime(num)
            break
        else:
            print("Enter Positive Number OVER 2")
    
    outputFile = "C:\\Users\\kurtl\\Documents\\primes_list.txt"
    output=openFile(outputFile, "w+")
    
    for i in primeList:
        tempList=[]
        for d in str(i):
                tempList.extend(d)
        if i>=1000:        
            tempList.insert(1, " , ")
            
        strList.append(tempList)
    
    for i in strList:
        if (len(i)+count)<=80:
            for j in i:
                output.write(j)
                count+=1
            output.write(" ")
            count+=1
        else:
            if len(i)+count>80:
                output.write("\n")
                count=0 
                
    output.close()
    

if __name__ == "__main__":
    main()