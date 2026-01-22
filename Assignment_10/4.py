def EvenNumbers(num):
    for i in range (2,num+1,2):
        print(i)


def main():
    No = int(input("Enter the number : "))
    EvenNumbers(No)

if __name__ == "__main__":
    main()

