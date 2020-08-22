from util.XML_handler import *


def help():
	print("""
	NOTE: The commands are not case sensitive
	NOTE: For commands save, help and exit the trailing data will be ignored.
	NOTE: ANd for create and remove commands the trailing data will be considered as a part of name.
	Commands:
		create <client|product> <Name>
		remove <client|product> <Name>
		save
		preview <client|product>
		help
		exit
		clear
	""")


def execute(func: list):
	"""
	:param func: This is a list containing [function, file, Name]
	:return: depends upon the function.
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
				help()
			elif func[0] == "clear":
				print("\n"*50)
		else:
			print("Invalid command")
	except KeyError:
		print(f"Please chose between [client|product] {func[1]} is not valid.")


command_list = ["help", "create", "remove", "save", "preview", "exit", "clear"]
file_dict = {"client": cli_obj, "product": prod_obj}
