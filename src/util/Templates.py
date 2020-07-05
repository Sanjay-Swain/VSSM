class MetadataAble:

    def __init__(self,name,**metadata):
        self.name = name
        self.metadata = metadata

    def edit_metadata(self, key, value):
        self.metadata[key] = value

    def add_metadata_key(self, key):
        for x in self.metadata.keys():
            self.metadata[x] += {key: None}

    def remove_metadata_key(self, key):
        for x in self.metadata.keys():
            del self.metadata[x][key]


class BatchProduct(MetadataAble):

    def __init__(self, name, bathcids, **metadata):
        super().__init__(name, **metadata)
        self.batches = bathcids


    def add_batch(self, btchid, **metadata):
        self.batches.append()
        self.metadata += metadata

class StockProduct(MetadataAble):
    pass


class Client(MetadataAble):
    pass