from segment import Segment, SegmentType

def calculate_segments_plow(segments: list[Segment], first_segment: Segment, last_segment: Segment):
    """
    Calculates BFO value given all plow segments.
    """

    plow_type = SegmentType.PLOW
    bfo = 0
    # Calculate all P segment
    for segment in segments:
        bfo += segment.length

    if first_segment.type == plow_type and last_segment.type == plow_type:
        bfo += 22
    elif first_segment.type == plow_type and last_segment.type != plow_type:
        bfo += 11
    elif first_segment.type != plow_type and last_segment.type == plow_type:
        bfo += 11

    return bfo

def calculate_segments_bore(segments: list[Segment], first_segment: Segment, last_segment: Segment):
    bore_type = SegmentType.BORE
    segment_sum = 0
    bm61d = 0
    bfov = 0
    bfoi = 0

    for segment in segments:
        segment_sum += segment.length

    if first_segment.type == bore_type and last_segment.type == bore_type:
        bm61d = segment_sum
        bfov = bm61d + 6
        bfoi = bm61d + 22

    elif first_segment.type == bore_type and last_segment.type != bore_type:
        bm61d = segment_sum
        bfov = bm61d + 3
        bfoi = bm61d + 11

    elif first_segment.type != bore_type and last_segment.type == bore_type:
        bm61d = segment_sum
        bfov = bm61d + 3
        bfoi = bm61d + 11
    else:
        bm61d = segment_sum
        bfov = segment_sum
        bfoi = segment_sum

    return (bm61d, bfov, bfoi)