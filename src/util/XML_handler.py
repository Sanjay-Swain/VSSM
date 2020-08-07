import xml.dom.minidom as minidom
import xml
import xmlformatter


def check_data(root_obj):                           # This help in creating id for client.
    count = 0
    for _ in root_obj.getElementsByTagName('data'):
        count += 1
    return count


def create_root(file_name: str):                    # This function checks if the file has a root node or not.
    xml_str = "<client></client>"
    f = open(file_name, 'w+')
    f.write(xml_str)


def create_client(dom_object, name):
    id_val = check_data(dom_object) + 1

    data_node = dom_object.createElement("data")        # Create <data /> node

    id_node = dom_object.createElement("id")            # Create <id />
    id_text = dom_object.createTextNode(str(id_val))
    id_node.appendChild(id_text)                        # Create <id>id_text</id>

    name_node = dom_object.createElement('name')        # Create <name /> node
    name_txt = dom_object.createTextNode(name)
    name_node.appendChild(name_txt)                     # Create <name>name_txt</name> node

    data_node.appendChild(id_node)
    data_node.appendChild(name_node)
    dom_object.childNodes[-1].appendChild(data_node)

    xml_str = formatter.format_string(dom_object.toxml(encoding="UTF-8")).decode()
    with open(file, "w") as f:
        f.write(xml_str)


def remove_client(dom_object, name):
    for node in [data for data in dom_object.getElementsByTagName('name') if data.firstChild.nodeValue == name]:
        parent = node.parentNode
        parent.parentNode.removeChild(parent)
    xml_str = formatter.format_string(dom_object.toxml(encoding="UTF-8")).decode()
    print(xml_str)
    with open(file, "w") as f:
        f.write(xml_str)


file = 'client.xml'
# This is used to read the data from the xml file.
try:
    client = minidom.parse(file)
except xml.parsers.expat.ExpatError:            # Exception handling in case the file is empty
    create_root(file)
    client = minidom.parse(file)
formatter = xmlformatter.Formatter()


if __name__ == '__main__':
    print("=====YOU ARE RUNNING THIS FILE DIRECTLY=====")
    # create_client(client, 'test_name')
    # remove_client(client, 'test_name')
