class Employee():
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def get_info(self):
        print(f'Имя сотрудника: {self.name} \n Айди: {self.id}')

class Manager(Employee):
    def __init__(self, name, id, departament):
        Employee.__init__(self, name, id)
        self.departament = departament
    def manage_project(self):
        print(f'Проектом управляет: {self.name} {self.id} из отделa: {self.departament}')

class Technician(Employee):
    def __init__(self, name, id, specialization):
        super().__init__(name, id)
        self.specialization = specialization
    def perform_mainyenance(self):
        print(f'Техническое обслуживание выполняет: {self.name} {self.id}, по специальности: {self.specialization}')

class TechManager(Manager, Technician):
    def __init__(self, name, id, departament, specialization):
        super().__init__( name, id, departament)
        super().__init__( name, id, specialization)
        self.team = []
    def get_info(self):
        print(f'Имя Босса: {self.name} \n Айди: {self.id}')
    def add_employee(self, new_employee):
        self.team.append(new_employee)
    def get_team_info(self):
        print("Команда: ")
        for employee in self.team:
            employee.get_info()

boss = TechManager('Дмитрий', '1', 'Управления', 'Самый крутой')
emp1 = Employee('Eгор', '122')
tch1 = Technician('Виталик', '148','Электрик')
tch1.perform_mainyenance()
mng1 = Manager('Кирилл', '173','Продажи')
mng1.manage_project()
boss.add_employee(emp1)
boss.add_employee(tch1)
boss.add_employee(mng1)
boss.get_info()
boss.get_team_info()