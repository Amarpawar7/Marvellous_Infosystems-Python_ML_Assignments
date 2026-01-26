def Minimum(No):
    Min =No[0]
    for i in No:
        if (i<Min):
            Min =i
    return Min

def main():
    No =int(input("Enter number of elements : "))
    Data=[]

    for i in range(No):
        Data.append(int(input()))

    print("Output : ",Minimum(Data))

if __name__ =="__main__" :
    main()
