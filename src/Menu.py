import commands

print("Welcome to VSSM v0.01")
print("type help to see available commands")
print("Current version of program doesn't have much features to use.")
print("For now this program maybe helpful for storing names of products|client.")
print()

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
