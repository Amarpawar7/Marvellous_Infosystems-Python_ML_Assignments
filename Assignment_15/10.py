def main():
    Data =[2,5,10,12,21,30,51,60]
    print("Actual data is : ",Data)

    FData =list(filter(lambda No :(No%2 == 0) ,Data))
    print("Data after filter is : ",FData)

if __name__ =="__main__" :
    main()