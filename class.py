class Employees(object):
	def __init__(self,	name, rate, hours): 
		self.name=name 
		self.rate=rate 
		self.hours=hours
	
staff=Employees("Wayne",20,8)
supervisor=Employees("Dwight",35,8)
manager=Employees("Melinda",100,8)
	
print(staff.name,staff.rate,staff.hours)
print(supervisor.name,supervisor.rate,supervisor.hours)
print(manager.name,manager.rate,manager.hours)

class Resigned(Employees):
	def	__init__(self,name,rate,hours,status):
		self.name=name
		self.rate=rate
		self.hours=hours
		self.status=status

exemp_1=Resigned("Dorothy",	32,	8,"retired") 
exemp_2	=Resigned("Malcolm",48,8,"resigned")
	
print(exemp_1.name,	exemp_1.rate,exemp_1.hours,exemp_1.status)
print(exemp_2.name,	exemp_2.rate,exemp_2.hours,	exemp_2.status)
	