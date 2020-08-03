# Archive File System 
v1.0 Specification

- All uses little endian
### FIRST CHUNK:
- The first chunk is reserved for the file system data:
    - First of all is a 64 bit integer signaling chunk size in bytes
    - current Archive size in chunks (64 bits)
    - Max fs size in chunks
    - The rest is reserved

the overall structure is as follows:

    [FS Data][Data...]

#### Chunks:
a chunk is compromised of the following things:
    
    [ File ID; File Part; DATA          ]
    [ 64 bits; 64 bits  ; rest of chunk ]

A chunk is marked as empty if its File ID is 0, as this file system is intended to be used 
within another file system as a file, for writing chunks that are non existent, it just appends
to the last part of the file or fail if the write exceeds max size. 

A file is compromised of one or more chunks with the same file ID;
If a file uses just one chunk, its file part will be 0xFFFFFFFF that signifies last part of file, 
else, it will have the part number.

the archiveFS implementation must be able to truncate the file in which it is by present moving data 
to empty chunks and then truncating empty chunks at the end of the file.

special file IDs used in the archive are: 1 for configs file and 2 for action history