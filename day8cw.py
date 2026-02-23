class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def show_details(self):
        print(self.name,self.age)
    
        
class employee(person):
    def __init__(self,name,age, employee_id):
        super().__init__(name,age)
        self.employee_id=employee_id
    
    def show_details(self):
        print(self.name,self.age,self.employee_id)
        
class partTime (person):
    def __init__(self, name, age, working_hours):
        super().__init__(name, age)
        self.working_hours=working_hours
        
    def show_details(self):
       print(self.name,self.age,self.working_hours)

class consultant(employee,partTime):
    def __init__(self,name,age,employee_id,working_hours,projectname):
        person.__init__(self, name, age)
        self.employee_id=employee_id
        self.working_hours=working_hours
        self.projectname = projectname
    
    def show_details(self):
        print(self.name,self.age,self.employee_id,self.working_hours,self.projectname)
        
p=person("aiswarya",24)
e=employee("arsha",32,"5")
pt=partTime("anjana",23,7)
c=consultant("anaswara", 25, "5", 7, "pythonproject")

p.show_details()
e.show_details()
pt.show_details()
c.show_details()  