def main():
    Data = [2,5,10,11,21,51]
    print("Actual data is : ",Data)

    FData = list(filter(lambda No : No%2 == 0 ,Data))
    print("Data after filter is : ",FData)

if __name__ =="__main__" :
    main()
