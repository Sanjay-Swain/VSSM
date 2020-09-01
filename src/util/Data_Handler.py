import lxml.etree as etree
import lxml
import random
import sqlite3


# This helps in creating root node for a xml file if for some reason the xml file contain unintended characters.
def create_root(file: str, root: str):
    xml_str = f"<{root}></{root}>"
    f = open(file, 'w+')
    f.write(xml_str)
    f.close()


def create_id():
    id_part = []
    for a in range(4):
        id_part.append(str(random.randint(1000, 9999)))
    return '-'.join(id_part)


class Client:
    root = 'client'

    def __init__(self, file):
        self.file = file  # File name of the client xml.
        try:        # Exception handling in case the file doesn't exist or empty.
            self.tree = etree.parse(file)       # Tree object of client xml file.
        except (lxml.etree.XMLSyntaxError, OSError, FileNotFoundError):
            create_root(file, self.root)
            self.tree = etree.parse(file)
        self.root_obj = self.tree.getroot()     # Root object.

    def create(self, name):
        data = etree.SubElement(self.root_obj, "data")
        id_node = etree.SubElement(data, 'id')
        name_node = etree.SubElement(data, 'name')
        id_node.text = create_id()
        name_node.text = name

    def remove(self, name):
        for data in self.root_obj:
            if data[1].text == name:
                data.getparent().remove(data)

    def search_id(self, name):
        for data in self.root_obj:
            if data[1].text == name:
                return [data[0].text, True]
        return [0, False]

    def save(self):  # This will write the changes to the file thereby making the changes permanent.
        xml_str = etree.tostring(self.root_obj, pretty_print=True).decode()
        f = open(self.file, 'w+')
        f.write(xml_str)
        f.close()

    def __str__(self):  # This will print the current status of the file in console.
        xml_str = etree.tostring(self.root_obj, pretty_print=True).decode()
        return xml_str


class Product(Client):
    root = 'product'


def buy(cursor, client, product, quantity):
    client_id = cli_obj.search_id(client)[0]
    product_id = prod_obj.search_id(product)[0]
    if prod_obj.search_id(product)[1]:
        cursor.execute(f"INSERT INTO purchase_data values('{client_id}', '{product_id}', '{quantity}')")
        conn.commit()
    else:
        print("Please check the client name and product name exists in the storage.")


def purchase_data(cursor):
    for a in cursor.execute("SELECT * FROM purchase_data"):
        print(a)


if __name__ == '__main__':
    print("=====YOU ARE RUNNING THIS FILE DIRECTLY=====")
    prod_obj = Product('product.xml')
    cli_obj = Client('client.xml')
    conn = sqlite3.connect("purchase.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS purchase_data (CID char(20), PID char(20), quantity int)")
    # Test Cases just remove the comments.
    cli_obj.create('test')
    cli_obj.remove('test')
    prod_obj.create('test')
    prod_obj.remove('test')
    print(cli_obj)
    print(prod_obj)
    buy(c, 'test', 'test', 2)
    purchase_data(c)
    cli_obj.save()
    prod_obj.save()
    conn.commit()
    conn.close()
