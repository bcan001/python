# the computer will try to guess a number I input
import random

class GuessGame:
	def __init__(self,my_num):
		if isinstance(my_num,int):
			self.my_num = my_num
			self.done = False
			self.computer_guess = 0
			self.computer_guess_count = 0
		else:
			print "Invalid number input"
			self.done = True

	def play(self):
		while (self.done == False):
			self.get_computer_guess()
			self.check_computer_guess()
			self.count_computer_guess()
		print "It took the computer %d tries to guess your number!" % self.computer_guess_count

	def get_computer_guess(self):
		self.computer_guess = random.randint(0,1000)
		return self.computer_guess

	def count_computer_guess(self):
		self.computer_guess_count = self.computer_guess_count + 1
		return self.computer_guess_count

	def check_computer_guess(self):
		if self.computer_guess == self.my_num:
			self.done = True


game = GuessGame(50)
game.play()