from abc import ABC,abstractmethod
class   Shape(ABC):

    @abstractmethod
    def  area(self):
        return

    @abstractmethod
    def  withdraw(self):
            return


class   Circle(Shape):
    def  area(self):
        print("this is circle area")

    def  withdraw(self):
            return

class  Rect(Shape):
    def  area(self):
        print("this is rect area")

    def  withdraw(self):
            return

##r1 = Shape()

r = Circle()
r.area()

r2 = Rect()
r2.area()
