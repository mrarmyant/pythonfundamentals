# use %s as a placeholder for strings and %d as a placeholder for numbers
hw = "Hello %s" % "world"
py = "I love Python %s" % 3
print(hw, py)
# the output would be: Hello world I love Python 3
# we can also pass variables
name = "Zen"
age = 27
print("My name is %s and I'm %d" % (name, age))