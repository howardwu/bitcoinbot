"""
The bot class is the fundamental class of bitcoinHFT.
Bots will analyze the market data, execute trades, and handle the user's 
balance.
"""
from random import randint

# from BotInterpreter import *
from TransactionManager import *
from wallet import *

class Bot(object):
	""" Analyzes market data, executes trades, makes decisions, handles
	user's balance. """
	def __init__(self):
		self.wallet = Wallet(100000)
		self.count = 4
		self.distributedBalance = self.wallet.balance() // self.count
		self.runningTMS = []
		self.strategies = []
		self.running = False

	def start(self):
		"""Starts the bot and creates the COUNT number of transaction mangers."""
		self.running = True
		for i in range(self.count):
			self.createTM(i, self.balance(), self.strategy())
		for transactor in self.runningTMS:
			transactor.start()
		# while self.running:
		# BotInterpreter(self).cmdloop()
		
		# while self.running:
		# 	self.update()
			
			# for transactor in self.runningTMS:
			# 	transactor.update()

	def update(self):
		"""Instructs each of the running TMs to update."""
		for transactor in self.runningTMS:
			transactor.update()

	def stop(self):
		"""Stops the bot and destroys all transaction managers."""
		self.running = False
		for transactor in self.runningTMS:
			self.destroyTM(transactor)

	def status(self):
		"""Gets the current status of the transaction managers in this bot."""
		for transactor in self.runningTMS:
			status = transactor.status() + ': $' + str(transactor.currentValue())
			status += '\n    Strategy: ' + str(transactor.currentStrategy()) + '%'
			print status

	def value(self):
		"""Gets the aggregate value in USD of the bot by getting the value in
		each of the transaction managers."""
		value = 0
		for transactor in self.runningTMS:
			value += transactor.currentValue()
		value += self.wallet.balance()
		return value

	##########################
	# Transaction Management #
	##########################

	def createTM(self, identifier, balance, strategy):
		"""Creates a new transaction manager."""
		transactor = TransactionManager(identifier, balance, strategy)
		self.runningTMS.append(transactor)

	def balance(self):
		"""Distributes the balance evenly among transaction managers."""
		if self.wallet.hasFunds(self.distributedBalance):
			self.wallet.subtract(self.distributedBalance)
			return self.distributedBalance

	def strategy(self):
		"""Creates a new strategy that is not current being used."""
		strategy = randint(1, 10)
		if strategy not in self.strategies:
			self.strategies.append(strategy)
			return strategy
		return self.strategy()

	def destroyTM(self, transactor):
		"""Destroys a transaction manager and reintegrates the 
		transaction manager's wallet with the bot's wallet."""
		transactor.stop()
		#INTEGRATE THE VALUE IN TRANSACTOR TO MY WALLET
		pass

if __name__ == '__main__':
	print("running")