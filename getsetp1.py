class Employee:
    def __init__(self,name,salary):
        self._name=name
        self._salary=salary
    def set_salary(self,salary):
        self._salary=salary
    def get_salary(self):
        return self._salary
    
E1=Employee("Raj",90000)
print("Salary before update: ",E1.get_salary())
E1.set_salary(99999)
print("Salary after update: ",E1.get_salary())
