from util.XML_handler import *
import commands


print("Welcome to VSSM v0.01")  # Removed some zeros : )
print("type help for seeing available commands")
print("Current version of program has almost no features to use.")
print("For now this program maybe helpful for storing names of data.")

running = True

while running:
	try:
		command_input = input("VSSM > ").strip().lower().split()
		if command_input[0] == "exit":
			verify = input("Are you sure you want to leave without saving changes (Y|N) :")
			if verify[0].strip().lower() == 'y':
				running = False
		commands.execute(command_input)
	except IndexError:
		print("Please check the syntax of the command.")
