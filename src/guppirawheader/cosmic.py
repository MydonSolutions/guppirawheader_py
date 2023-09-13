from keyvalueproperty_rao_lists.cosmic import PROPERTIES
from guppirawheader import GuppiRawHeader
from keyvaluestore import KeyValueStore

class GuppiRawHeaderCOSMIC(GuppiRawHeader):
    pass

KeyValueStore.add_properties(
    GuppiRawHeaderCOSMIC,
    PROPERTIES
)
