from _io import BufferedReader

from keyvaluestore import KeyValueStore

class GuppiRawHeader(KeyValueStore):

    def __init__(self, key_values: dict):
        self.key_values = key_values

    @staticmethod
    def parse_string_for_value(value: str):
        value = value.strip()
        try:
            value = float(value)
            try:
                value = int(value)
            except ValueError:
                pass
        except:
            # must be a str value, drop enclosing single-quotes
            assert value[0] == value[-1] == "'"
            value = value[1:-1].strip()
        return value

    @staticmethod
    def file_read_header(f: BufferedReader, class_obj=None):
        key_values = {}
        header_entry = f.read(80).decode()
        while header_entry:
            if header_entry == "END" + " "*77:
                break

            key_values[
                header_entry[0:8].strip()
            ] = GuppiRawHeader.parse_string_for_value(
                header_entry[9:]
            )
            header_entry = f.read(80).decode()
        if class_obj is None:
            return GuppiRawHeader(key_values)
        else:
            return class_obj(key_values)

    def get(self, keys: list or str = None, fallback = None):
        if keys is None:
            keys = list(self.key_values.keys())

        if isinstance(keys, list):
            return {
                key: self.key_values.get(key, fallback)
                for key in keys
            }
        else:
            return self.key_values.get(keys, fallback)
    
    def __getitem__(self, key):
        return self.key_values[key]
