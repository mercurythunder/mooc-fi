class BankAccount:
	def __init__(self, owner: str, account_number: str, balance: float):
		self.__owner = owner
		self.__account_number = account_number
		self.__balance = balance
	
	@property
	def balance(self):
		return self.__balance

	def deposit(self, amount: float):
		if amount > 0:
			self.__balance += amount
			self.__service_charge()
	
	def withdraw(self, amount: float):
		if amount > 0 and self.__balance >= amount:
			self.__balance -= amount
			self.__service_charge()
	
	def __service_charge(self):
		self.__balance *= 0.99

if __name__ == "__main__":
	account = BankAccount("Randy Riches", "12345-6789", 1000)
	account.withdraw(100)
	print(account.balance)
	account.deposit(100)
	print(account.balance)