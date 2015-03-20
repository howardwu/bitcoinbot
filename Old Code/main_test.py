import cmd
import subprocess
import threading

from bot import *
from btceapi import *
from wallet import *

class Main(object):
	t = None
	bot = None

	def __init__(self):
		self.prompt = "User> "
		self.balance = 100000
		self.bot = None
		# self.bot = subprocess.Popen('python bot.py', shell=True,
		# 	stdin=subprocess.PIPE, stdout=subprocess.PIPE)
		self.running = False

	def start(self):
		"""Starts the trading bot."""
		self.running = True
		print 'Starting the trading bot.'
		# cmd1 = 'bot = Bot()'
		# cmd2 = 'bot.start()'
		# self.bot.stdin.write('%s\n%s\n' % (cmd1, cmd2))
		# output = self.bot.stdout.readline()
		# print output.rstrip()
		# self.prompt = "Botter> "
		self.bot = Bot(self.balance, 4)
		self.t = threading.Thread(target=self.bot.start)
		self.t.start()

	def status(self):
		"""Get the current status of the Transaction Managers in our bot"""
		# cmd = 'bot.status()'
		# self.bot.stdin.write('%s\n' % cmd)
		# output = self.bot.stdout.readline()
		# print output.rstrip()
		print self.bot.status()

	def stop(self):
		"""Stops the trading bot."""
		print 'Stopping the trading bot.'
		self.bot.stop()
		return True
		
	def balance(self):
		"""Returns the current USD balance."""
		print 'Balance: ' + str(self.balance)

	def price(self, arg):
		"""Returns the current price of 1 bitcoin in USD."""
		print 'BTC to USD Price: ' + str(getTicker('btc_usd').last)
		
	def market(self, arg):
		"""Returns the current market data about bitcoins."""
		print 'Market Data: '

	def error(self, arg):
		"""Gives the following output for commands specific to the bot."""
		print 'Bot is not running.'

	def quit(self, arg):
		"""Quit the trading system."""
		return 'quit()'

if __name__ == '__main__':
	f = open('welcome.txt', 'r')
	print f.read()
	console = Main()
