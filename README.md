# CFSM
*Client Based Sells Manager*

####*This program for now its in a pre-working state, so its really not ready to use in a regular basis*

CFSM aims to help sellers keep a control of the sells 
by providing a client driven classification of their sells, 
some basic inventory control and summarys of data.

For its initial development only cli will be used, without 
any fancy interface. 

>*Initial development will be over when all inicial 
feauters are implemented*


##Initial Features

-   **Client list**
    -   Clients names, and optional information.
    -   basic info like current debt

-   **Client detailed info**
    -   Client purchases info
    -   on a purchase by purchase basis

    -   debt info
        -   specific products in debt

-   **Purchases interface**
    -   Purchasing client selection
        -   Easy client creation just by entering name or some basic data
        -   Client search
        -   Anonymous client option
    -   Product to sell
        1.   Multiple product selection
        2.   Selectable quantity
        3.   Optional custom price
    - Modifiable purchase metadata (ie date)
    
- **Inventory**
    - Product adding
        - Name, price and optional description/metadata
    -   Product managing
    
     -   Price & stock properties
         -   Can be batch 
         -   Optional metadata (ie expiration date)
             -   Independent batch metadata
    
         -   Price and stock change 
         -   Batch adding/discarding

-   **Storage**
    -   All files stored on a .zip folder
        -  Including any configuration files
        -  Each file will be an inventory element, or client os their specific folders
    -   Optional encryption (no guarantees)
    -   (optional) extra parity checks to ensure data integrity (on a file per file basis)
 