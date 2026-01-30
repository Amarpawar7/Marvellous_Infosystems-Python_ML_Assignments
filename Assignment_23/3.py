class Numbers:
    
    def __init__(self):
        self.Value =int(input("Enter a number : "))
    
    def ChkPrime(self):
        if(self.Value <= 1):
            print("Enter a valid number! ")

        for i in range(2,self.Value):
            if (self.Value%i != 0 ):
                return True
            else: 
                return False
        
    def Factors(self):
        print("Factors of ",self.Value ,"are : ")
        for i in range(1,self.Value+1):
            if (self.Value%i == 0):
                print(i,end=" ")
        print()

    def SumFactors(self):
        Total = 0
        for i in range(1, self.Value):
            if(self.Value%i == 0):
                Total =Total+i
        return Total
    
    def ChkPerfect(self):
        total=0
        for i in range(1,self.Value):
            if(self.Value%i == 0):
                total =total+i

        if (total == self.Value):
            return True
        else:
            return False
        
obj1 =Numbers()

print("Prime : ",obj1.ChkPrime())
obj1.Factors()
print("Perfect : ",obj1.ChkPerfect())

print("-"*40)

obj2 =Numbers()

print("Prime : ",obj2.ChkPrime())
obj2.Factors()
print("Perfect : ",obj2.ChkPerfect())