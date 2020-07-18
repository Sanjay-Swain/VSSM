"""
on this file, all elements necessary to deal with .VSSM archives are handled
"""


class FileHandler:

    def __init__(self, archive: str):
        self.path = archive
        self.file = open(archive, "b+")
        self.filesize = self.file.seek(0, 2)

    def offset_at(self, place, offset, chunksize=8192):
        if offset > chunksize:
            return "Error: offset bigger than chunksize"

        size = self.file.seek(0, 2) - place
        if size < chunksize*2:
            padding = ((chunksize*2) - (size % (chunksize*2))) % (chunksize*2)
            padded = [True, padding]
            while 0 < padding:
                self.file.write(" ".encode())
                padding -= 1
        else:
            padded = [False]

        self.file.seek(place)
        temp = [None, None]
        temp[0] = self.file.read(chunksize)
        temp[1] = self.file.read(chunksize)
        next_temp = self.file.tell()
        self.file.seek(place - offset)
        pointer = self.file.tell()
        print([self.file.tell(), pointer])
        while True:
            if (temp[0] != "\x00") and (temp[0] != ""):  # fileidk why, but i had to apparently
                self.file.write(temp[0])
                self.file.flush()
                self.file.seek(next_temp)
                temp[0] = self.file.read(4)
                next_temp += 4
                pointer += 4
                self.file.seek(pointer)
                temp[0], temp[1] = temp[1], temp[0]
            else:
                break

        if padded[0] is True:
            size = self.file.seek(0, 2)
            self.file.truncate(size - padded[1])

    def read_at(self, place: int, size: int):
        self.file.seek(place)
        return self.file.read(size)

    def write_at(self, place: int, content: bytes):
        self.file.seek(place)
        self.file.write(content)
        a = self.file.read()


class ArchiveHandler(FileHandler):

    def __init__(self, archive):
        # initialise
        super().__init__(archive)
        self.reflist = {}
        # load FS data
        self.chunksize = self.from_bytes(self.file.read(8))
        self.cache_start = self.from_bytes(self.file.read(8))
        self.cache_reserved = self.from_bytes(self.file.read(8))
        self.current_size = self.from_bytes(self.file.read(8))
        if self.cache_start != 0xFFFFFFFF:
            self.cache_present = True
            self.reflist += {1: [self.cache_start]}
        else:
            self.cache_present = False

    # Loading and constructing cache

    def load_cache(self):
        temp = self.load_file(1)

        if self.from_bytes(temp[:8]) == 1:
            for wordcount in range(self.from_bytes(temp[8:16])):
                self.reflist[1].append(self.from_bytes(temp[wordcount*8:(wordcount+1)*8]))
            #rereads cache file after reading cache file parts
            temp = self.load_file(1)
            wordcount = 0
            while True:
                word = self.from_bytes(temp[wordcount * 8:(wordcount + 1) * 8])
                if  word == 0:
                    break

                fileid = word
                wordcount += 1
                word = self.from_bytes(temp[wordcount * 8:(wordcount + 1) * 8])
                if not(word in self.reflist):
                    self.reflist += {word: []}

                for wordcount in range(word):
                    if word in self.reflist[fileid]:
                        wordcount += 1
                    else:
                        self.reflist[fileid].append(word)
                        wordcount += 1
        else:
            self.build_cache()

    def build_cache(self):
        for i in range(1):
            pass

    def update_file_cache(self):
        pass

    # Managing RAM references
    def add_reference(self, fileid: int, index: list):
        self.reflist += {fileid: index}

    def remove_reference(self, fileid: int):
        self.reflist.pop(fileid)

    def edit_reference(self, fileid: int, start=None, end=None):
        if start is not None:
            self.reflist[fileid][0] = start

        if end is not None:
            self.reflist[fileid][1] = end

    def rename_reference(self, fileid: int, newfileiden):
        self.reflist[newfileiden] = self.reflist.pop(fileid)

    # File Writing and reading
    def load_file(self, fileid):
        file = bytearray
        for ref in self.reflist[fileid]:
            file.append((bytearray(self.read_at(self.reflist[fileid][ref], self.chunksize))))
        return file

    def write_file(self, fileid, content):
        pass

    def truncate_file(self, fileid, size):
        pass

    def delete_file(self, fileid):
        pass

    # basic operation corrected with chunksize
    def read_at(self, place: int, size: int):
        return super().read_at(place*self.chunksize, size)

    def write_at(self, place: int, content: bytes):
        return super().write_at(place*self.chunksize, content)

    def from_bytes(self,bytes: bytes,signed=False):
        return int.from_bytes(bytes,"big",signed=signed)
