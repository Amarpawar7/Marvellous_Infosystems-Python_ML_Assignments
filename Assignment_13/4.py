
def PrintBinary(num):
    print("Binary equivalent :" ,bin(num)[2:])                   # new : bin(num) Converts a decimal number to binary, and [2:] removes prefix(that is it indicates 0b as binary to the base 2 number) of th eanswer to get exact binary number

def main():
    No = int(input("Enter the number : "))
    PrintBinary(No)

if __name__ == "__main__":
    main()
