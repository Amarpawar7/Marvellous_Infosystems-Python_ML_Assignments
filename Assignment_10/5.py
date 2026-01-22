def OddNumbers(num):
    for i in range (1,num+1,2):
        print(i)


def main():
    No = int(input("Enter the number : "))
    OddNumbers(No)

if __name__ == "__main__":
    main()

