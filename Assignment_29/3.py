# copying content using Command line

import os
import sys

def main():

    if(len(sys.argv)<2):
        print("Please provide file name from command line")
        return

    FileName = sys.argv[1]

    if os.path.exists(FileName):
        fobj1= open(FileName,"r")
        fobj2 = open("Hello.txt","w")

        fobj2.write(fobj1.read())

        print("Contents copied successfully into Hello.txt")

        fobj1.close()
        fobj2.close()
    else:
        print("There is no such file")

if __name__ == "__main__":
    main()

