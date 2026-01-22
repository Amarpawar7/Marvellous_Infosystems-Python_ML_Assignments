def AreaOfCircle(r):
    area = 3.14*r*r
    print("Area of circle with given radius is : ",area)


def main():

    radius= int(input("Enter the radius : "))
    AreaOfCircle(radius)

if __name__ == "__main__":
    main()
    