def Frequency(No,Search):
    Count=0
    for i in No:
        if(i == Search):
            Count =Count+1
    return Count

def main():
    No =int(input("Enter number of elements : "))
    Data=[]

    for i in range(No):
        Data.append(int(input()))

    Target = int(input("Enter element to search : "))
    print("Output : ",Frequency(Data,Target))

if __name__ == "__main__":
    main()
