from keyvalueproperty_rao_lists.cosmic import PROPERTIES
from guppirawheader import GuppiRawHeader, BufferedReader
from keyvaluestore import KeyValueStore

class GuppiRawHeaderCOSMIC(GuppiRawHeader):
    @staticmethod
    def file_read_header(f: BufferedReader):
        return GuppiRawHeader.file_read_header(f, GuppiRawHeaderCOSMIC)

KeyValueStore.add_properties(
    GuppiRawHeaderCOSMIC,
    PROPERTIES
)
