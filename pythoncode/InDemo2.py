class   Shape:
    def  method1(self):
        print('This is a shape class')

class  Circle(Shape):
    def  method2(self):
        print('This is a circle class')


class   Line(Circle):
    def  method3(self):
        print('This is a Line class')

obj=Line()
obj.method1()

obj.method2()
obj.method3()
