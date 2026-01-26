import MarvellousNum

def PrimeNos(No):
    Sum =0
    for i in No:
        if(MarvellousNum.ChkPrime(i)):
            Sum =Sum + i
    return Sum

def main():
    No =int(input("Enter number of elements : "))
    Data=[]

    for i in range(No):
        Data.append(int(input()))

    print("Output : ",PrimeNos(Data))

if __name__ =="__main__" :
    main()
