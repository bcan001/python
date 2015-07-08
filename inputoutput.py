my_list = [i**2 for i in range(1,11)]
# Generates a list of squares of the numbers 1 - 10
# my_list = [1,4,9,16,25,36,49,64,81,100]

f = open("output.txt", "w")

for item in my_list:
    f.write(str(item) + "\n")

f.close()
