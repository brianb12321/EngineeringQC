import os
from collections import defaultdict
from segment import SegmentType, create_segment_from_input
import segment_calculations as calc

if __name__ == "__main__":
    os.system("cls")
    print("Welcome to engineering units QC")

    while True:
        segments = defaultdict(list)
        first_segment = None
        totals = {}

        while True:
            print("> ", end="")
            input_text = input()

            if not input_text:
                break

            new_segment = create_segment_from_input(input_text)
            segments[new_segment.type].append(new_segment)

            if first_segment is None:
                first_segment = new_segment

            last_segment = new_segment
        
        totals[SegmentType.PLOW] = calc.calculate_segments_plow(segments[SegmentType.PLOW], first_segment, last_segment)
        totals[SegmentType.BORE] = calc.calculate_segments_bore(segments[SegmentType.BORE], first_segment, last_segment)
        print(f"BFO = {totals[SegmentType.PLOW]}")
        print(f"BFOI = {totals[SegmentType.BORE].bfoi}")
        print(f"BFOV = {totals[SegmentType.BORE].bfov}")
        print(f"BM61D = {totals[SegmentType.BORE].bm61d}")

        print("Press ENTER when ready.")
        input()