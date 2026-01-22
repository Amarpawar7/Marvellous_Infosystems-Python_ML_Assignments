def ReverseNumber(num):
        count= 0
        while (num != 0):
            count = count*10 + (num%10)
            num =num//10
        return count
            
def main():
    No = int(input("Enter the number : "))
    
    Result = ReverseNumber(No)
    print("Reverse of number is : ",Result)

if __name__ == "__main__":
    main()

