"""
on this file, all elements necessary to deal with .CBSM archives are handled
"""


class FileHandler:

    def __init__(self, archive):
        self.file = open(archive, "w+")
        self.DefaultRewriteChunkSize = 1024
        self.filesize = self.file.seek(0, 2)

    def read_at(self, place, size):
        self.file.seek(place)
        return self.file.read(size)

    def write_at(self, place: int, content: str):
        # TODO fix for writes larger than DefaultRewriteChunkSize
        self.file.seek(place)
        temp1 = self.file.read(self.DefaultRewriteChunkSize)
        temp2 = self.file.read(self.DefaultRewriteChunkSize)
        tempreadpos = self.file.tell()

        self.file.seek(place)
        self.file.write(content)
        writepos = self.file.tell()

        while len(temp1) > 0:
            self.file.seek(writepos)
            self.file.write(temp1)
            writepos = self.file.tell()
            self.file.seek(tempreadpos)
            temp1 = self.file.read(self.DefaultRewriteChunkSize)
            tempreadpos = self.file.tell()

            self.file.seek(writepos)
            self.file.write(temp2)
            writepos = self.file.tell()
            self.file.seek(tempreadpos)
            temp2 = self.file.read(self.DefaultRewriteChunkSize)
            tempreadpos = self.file.tell()

    def overwrite_at(self, place, content):
        self.file.seek(place)
        self.file.write(content)

    def errase_at(self, place, quantity):
        writepos = quantity
        self.file.seek(place + quantity)
        temp1 = self.file.read(self.DefaultRewriteChunkSize)
        temp2 = self.file.read(self.DefaultRewriteChunkSize)
        tempreadpos = self.file.tell()

        while len(temp1) > 0:
            self.file.seek(writepos)
            self.file.write(temp1)
            writepos = self.file.tell()
            self.file.seek(tempreadpos)
            temp1 = self.file.read(self.DefaultRewriteChunkSize)
            tempreadpos = self.file.tell()

            self.file.seek(writepos)
            self.file.write(temp2)
            writepos = self.file.tell()
            self.file.seek(tempreadpos)
            temp2 = self.file.read(self.DefaultRewriteChunkSize)
            tempreadpos = self.file.tell()
        self.filesize = self.file.truncate(self.filesize - quantity)


class ArchiveHandler(FileHandler):

    def __init__(self, archive):
        super().__init__(archive)
        self.references = {}
        self.find_cache()

    def find_cache(self):
        # TODO finds cache on archive and loads all references to memory for quick file manipulation
        pass

    def build_cache(self):
        # TODO in case no cache is present on archive
        pass

    def update_offsetted_references(self, start, offset):
        for x in self.references.keys():
            if self.references[x][0] > start:
                self.references[x][0] = self.references[x][0] + offset

    def write_at(self, place: int, content: str):
        super().write_at(place, content)
        self.update_offsetted_references(place, len(content))

    def overwrite_at(self, place, content):
        super().overwrite_at(place, content)
        self.update_offsetted_references(place, len(content))

    def errase_at(self, place, quantity):
        super().errase_at(place, quantity)
        self.update_offsetted_references(place, -quantity)
