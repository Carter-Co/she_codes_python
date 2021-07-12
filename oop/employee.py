class Employee:

    def __init__(self, name, salary, phone, start_date):
        self.name = name
        self.salary = salary
        self.phone = phone
        self.start_date = start_date

    def __str__(self):
        return self.name

    def get_employment_details(self):
        return (self.name, self.salary, self.start_date)

    def get_contact_details(self):
        return (self.name, self.phone)
    
Employee1 = Employee("Abby Carter", 50000, "0400175881", "October 15 2021")
#print(Employee1.name)
#print(Employee1.salary)
#print(Employee1.phone)
#print(Employee1.start_date)

Employee2 = Employee("Paul Carter", 40000, "0488175888", "September 15 2021")
#print(Employee2.name)
#print(Employee2.salary)
#print(Employee2.phone)
#print(Employee2.start_date)

print(Employee1)
print(Employee1.get_employment_details())
print(Employee2)
print(Employee2.get_contact_details())

