"""
on this file, all elements necessary to deal with .VSSM archives are handled
"""


class FileHandler:

    def __init__(self, archive: str):
        self.path = archive
        self.file = open(archive, "w+")
        self.filesize = self.file.seek(0, 2)

    def offset_seek(self, offset: int):
        self.file.seek(self.file.tell() + offset)

    def read_at(self, place: int, size: int):
        self.file.seek(place)
        return self.file.read(size)

    def write_at(self, place: int, content: str):
        # TODO fix for writes larger than DefaultRewriteChunkSize
        # for testing only, default must be\
        # something like 8192\
        # or fs page size multiplied various times
        chunksize = 1

        max = self.file.seek(0, 2)
        total_swaps = (max - place + 1) // chunksize

        nwritchnks = (len(content) + 1 // chunksize)
        ttalcnks = nwritchnks
        self.file.seek(place)
        swaps = 0

        temp1 = self.file.read(chunksize)
        temp2 = self.file.read(chunksize)
        self.offset_seek(-chunksize)
        while swaps <= total_swaps :
            self.file.write(temp1)
            temp1 = self.file.read(chunksize)
            self.offset_seek(-chunksize)
            self.file.write(temp2)
            temp2 = self.file.read(chunksize)
            swaps += 1


    def overwrite_at(self, place: int, content: str):
        self.file.seek(place)
        self.file.write(content)

    def errase_at(self, place: int, quantity: int):
        pass


class ArchiveHandler(FileHandler):

    def __init__(self, archive):
        super().__init__(archive)
        self.reflist = {}
        self.find_cache()

    def find_cache(self):
        # TODO finds cache on archive and loads all references to memory for quick file manipulation
        pass

    def build_reference_cache(self):
        # TODO in case no cache is present on archive
        pass

    def update_offsetted_references(self, start, offset):
        for x in self.reflist.keys():
            if self.reflist[x][0] > start:
                self.reflist[x][0] = self.reflist[x][0] + offset
                self.reflist[x][1] = self.reflist[x][1] + offset

    def add_reference(self, iden, place: list):
        self.reflist += {iden: place}

    def remove_reference(self, iden):
        self.reflist.pop(iden)

    def edit_reference(self, iden, start=None, end=None):
        if start is not None:
            self.reflist[iden][0] = start

        if end is not None:
            self.reflist[iden][1] = end

    def rename_reference(self, iden, newiden):
        self.reflist[newiden] = self.reflist.pop(iden)

    def write_at(self, place: int, content: str):
        super().write_at(place, content)
        self.update_offsetted_references(place, len(content))

    def overwrite_at(self, place, content):
        super().overwrite_at(place, content)
        self.update_offsetted_references(place, len(content))

    def errase_at(self, place, quantity):
        super().errase_at(place, quantity)
        self.update_offsetted_references(place, -quantity)

    def load_file(self, refs: list):
        return self.read_at(refs[0], refs[0] - refs[1])

    def save_file(self, refs, newfile: str):
        newlength = len(newfile)
        oldlength = refs[1] - refs[0]

        if newlength <= oldlength:
            self.overwrite_at(refs[0], newfile)
            diff = oldlength - len(newfile)
            self.errase_at(refs[0] + newlength + 1, diff)  # truncates file

        if newlength > oldlength:
            self.overwrite_at(refs[0], newfile[:oldlength])
            self.write_at(oldlength, newfile[oldlength:])

        self.update_offsetted_references(refs[0], newlength - oldlength)

    def new_file(self, iden):
        lastref = 0
        for x in self.reflist.keys():
            if lastref < self.reflist[x][1]:
                lastref = self.reflist[x][1]
        self.add_reference(iden, [lastref + 1, lastref + 1])
