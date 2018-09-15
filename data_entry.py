class DataEntry:
    """Thic class represents a single air craft and his data. It separates the key icao from the rest of data to
    use it as a unique key in the dictionary of air crafts"""
    def __init__(self, data_entry_dict):
        self.data_entry_dict = data_entry_dict
        self.icao = data_entry_dict["icao"]
        self.values = self.remove_key(data_entry_dict, "icao")

    def remove_key(self, d, key):
        r = dict(d)
        del r[key]
        return r

    def get_data_entry_dict(self):
        return self.data_entry_dict