def CheckPalindrome(num):
    OriginalNo=num
    ReverseNo = 0
    while num != 0:
        ReverseNo = ReverseNo*10 + (num%10)
        num //= 10
    return OriginalNo == ReverseNo

def main():
    No = int(input("Enter the number : "))
    
    if CheckPalindrome(No)==True:
        print("Palindrome")
    else:
        print("Not Palindrome")


if __name__ == "__main__":
    main()

