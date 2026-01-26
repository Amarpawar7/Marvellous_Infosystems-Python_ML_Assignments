def ListSum(No):
    Value = 0
    for i in No:
        Value = Value+i
    return Value

def main():
    No =int(input("Enter number of elements : "))
    Data=[]

    for i in range(No):
        Data.append(int(input()))

    print("Output : ",ListSum(Data))

if __name__ =="__main__" :
    main()
