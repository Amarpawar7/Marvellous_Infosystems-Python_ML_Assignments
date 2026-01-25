from functools import reduce

def main():
    Data = [2,5,10,11,21,51]
    print("Actual data is : ",Data)

    RData = reduce((lambda No1,No2 : No1 if(No1>No2) else No2),Data)
    print("Data after reduce is : ",RData)

if __name__ =="__main__" :
    main()