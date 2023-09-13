from keyvalueproperty_rao_lists.ata import PROPERTIES
from guppirawheader import GuppiRawHeader
from keyvaluestore import KeyValueStore

class GuppiRawHeaderATA(GuppiRawHeader):
    pass

KeyValueStore.add_properties(
    GuppiRawHeaderATA,
    PROPERTIES
)
