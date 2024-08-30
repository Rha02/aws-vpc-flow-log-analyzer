
# Mapping of IANA protocol numbers to their respective names
import socket

class IanaProtocols:
    """Class for handling IANA protocol names and numbers"""

    _protNbrToName = {
        1: 'icmp',
        6: 'tcp',
        17: 'udp'
    }
    
    @classmethod
    def getProtName(cls, protNbr: int) -> str:
        """Get protocol name given its IANA number"""
        return cls._protNbrToName.get(protNbr, "unknown")
    
    @classmethod
    def hasProtName(cls, protName: str) -> bool:
        """Check if a protocol name is present in the class map"""
        return protName in cls._protNbrToName.values()
    
    @classmethod
    def tryAddingProt(cls, protName: str) -> bool:
        """Try adding a protocol to the IANA map by using python's socket module to identify the protocol number"""
        try:
            protocolNbr = socket.getprotobyname(protName)
            print(f"Adding {protName} to IANA protocol map for number {protocolNbr}")
            cls._protNbrToName[protocolNbr] = protName
        except:
            print(f"Unknown protocol: {protName}")