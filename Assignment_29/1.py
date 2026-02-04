import os

def main():
    FileName =input("Enter name of the file : ")

    if os.path.exists(FileName):
        print(FileName ,"exists in current directory")
    else:
        print(FileName ,"does not exist in current directory") 


if __name__=="__main__":
    main()
