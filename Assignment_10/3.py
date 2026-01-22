def Factorial(num):
    Fact = 1
    for i in range(1,num+1):
        Fact =Fact * i
    return Fact

def main():
    No = int(input("Enter the number : "))
    Result = Factorial(No)
    print("Factorial of ",No ,"is : ",Result)

if __name__ == "__main__":
    main()

