def SumOfDigits(No):
    count=0
    while (No>0):
        count =count + (No%10)
        No=No//10
    return count

def main():
    No =int(input("Enter number : "))
    print("Output:",SumOfDigits(No))

if __name__ == "__main__":
    main()
