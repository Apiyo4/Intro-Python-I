"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE


foo_file = open(r"C:\Users\HP\Documents\lambda\Python\Intro-Python-I\src\foo.txt")
# foo_file = open("foo.txt", "r")
read_data = foo_file.read()
foo_file.close()
print(read_data)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
bar_file = open("bar.txt", "r+")
bar_file.write("I'm not just a pretty girl \nI can swear, I can joke \nI say what's on my mind \nIf I drink, if I smoke, I keep up with the guys \nAnd you'll see me holding up my middle finger to the world ")
bar_file.close()
bar_file = open("bar.txt", "r")
read_new_data = bar_file.read()
bar_file.close()
print(read_new_data)