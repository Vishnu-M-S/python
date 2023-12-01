class Bank_Account:
	def __init__(self):
		self.account_balance=0
		print("WELCOME")
	def deposit(self):
		d=int(input("Enter the amount to deposit: "))
		self.account_balance+=d
		print("Amount Credited",d)
	def witdraw(self):
		w=int(input("Enter the amount to witdraw: "))
		if self.account_balance >= w:
			self.account_balance-=w
			print("Amount withdrawn: ",w)
		else:
			print("Insufficient Balance: ")
	def display(self):
		print("Current Balance: ",self.account_balance)
obj=Bank_Account()
obj.deposit()
obj.witdraw()
obj.display()

