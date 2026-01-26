def ChkNum(no):
    if (no%2 == 0):
        print("Even Number")
    else:
        print("Odd Number")

def main():
    No =int(input("Enter number : "))
    ChkNum(No)

if __name__ == "__main__":
    main()
