from src.util.XML_handler import *

print("Welcome to VSSM v0.01")  # Removed some zeros : )
print("type help for seeing available commands")

running = True

while running:
	command_input = input("VSSM > ").strip().lower().split()
	execute(command_input)
	if command_input[0] == "exit":
		verify = input("Are you sure you want to leave without saving changes (Y|N) :")
		if verify[0].strip().lower() == 'y':
			running = False
