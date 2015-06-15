# guessing game using python

# class GuessingGame:
#   def __init__(self, game_number):
#     if isinstance(game_number,int):
#       self.game_number = game_number
#       self.user_guess = 0
#       self.done = False
#     else:
#       self.done = True

#   def play(self):
#     while (self.done == False):
#       self.get_user_guess()
#       self.check_guess()
#     print "You are correct!"

#   def get_user_guess(self):
#     self.user_guess = raw_input("What number would you like to Guess?")
#     self.user_guess = int(self.user_guess)
#     return self.user_guess

#   def check_guess(self):
#     # self.user_guess is always greater than self.game_number
#     if self.user_guess > self.game_number:
#       print "Too High"
#     elif self.user_guess < self.game_number:
#       print "Too Low"
#     else:
#       self.done = True

# game = GuessingGame(45)
# # print game.game_number
# # print game.user_guess
# # print game.done

# # print game.get_user_guess()
# game.play()


# refactored python code:
import random

class GuessingGame:
  def __init__(self):
    self.game_number = random.randint(0,50)
    self.user_guess = 0
    self.done = False
    
  def play(self):
    while (self.done == False):
      self.get_user_guess()
      self.check_guess()
    print "You are correct!"

  def check_guess(self):
    # self.user_guess is always greater than self.game_number
    if self.user_guess > self.game_number:
      print "Too High"
    elif self.user_guess < self.game_number:
      print "Too Low"
    else:
      self.done = True

  def get_user_guess(self):
    self.user_guess = raw_input("What number would you like to Guess? (0-50)")
    self.user_guess = int(self.user_guess)
    return self.user_guess

game = GuessingGame()
# print game.game_number
# print game.user_guess
# print game.done

# print game.get_user_guess()
game.play()





# below is ruby code for the same game --------------------------------------------------

# class GuessingGame
# 	attr_accessor :game_number, :user_guess, :done
#   def initialize(game_number)
#   	if game_number.is_a?(Integer)
#   		@game_number = game_number
#   		@user_guess = nil
#   		@done = false
#   	else
#   		@done = true
#   		puts "invalid number input"
#   	end
#   end

#   def play
#   	while @done == false
#   		get_user_guess
#   		check_guess
#   	end
#   end

#   def check_guess
#   	if @user_guess > @game_number
#   		p "You are High"
#   	elsif @user_guess < @game_number
#   		p "You are Low"
#   	else
#   		p "You Got It!"
#   		@done = true
#   	end
#   end

#   def get_user_guess
#     puts "What number would you like to guess?"
#     input = gets.chomp
#   	@user_guess = input.to_i
#   end
# end