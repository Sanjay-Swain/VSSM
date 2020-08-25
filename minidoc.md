# Mini Documentation

This is meant to specify the program inner workings in a resumed manner, 
including not yet implemented features.

thi is some sort of to do list, but a little more in detail.

>There's probably a better way to do this, but i was too lazy to find one.
>>If someone recommends something, i'll surely do it.

---
---
### `Menu.py`
probably temporal name, used for starting the program and parsing the 
commands entered.

#### 1. client
Starts with `<client id=x>` and has all the metadata associated with it.

Obligatory fields: `<name>`

#### 2. Product
Starts with `<product id=x>` and has all the metadata associated with it.
Obligatory field: `<name>,`


- each product works with *batches* with each *batch* having a separate 
product count and metadata, though the same types of metadata are peresent 
on all the batches of the product.

#### 3. Configuration file
Currently not in use, but there will be only one of these type of 
file per archive. its job is to hold any possible customisation VSSM 
may allow in the future 

#### 4. Other important
This will other important information

For now just the purchase history
- Each entry on the purchase history must have the ID of buyer (0 == anonymous), 
sell date, the ID of each product sold and the respective quantity.

### `Templates.py` (util)
has all predefined structures used by other code, right now it has a queue, and
basic product/client stuffable structs