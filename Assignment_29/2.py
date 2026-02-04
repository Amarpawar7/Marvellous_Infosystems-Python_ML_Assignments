import os

def main():
    FileName =input("Enter the name of the file : ")

    if os.path.exists(FileName):

        fobj =open(FileName,"r")
        Data =fobj.read()
        
        print("File contents are: ",Data)
        
        fobj.close()
    else:
        print("There is no such file")


if __name__=="__main__":
    main()
