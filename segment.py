from enum import Enum

class SegmentType(Enum):
    PLOW = "P"
    BORE = "B"

def create_segment_from_input(text):
    """
    Creates a new segment object using the provided text in the following format: \w{1}\d+
    """
    
    return Segment(SegmentType(text[0].upper()), int(text[1:]))

class Segment:
    type: SegmentType
    length: int

    def __init__(self, type: SegmentType, length: int) -> None:
        self.type = type
        self.length = length