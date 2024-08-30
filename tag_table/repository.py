from abc import ABC, abstractmethod

class TagTableRepository(ABC):
    """Interface for the tag table"""

    @abstractmethod
    def lookUpTag(self, dstPort: int, protocol: str) -> str:
        """Look up the tag given a combination of destination port and protocol name"""
        pass