class FileHandler:

    def __init__(self, archive: str):
        self.path = archive
        self.file = open(archive, "r+")
        self.filesize = self.file.seek(0, 2)

    def offset_seek(self, offset: int):
        self.file.seek(self.file.tell() + offset)

    def read_at(self, place: int, size: int):
        self.file.seek(place)
        return self.file.read(size)

    def write_at(self, place: int, content: str):
        # TODO fix this
        chunksize = 1
        difference = self.file.seek(0, 2) % chunksize
        if (difference != 0) or (self.file.seek(0,2) == 0):
            padding = chunksize - difference
            for x in range(padding*2):
                self.file.write(" ")
        # for testing only, default must be\
        # something like 8192\
        # or fs page size multiplied various times

        nwritchnks = (len(content) // chunksize) + 1
        ttalcnks = nwritchnks
        self.file.seek(place)
        while True:
            temp1 = self.file.read(chunksize)
            temp2 = self.file.read(chunksize)
            if nwritchnks > 0:
                self.offset_seek(-(chunksize*2))
                # writes part of content, in chunk size
                self.file.write(content[ttalcnks - nwritchnks * chunksize:(ttalcnks - nwritchnks + 1) * chunksize])
                nwritchnks -= 1
                while len(temp1) > 0:
                    self.file.write(temp1)
                    temp1 = self.file.read(chunksize)
                    self.offset_seek(-chunksize)
                    self.file.write(temp2)
                    temp2 = self.file.read(chunksize)
                    self.offset_seek(-chunksize)

            else:
                break

    def overwrite_at(self, place: int, content: str):
        self.file.seek(place)
        self.file.write(content)

    def errase_at(self, place: int, quantity: int):
        pass


ala = FileHandler("./lel.txt")
ala.write_at(0,"a")
