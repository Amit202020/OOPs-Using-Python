class    Emp:

    empDesc = "govt employee"   ## static or class variable

    def  __init__(self , pempId , pempName):  ## default contrustor
        self.empId=pempId     ##instance variable
        self.empName=pempName


    def   displayInfo(self): ##method
        empSal = 20000   ## local variable
        print('Welcome Too OOPs Using Python'+str(empSal))

##obj  =  Emp()
##print(str(obj.empId)+"/"+obj.empName+"/"+obj.empEmail)

obj1  =  Emp(1002,"nikhil")
print(str(obj1.empId)+"/"+obj1.empName)
obj1.displayInfo();
