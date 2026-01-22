def CheckDivisibility(num):
    if (num%3 == 0 and num%5 == 0):
        print("Divisible by 3 and 5")
    else:
        print("Not divisible by 3 and 5")
    
def main():
    No = int(input("Enter the number : "))
    CheckDivisibility(No)

if __name__ == "__main__":
    main()

