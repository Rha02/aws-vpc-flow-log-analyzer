import sys

from iana_protocols.iana_protocols import IanaProtocols
from tag_table.csv_tag_table import CsvTagTable
from tag_table.repository import TagTableRepository

def main(flowLogsFilepath: str, tagTable: TagTableRepository, outputPath: str):
    tagCounter: dict[str, int] = {}
    portProtocolCounter: dict[tuple[int, str], int] = {}

    # Read flow logs and update counters
    with open(flowLogsFilepath, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            # Split line by space and check if it is of valid format (version 2 flow log)
            lineComponents = line.split(" ")
            if len(lineComponents) != 14:
                print("Error - not a default log format: \n" + line)
                continue

            # Extract the destination port and protocol nbr
            try:
                dstPort = int(lineComponents[6])
                protocolNbr = int(lineComponents[7])
                protocolName = IanaProtocols.getProtName(protocolNbr)
            except:
                print(f"Invalid line: {line}")
                continue

            tag = tagTable.lookUpTag(dstPort, protocolName)

            tagCounter[tag] = tagCounter.get(tag, 0) + 1

            portProtocolKey = (dstPort, protocolName)
            portProtocolCounter[portProtocolKey] = portProtocolCounter.get(portProtocolKey, 0) + 1

    # Write counter results to the output file
    with open(outputPath, "w") as out:
        # Print Tag Counts
        out.write("Tag Counts:\nTag, Count\n")
        for tag, count in tagCounter.items():
            out.write(f"{tag}, {count}\n")
        
        # Print Port/Protocol Counts
        out.write("\nPort/Protocol Combination Counts:\nPort, Protocol, Count\n")
        for (dstPort, protocol), count in portProtocolCounter.items():
            out.write(f"{dstPort}, {protocol}, {count}\n")


if __name__ == "__main__":
    """Usage: py main.py <flow_logs.txt> <tag_table.csv>"""
    
    args = sys.argv[1:]

    # Check that the correct number of arguments is entered
    if len(args) != 2:
        print("Invalid number of arguments")
        sys.exit(1)
    
    # Create filepath strings for the flow logs and tag lookup files
    dataDir = "data/"
    flowLogsTxt = dataDir + args[0]
    tagTableCsv = dataDir + args[1]

    # Create a Tag Table
    tagTable = CsvTagTable(tagTableCsv)

    # Path of output file
    outputPath = "output.txt"

    main(flowLogsTxt, tagTable, outputPath)
    

