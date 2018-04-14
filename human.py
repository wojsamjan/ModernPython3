class Human:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self._age = max(age, 0)

	@property
	def age(self):
		return self._age

	@age.setter
	def age(self, value):
		if value >= 0:
			self._age = value
		else:
			raise ValueError("age can not be negative!")

	@property
	def full_name(self):
		return f"{self.first} {self.last}"

	@full_name.setter
	def full_name(self, name):
		self.first, self.last = name.split(" ")


stan = Human("Stan", "DeePaQ", 24)
print(stan.age)
stan.age = 25
print(stan.age)
print(stan.full_name)
stan.full_name = "Yashi Yashimoto"
print(stan.__dict__)
