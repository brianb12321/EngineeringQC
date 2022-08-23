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
        
        totals["P"] = calc.calculate_segments_plow(segments[SegmentType.PLOW], first_segment, last_segment)
        totals["B"] = calc.calculate_segments_bore(segments[SegmentType.BORE], first_segment, last_segment)
        print(f"BFO = {totals['P']}")
        print(f"BFOI = {totals['B'].bfoi}")
        print(f"BFOV = {totals['B'].bfov}")
        print(f"BM61D = {totals['B'].bm61d}")

        print("Press ENTER when ready.")
        input()