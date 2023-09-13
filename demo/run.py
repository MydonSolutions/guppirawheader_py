import argparse

from guppirawheader.cosmic import GuppiRawHeaderCOSMIC
from guppirawheader.ata import GuppiRawHeaderATA

class_name_map = {
    "COSMIC": GuppiRawHeaderCOSMIC,
    "ATA": GuppiRawHeaderATA,
}

parser = argparse.ArgumentParser(
    description="Demonstrate the GuppiRawHeader class.",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)

parser.add_argument(
    "guppi_raw_filepath",
    type=str,
    help="The filepath to open.",
)

parser.add_argument(
    "-c","--class",
    default="COSMIC",
    choices=list(class_name_map.keys()),
    help="Specify the class to instantiate."
)

args = parser.parse_args()

with open(args.guppi_raw_filepath, "rb") as f:
    header = GuppiRawHeaderCOSMIC.file_read_header(f, GuppiRawHeaderCOSMIC)

print(f"type(header): {type(header)}")
print(f"Header: {header.get()}")

print(f'Header[DAQPULSE]: {header["DAQPULSE"]} (type: {type(header.get("DAQPULSE"))})')
print(f'Header.pulse: {header.pulse} (type: {type(header.pulse)})')
print(f'Header.antenna_names: {header.antenna_names} (type: {type(header.antenna_names)})')
