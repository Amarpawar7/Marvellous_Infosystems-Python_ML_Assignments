import threading

def SumOfEvenList(Data):
    Sum = 0
    for i in Data:
        if(i%2 == 0):
            Sum = Sum + i
    print("Sum of Even Elements : ",Sum)

def SumOfOddList(Data):
    Sum = 0
    for i in Data:
        if(i%2 != 0):
            Sum = Sum + i
    print("Sum of Odd Elements : ",Sum)

def main():
    Data = []
    No = int(input("Enter number of elements : "))

    for i in range(No):
        Data.append(int(input()))

    t1 = threading.Thread(target=SumOfEvenList, args=(Data,), name="EvenList")
    t2 = threading.Thread(target=SumOfOddList, args=(Data,), name="OddList")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
