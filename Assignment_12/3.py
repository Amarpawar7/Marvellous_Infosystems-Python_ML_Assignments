def ArithmeticOperations(a,b):
    print("Addition of the given number is :", a+b)
    print("Subtraction of the given number is :", a-b)
    print("Multiplication of the given number is :", a*b)
    print("Division of the given number is :", a/b)

def main():
    No1 =int(input("Enter first number : "))
    No2 =int(input("Enter second number : "))
    
    ArithmeticOperations(No1,No2)

if __name__ == "__main__":
    main()