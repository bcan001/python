import inheritance

cat = inheritance.Cat("Mister", "Cat")
print cat.hatesDogs() 				# from Cat class 
print cat.getSpecies()        # inherited from Pet class
print cat.getName()						# inherited from Pet class
print cat.__str__() 					# inherited from Pet class



print inheritance.duck