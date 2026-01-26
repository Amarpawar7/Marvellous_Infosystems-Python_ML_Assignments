def DivisibleByFive(No):
    return ((No%5) == 0)

def main():
    No =int(input("Enter number: "))
    Ret = DivisibleByFive(No)
    print("Output:", Ret)

if __name__ =="__main__" :
    main()
