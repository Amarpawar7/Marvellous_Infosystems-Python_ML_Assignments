def SumOfFactors(No):
    Value = 0
    for i in range(1, No):
        if No%i == 0:
            Value =Value+i
    return Value

def main():
    No =int(input("Enter number : "))
    print("Output : ",SumOfFactors(No))

if __name__ =="__main__" :
    main()
