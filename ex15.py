from sys import argv
# use argv to get the filename from the user
script, filename = argv
# open the file and assign the contents to variable 'txt'
txt = open(filename)
# prints the name of the file back to the user
print(f"Here's your file {filename}:")
# perform the 'read' function on the variable 'txt' with no parameters; print it
print(txt.read())
# ask the user to provide the text file name again
file_again = input("Type the filename again: ")

txt_again = open(file_again)

print(txt_again.read())
