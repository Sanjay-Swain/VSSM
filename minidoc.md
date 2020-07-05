# Mini Documentation

This is meant to specify the program inner workings in a resumed manner, 
including not yet implemented features.

thi is some sort of to do list, but a little more in detail.

>Theres probably a better way to do this, but i was too lazy to find one.
>>If someone recomends something, i'll surely do it.

---
---
### `Menu.py`
probably temporal name, used for starting the program and parsing the 
comands entered.


### `xml_handler.py` (util)
used to handle xml files from the archive.
it can:
Initiate template classes based on the contents of anmplate.
- or

Take a "stuffed" class and save its contents on a .xml file

### `xml structure`
all xml start by their type, that can be:
1. client
2. product
3. configuration file
4. "other important"
5. cache

#### 1. client
starts with `<client>` and has all the metadata asociated with it.

obligatory fields: `<name>,<ID>`

#### 2. Product
obligatory field: `<name>,<ID>`
products can be either `stock` or `batch` type products.

- `stock` type just maintains a count of the product quantity
sharing the metadata with all the stock.

- `batch` types handles different *batches* of the same product, 
with each *batch* having a separate product count and metadata, 
though the same types of metadata are peresent on all the batches 
of the product.


#### 3. Configuration file
currently not in use, but there will be only one of these type of 
file per archive. its job is to hold any posible customisation CFSM 
may allow in the future 

#### 4. Other important
this will other important information

for now just the purchase history
- each entry on the purchase history must have the ID of buyer (0 == anonymous), 
sell date, the ID of each product selled and the respective quantity.
#### 5. Cache
this file will hold metadata key names used in the past, for a quick 
access when reusing them, like creating a new product or client.

it may hold other temporal information like the name and ID of all clients 
for speeding up search.