def main():
    Data =["Python","Java","C++","Marvelous","Infosystems","Placement","Automation"]
    print("Actual data is : ",Data)

    FData =list(filter(lambda Str: len(Str)>5 ,Data))
    print("Data after filter is : ",FData)

if __name__ =="__main__" :
    main()