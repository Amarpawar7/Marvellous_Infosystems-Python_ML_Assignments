def CountingDigits(No):
    count=0
    while (No>0):
        count =count + 1
        No=No//10
    return count

def main():
    No =int(input("Enter number : "))
    print("Output:",CountingDigits(No))

if __name__ == "__main__":
    main()
