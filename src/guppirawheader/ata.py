from keyvalueproperty_rao_lists.ata import PROPERTIES
from guppirawheader import GuppiRawHeader, BufferedReader
from keyvaluestore import KeyValueStore

class GuppiRawHeaderATA(GuppiRawHeader):
    @staticmethod
    def file_read_header(f: BufferedReader):
        return GuppiRawHeader.file_read_header(f, GuppiRawHeaderATA)

KeyValueStore.add_properties(
    GuppiRawHeaderATA,
    PROPERTIES
)
