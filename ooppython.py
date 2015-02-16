# oop concepts in python

class Player:
	# 'counts every time a new player is created'
	plyrCount = 0
	def __init__(self, name, age):
		self.name = name
		self.age = age
		Player.plyrCount += 1

	def displayPlayerCount(self):
		print "Total Players: %d" % Player.plyrCount

	def displayPlayer(self):
		print "Name: ", self.name, "Age: ", self.age

# creating objects and access attributes:

player1 = Player("Ben", 26)
print player1.name
print player1.age
player1.displayPlayer()
player2 = Player("Mary", 45)

print
print Player.plyrCount


# how to update attributes of objects

player1.name = "Jimmy"
print player1.name
#del player1.age
print player1.age

hasattr(player1, 'age')    # Returns true if 'age' attribute exists
getattr(player1, 'age')    # Returns value of 'age' attribute
setattr(player1, 'age', 8) # Set attribute 'age' at 8
#delattr(player, 'age')    # Delete attribute 'age'

print player1.age


# Built-In class attributes
print "Player.__doc__:", Player.__doc__
print "Player.__name__:", Player.__name__
print "Player.__module__:", Player.__module__
print "Player.__bases__:", Player.__bases__
print "Player.__dict__:", Player.__dict__


# destroying objects


