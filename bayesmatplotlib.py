import numpy as np  
import matplotlib.pyplot as plt  

# def graph(formula, x_range):  
#     x = np.array(x_range)  
#     y = formula(x)  # <- note now we're calling the function 'formula' with x
#     plt.plot(x, y)  
#     plt.show()  

# def my_formula(x):
#     return x**3+2*x-4

# graph(my_formula, range(-10, 11))


# =============


# A sampling distribution is the probability of seeing our data (X) given our parameters (θ). This is written as p(X|θ).
# 2 means 2 possible answers, heads or tails
# coin flipped 1000 times
# calculates the mean distribution between heads and tails
data_coin_flips = np.random.randint(2, size=1000)
print np.mean(data_coin_flips)
