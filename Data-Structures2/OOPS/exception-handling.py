'''class Vehicles:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def get_value(Self):
        try:
            age = 2023-Self.model
            return 100*(1/age)
        except TypeError:
            age = 2023-int(Self.model)
            return 100*(1/age)


myObj = Vehicles("Tesla","2022","electric")
print(myObj.get_value())'''

class ZeroDenominatorError(ZeroDivisionError):
    pass
try:
    a = 10
    b = 0
    if(b==0):
        raise ZeroDenominatorError()
    c = a/b
except ZeroDivisionError:
    print('Zero Division Error occured',end= "")
except ZeroDenominatorError:
    print('Zero Denominator Error occured',end = "")
else:
    print("else works",end=' ')
finally:
    print("finally works")