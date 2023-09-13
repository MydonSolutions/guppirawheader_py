# GUPPI Raw Headers

Provides the `GuppiRawHeader` class, pertinent to the headers of blocks within GUPPI Raw files, as an implementation of the [KeyValueStore](https://github.com/MydonSolutions/keyvaluestore) abstraction container.
Further implementations apply the [property lists](https://github.com/MydonSolutions/keyvalueproperty_rao_lists) to define higher level values for the instruments behind the GUPPI Raw files.

## Exemplary use of the `GuppiRawHeader` class

```python
from guppirawheader.cosmic import GuppiRawHeaderCOSMIC

with open(guppi_raw_filepath, "rb") as f:
    header = GuppiRawHeaderCOSMIC.file_read_header(f, GuppiRawHeaderCOSMIC)
```
