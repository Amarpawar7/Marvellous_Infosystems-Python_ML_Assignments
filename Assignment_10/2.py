def Summation(num):
    Ans = 0
    for i in range(num+1):
        Ans =Ans + i
    return Ans

def main():
    No = int(input("Enter the number : "))
    Result = Summation(No)
    print("Sum of first ",No ,"Natural numbers is : ",Result)

if __name__ == "__main__":
    main()

