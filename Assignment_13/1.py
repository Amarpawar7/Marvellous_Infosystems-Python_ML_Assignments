def AreaOfRectangle(length,width):
    area = length*width
    print("Area of rectangle with given attributes is : ",area)


def main():

    length =int(input("Enter length : "))
    width =int(input("Enter width : "))
    AreaOfRectangle(length,width)

if __name__ == "__main__":
    main()