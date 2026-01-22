def CheckPrime(num):
        for i in range(2,num):
            if (num%i != 0 ):
                return True
            else: 
                return False

def main():
    No = int(input("Enter the number : "))
    
    Result = CheckPrime(No)
    if(Result == True):
        print("The given number is prime")
    else: 
        print("The given number is not prime")


if __name__ == "__main__":
    main()

