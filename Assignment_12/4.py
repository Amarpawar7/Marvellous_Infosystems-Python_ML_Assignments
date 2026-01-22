def PrintNumbers(num):
    for i in range(1,num+1):
        print(i,end=" ")


def main():

    No = int(input("Enter the number : "))
    PrintNumbers(No)

if __name__ == "__main__":
    main()
