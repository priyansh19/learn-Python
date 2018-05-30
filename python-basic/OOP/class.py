
class Employee():

	noofemployee = 0    #class variable
	raise_amount = 1.04
	
	def __init__(self,first,last,pay):
		self.first = first #instance variable
		self.last  = last
		self.pay   = pay
		self.email = first + '.' + last + '@company.com'
		Employee.noofemployee += 1 

	def fullname(self):
		return('{} {}'.format(self.first,self.last))

	def empraise(self):
		self.pay = int(self.pay * self.raise_amount)

	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amount = amount

	@classmethod
	def from_string(cls, emp_str):
		first, last, pay = emp_str.split('-')
		return(cls(first, last, pay))

	@staticmethod
	def is_workday(day):
		pass


class Developer(Employee):
	raise_amount = 1.10

	def __init__(self,first,last,pay, pro_lang):
		super().__init__(first,last,pay)
		self.pro_lang = pro_lang

class Manager(Employee):
	def __init__(self, first, last, pay, employees=None):
		super().employees

dev = Developer('Abhishek','Verma',120000,'Python')

print(dev.pay)
dev.empraise()
print(dev.pay)
print(dev.pro_lang)

# emp_1 = Employee('Abhishek', 'Verma', 120000)
# emp_string = 'Abhishek-Verma-120000'
# emp_2 = Employee.from_string(emp_string)
# print(emp_2.fullname())
# print(Employee.raise_amount)
# Employee.set_raise_amt(1.05)
# print(Employee.raise_amount)
