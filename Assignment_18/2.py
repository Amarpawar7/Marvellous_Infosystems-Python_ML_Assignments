def Maximum(No):
    Max=No[0]
    for i in No:
        if (i > Max):
            Max=i
    return Max

def main():
    No =int(input("Enter number of elements : "))
    Data=[]

    for i in range(No):
        Data.append(int(input()))

    print("Output : ",Maximum(Data))

if __name__ =="__main__" :
    main()
