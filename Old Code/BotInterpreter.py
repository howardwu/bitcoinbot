import cmd
import sys
from btceapi import *
from bot import *
from wallet import *

class BotInterpreter(cmd.Cmd, object):
	"""A command interpreter that reads and interprets a command
	from the input.
	"""
	def __init__(self, Bot):
		cmd.Cmd.__init__(self)
		self.prompt = 'Bot> '
		self.bot = Bot
		self.temp = 0
		
	def do_status(self, arg):
		"""Get the current status of the Transaction Managers in our bot"""
		print self.bot.status()

	def do_stop(self, arg):
		"""Stops the trading bot."""
		print 'Stopping the trading bot.'
		self.bot.stop()
		return True

	def do_balance(self, arg):
		"""Returns the current USD balance."""
		print 'Balance: ' + str(self.bot.value())

	def do_price(self, arg):
		"""Returns the current price of 1 bitcoin in USD."""
		print 'BTC to USD Price: ' + str(getTicker('btc_usd').last)
		
	def do_market(self, arg):
		"""Returns the current market data about bitcoins."""
		print 'Market Data: '

	def do_error(self, arg):
		"""Gives the following output for commands specific to the bot."""
		print 'Bot is already running.'

	def do_quit(self, arg):
		"""Quit the trading system."""
		return True

	
	# def cmdloop(self, intro=None):
	# 	self.temp += 1
	# 	print "THIS IS AN UPDATE: YOU SUCK " + temp + " TIMES"
	# 	self.bot.update()
	# 	return cmd.Cmd.cmdloop(self, intro)




	# def onecmd(self, s):
	# 	print "THIS IS AN UPDATE: YOU SUCK"
	# 	self.bot.update()
	# 	return cmd.Cmd.onecmd(self, s)

	# def cmdloop(self):
	# 	print("IT WORKED")
	# 	# self.bot.update()
	# 	super(BotInterpreter, self).cmdloop()

	# def precmd(self, line):
	# 	"""Executes before every prompt to the user."""
	# 	print('This is the fuckin precmd yo')
	# 	self.bot.update()

	"""Shortcut for quitting the program"""
	do_q = do_quit

	"""Bot Specific Commands"""
	do_start = do_error

	# def do_model(self, arg):
	#     if arg:

	#         return models.getModel(arg)