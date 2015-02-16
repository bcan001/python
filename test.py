print "hello, this is python"

var = "maybe"

if var == "yes":
	print "that is correct"
elif var == "maybe":
	print "call me maybe"
else:
	print "nope"


# data structures
my_array = [1,2,3,4,5,6,7,8]
print my_array[0]

my_hash = {"key1":"value1", "key2":"value2", "key3":"value3"}
print my_hash["key1"]
print my_hash["key3"]

for val in my_array:
	print val

for key in my_hash:
	print my_hash[key]

