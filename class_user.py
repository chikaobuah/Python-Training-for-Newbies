class User():

	def __init__(self,first_name,last_name, **others):
		self.others = {}
		self.others['first_name'] = first_name
		self.others['last_name'] = last_name
		for key, value in others.items():
			self.others[key] = value 
		
	def describe_user(self):
		print('\nUser name:'+ ' ' + self.others['first_name'].title()+ ' ' + self.others['last_name'].title())
		print(self.others)
	
	def greet_user(self):
		print('\nHello'+ ' ' + self.others['first_name'].title()+ ' ' + self.others['last_name'].title())
		
chika = User('chika', 'obuah', location='princeton', field='physics')
samson = User('samson', 'soyombo')
ayo = User('ayo', 'ojikutu')

chika.describe_user()
samson.describe_user()
ayo.describe_user()

chika.greet_user()
samson.greet_user()
ayo.greet_user()


		