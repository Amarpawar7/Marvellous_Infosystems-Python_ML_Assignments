def main():
    Data = [2,5,11,21,51]
    print("Actual data is : ",Data)

    MData = list(map(lambda No : No*No ,Data))
    print("Data after map is : ",MData)

if __name__ =="__main__" :
    main()
