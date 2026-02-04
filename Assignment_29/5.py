import os

def main():
    FileName =input("Enter the name of the file : ")
    Search =input("Enter the string : ")

    if os.path.exists(FileName):

        fobj =open(FileName,"r")

        Data =fobj.read()
        count =Data.count(Search)

        print("Frequency of ",Search," is : ",count)

        fobj.close()
    else:
        print("File does not exist")

if __name__ =="__main__" :
    main()
