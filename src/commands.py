import util.Templates as Templates


def _help():
    print("""
commands:
    help: Displays all commands
    create_client():  creates new client
    
    create_product(): creates new product
    
    remove_client():  removes client, also deletes all info form the archive and changing all history entres at his name 
                      to anonymos
                      
    remove_product(): removes product
    
    sell():           sells product to given client, also writing to history.
    
    save():           writes all loaded data to storage.
    
    open_archive():   if no archive is found at startup, this command can be used to open one manually, 
                      other open archives will be saved and closed.
                      
          """)


def create_client(name):
    client = Templates.Client(name=name)
    return client


def create_product(name):
    product = Templates.Product(name=name, batch_0={"stock": 0})
    return product


def sell(client, items, quantities,batch=0):
    pass

