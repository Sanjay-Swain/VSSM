from xml.dom import minidom
import xml
import xmlformatter

formatter = xmlformatter.Formatter()


# This helps in creating root node for a xml file if for some reason the xml file contain unintended characters.
def create_root(file: str, root: str):
	xml_str = f"<{root}></{root}>"
	f = open(file, 'w+')
	f.write(xml_str)
	f.close()


def check_data(root_obj):  # This help in creating id for client and product.
	count = 0
	for _ in root_obj.getElementsByTagName('data'):
		count += 1
	return count


class Client:
	root = 'client'

	def __init__(self, file):
		self.file = file  # File name of the client xml.
		try:
			self.document = minidom.parse(file)		# minidom document object of client xml file.
		except xml.parsers.expat.ExpatError:		# Exception handling in case the file is empty
			create_root(file, self.root)
			self.document = minidom.parse(file)

	def create(self, client_name):
		id_val = check_data(self.document) + 1
		# Create <data /> node
		data_node = self.document.createElement("data")

		# Create <id />
		id_node = self.document.createElement("id")
		id_text = self.document.createTextNode(str(id_val))
		id_node.appendChild(id_text)  # Create <id>id_text</id>

		# Create <name /> node
		name_node = self.document.createElement('name')
		name_txt = self.document.createTextNode(client_name)

		# Create <name>name_txt</name> node
		name_node.appendChild(name_txt)

		data_node.appendChild(id_node)
		data_node.appendChild(name_node)
		self.document.childNodes[-1].appendChild(data_node)

		xml_str = formatter.format_string(self.document.toxml(encoding="UTF-8")).decode()
		f = open(self.file, 'w+')
		f.write(xml_str)
		f.close()

	def remove(self, client_name):
		for data in self.document.getElementsByTagName('name'):
			if data.firstChild.nodeValue == client_name:
				parent = data.parentNode
				parent.parentNode.removeChild(parent)
		xml_str = formatter.format_string(self.document.toxml(encoding="UTF-8")).decode()
		f = open(self.file, 'w+')
		f.write(xml_str)
		f.close()

	def __str__(self):
		xml_str = formatter.format_string(self.document.toxml(encoding="UTF-8")).decode()
		return xml_str


class Product(Client):
	root = 'product'


prod_obj = Product('product.xml')
cli_obj = Client('client.xml')


if __name__ == '__main__':
	print("=====YOU ARE RUNNING THIS FILE DIRECTLY=====")
	# cli_obj.create('test')
	# cli_obj.remove('test')
	# prod_obj.create('test')
	# prod_obj.remove('test')
	# print(cli_obj)
	# print(prod_obj)
