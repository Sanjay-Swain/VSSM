# Archive File System 
v1.0 Specification

- All uses bigEndian
### FIRST CHUNK:
- The first chunk is reserved for the file system data:
    - First of all is a 64 bit integer signaling chunk size in bytes
    - A 64 bit chunk index signaling the start of the cache, this must be set to 0xFFFFFFFF if no 
     cache is present (cache ID must be 0, else no cache present will be asumed)
    - A 64 bit number of chunks reserved for the cache if none are reserved this must be 0
    - current Archive size in chunks
    - The rest is reserved.
    
    

#### CACHE:

- 8kb chunks reserved by default (configurable)
    - first 8 chunks reserved for cache (configurable)

The cache is a basically a FAT, whose ID will always be 1. The CACHE saves in the file ID as keys,
and the value is a list of the chunk addresses of the file, in order of part.
as the cache behaves as any other file in the archive, if it gets full, it can just behave like 
any other file in the archive, the same is for settings reserved chunks.

- The first entry of the cache must be all the cache parts
 
The cache entry format is as follows:

    [File ID;File Parts; Part 0; Part 1; ... Part N ]
    [64 bits; 64 bits  ;64 bits;64 bits; ... 64 bits]

this way the cache size is very small and 

if the cache is not present or its deleted, it must be reconstructed for rapid file access.

the overall structure is as follows:

    [FS Data] [Cache reserved space] [Data...]
    
if the cache uses reserved space, ends with 0x00000000 where a fileID is suposed to be

#### Chunks:
a chunk is compromised of the following things:
    
    [ File ID; File Part; DATA          ]
    [ 64 bits; 64 bits  ; rest of chunk ]

A chunk is marked as empty if its File ID is 0, as this file system is intended to be used 
within another file system as a file, for writing chunks that are non existent, it just appends
to the last part of the file.

A file is compromised of one or more chunks with the same file ID;
If a file uses just one chunk, its file part will be 0xFFFFFFFF that signifies last part of file, 
else, it will have the part number.



#### EXTRA:
The configuration file saves keys for settings of VSSM, its File ID will always be 2.

the archiveFS implementation must be able to truncate the file in wich it is present moving data 
to empty chunks and then truncating empty chunks at the end of the file.
