def CountofDigit(num):
        count= 0
        while (num != 0):
            count= count+1
            num =num//10
        return count
            
def main():
    No = int(input("Enter the number : "))
    
    Result = CountofDigit(No)
    print("Count of digits in the given number is : ",Result)

if __name__ == "__main__":
    main()

