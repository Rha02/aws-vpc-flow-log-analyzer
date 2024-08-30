import csv
import socket

from iana_protocols.iana_protocols import IanaProtocols

from .repository import TagTableRepository

class CsvTagTable(TagTableRepository):
    """Implementation of the Tag Table using a CSV file"""

    def __init__(self, csvFilePath: str):
        # key: (dstPort, protocolName), value: tag
        self.tagMap: dict[tuple[int, str], str] = {}

        with open(csvFilePath, "r") as f:
            reader = csv.reader(f)

            # Skip header - Assuming it's (dstPort, protocolName, tag)
            next(reader)

            for row in reader:                
                if len(row) != 3:
                    # Skip invalid rows
                    continue

                # Extract destination port, protocol name, and tag
                try:
                    dstPort = int(row[0].strip())
                    protocol = row[1].strip().lower()
                    tag = row[2].strip().lower()
                except:
                    # Skip invalid rows
                    print(f"Invalid row: {row}")
                    continue

                # If protocol is not present in iana_protocols.py map, add it to the map
                if not IanaProtocols.hasProtName(protocol):
                    IanaProtocols.tryAddingProt(protocol)

                key = (dstPort, protocol)
                self.tagMap[key] = tag
    
    def lookUpTag(self, dstPort: int, protocol: str) -> str:
        key = (dstPort, protocol)

        if key in self.tagMap:
            return self.tagMap[key]
        
        return "untagged"