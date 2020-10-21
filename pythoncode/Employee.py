class     Employee:

    aa = 10		## class variable/static variable

    def  __init__(self,eId,eName):
        self.empId = eId
        self.empName=eName

    def  method1(self):
         Employee.aa = Employee.aa + 1

    def printdemo(self):
         print(Employee.aa)

eobj  = Employee("10002","navin")
print(eobj.empId +"/"+eobj.empName)
eobj.method1()
eobj.printdemo()                               ##  aa  =   11    (eobj)


eobj1  = Employee("10003","prasanna")
print(eobj1.empId +"/"+ eobj1.empName)
eobj1.method1()
eobj1.printdemo()                              ## aa =12  (eobj1)

eobj2  = Employee("10005","dola")
print(eobj2.empId +"/"+ eobj2.empName)
eobj2.method1()                                ## aa = 13
eobj2.printdemo()   ## 11
