import threading

def SumOfEvenFactor(No):
    Sum = 0
    for i in range(1,No+1):
        if(No%i == 0) and (i%2 == 0):
            print("Even Factor : ",i)
            Sum = Sum + i
    print("Sum of Even Factors : ",Sum)

def SumOfOddFactor(No):
    Sum =0
    for i in range(1,No+1):
        if(No%i == 0) and (i%2 != 0):
            print("Odd Factor : ",i)
            Sum = Sum + i
    print("Sum of Odd Factors : ",Sum)

def main():
    No = int(input("Enter number : "))

    t1 = threading.Thread(target=SumOfEvenFactor , args=(No,) , name="EvenFactor")
    t2 = threading.Thread(target=SumOfOddFactor , args=(No,) , name="OddFactor")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
