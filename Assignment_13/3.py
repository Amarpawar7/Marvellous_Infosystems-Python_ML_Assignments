def CheckPerfectNo(num):
    total=0
    for i in range(1,num):
        if(num%i == 0):
            total =total+i

    if (total == num):
        print("Perfect Number")
    else:
        print("Not Perfect Number")

def main():

    No= int(input("Enter the number : "))
    CheckPerfectNo(No)

if __name__ == "__main__":
    main()
