import ArithematicModule

def main():
    No1 = int(input("Enter first number: "))
    No2 = int(input("Enter second number: "))

    print("Addition : ",ArithematicModule.Add(No1, No2))
    print("Subtraction : ",ArithematicModule.Sub(No1, No2))
    print("Multiplication : ",ArithematicModule.Mult(No1, No2))
    print("Division : ",ArithematicModule.Div(No1, No2))

if __name__ =="__main__" :
    main()
