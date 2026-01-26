def CheckPrime(No):
    if (No<=1):
        return False
    for i in range(2,No):
        if ((No%i) == 0):
            return False
    return True

def main():
    No =int(input("Enter number : "))
    if CheckPrime(No):
        print("It is a Prime Number")
    else:
        print("It is not a Prime Number")

if __name__ =="__main__" :
    main()
