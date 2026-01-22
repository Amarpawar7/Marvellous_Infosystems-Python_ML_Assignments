def SumOfDigits(num):
        count= 0
        while (num != 0):
            Remainder= num%10          
            count= count +Remainder    # count= count +(num%10)    
            num =num//10
        return count
            
def main():
    No = int(input("Enter the number : "))
    
    Result = SumOfDigits(No)
    print("Count of digits in the given number is : ",Result)

if __name__ == "__main__":
    main()

