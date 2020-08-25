from util.XML_handler import *

help_str = """NOTE: The commands are not case sensitive
NOTE: For commands help and exit the trailing data will be ignored.
NOTE: And for create and remove commands the trailing data will be considered as a part of name.
Commands:
	create <client|product> <Name>
	remove <client|product> <Name>
	save
	preview <client|product>
	help
	exit
	clear
	"""

create_help_str = """create:
	Syntax: create <client|product> <name>
All must be separated by spaces and all last trailing data will be considered as a part of name."""
remove_help_str = """remove:
	syntax: remove <client|product> <name>
All must be separated by spaces and all last trailing data will be considered as a part of name."""
save_help_str = """save:
	syntax <client|product>
This save all the changes in current session and cannot be undone (yet)."""
preview_help_str = """preview:
	syntax: preview <client|product>
This show the current status of complete file."""
exit_help_str = """exit:
	syntax: exit
This will close the program after asking conformation."""
clear_help_str = """clear:
	syntax: clear
It will clear the screen by printing empty strings."""
help_help_str = "Really now you are asking for this come on!!"

prod_obj = Product('util\\product.xml')
cli_obj = Client('util\\client.xml')


def help(command = None):
	if command is None:
		print(help_str)
	elif command == "create":
		print(create_help_str)
	elif command == "remove":
		print(remove_help_str)
	elif command == "save":
		print(save_help_str)
	elif command == "exit":
		print(exit_help_str)
	elif command == "preview":
		print(preview_help_str)
	elif command == "clear":
		print(clear_help_str)
	elif command == "help":
		print(help_help_str)
	else:
		print("Well it seems like your command doesn't exist.. :(")


def execute(func: list):
	"""
	:param func: This is a list containing [function, file, Name]
	"""
	try:
		func_len = len(func)
		if func_len > 0 and func[0] in command_list:
			if (func[0] in ["create", "remove"] and func_len < 3) or (func[0] in ["save", "preview"] and func_len < 2):
				print("More information required to execute the given command")
				print("Type help for more information")
			elif func[0] == "create":
				file = file_dict[func[1]]
				file.create(' '.join(func[2:]))
			elif func[0] == "remove":
				file = file_dict[func[1]]
				file.remove(' '.join(func[2:]))
			elif func[0] == "save":
				file = file_dict[func[1]]
				file.save()
			elif func[0] == "preview":
				print(file_dict[func[1]])
			elif func[0] == "help":
				try:
					help(func[1])
				except IndexError:
					help()
			elif func[0] == "clear":
				print("\n"*50)
		else:
			print("Invalid command")
	except KeyError:
		print(f"Please chose between [client|product] {func[1]} is not valid.")


command_list = ["help", "create", "remove", "save", "preview", "exit", "clear"]
file_dict = {"client": cli_obj, "product": prod_obj}
