import bisect

from day_factory.day import Day
from day_factory.day_utils import TestEnum
from utils.input_parser import InputParser


class Day02(Day):
    FIRST_STAR_TEST_RESULT = 1227775554
    SECOND_STAR_TEST_RESULT = 4174379265

    def __init__(self):
        super().__init__(self)

    @staticmethod
    def solve(input_value: InputParser) -> int:
        ranges = next(input_value.get_iterator()).split(",")
        total = 0
        for r in ranges:
            start, end = r.split("-")
            if len(start) % 2 == 1:
                a = 10 ** (len(start) // 2)
            else:
                a = int(start[0 : len(start) // 2])
            if len(end) % 2 == 1:
                b = 10 ** (len(end) // 2) - 1
            else:
                b = int(end[0 : len(end) // 2])
            for v in range(a, b + 1):
                invalid_id = int(str(v) * 2)
                if int(start) <= invalid_id <= int(end):
                    total += invalid_id
        return total

    @staticmethod
    def solve_2(input_value: InputParser) -> int:
        ranges = next(input_value.get_iterator()).split(",")
        invalid_ids = set()
        start = sorted([int(r.split("-")[0]) for r in ranges])
        end = sorted([int(r.split("-")[1]) for r in ranges])
        i = 1
        while int(str(i) * 2) <= end[-1] + 1:
            repeat = 2
            while int(str(i) * repeat) <= end[-1] + 1:
                invalid_id = int(str(i) * repeat)
                idx = bisect.bisect_left(end, invalid_id)
                if start[idx] <= invalid_id <= end[idx]:
                    invalid_ids.add(invalid_id)
                repeat += 1
            i += 1
        return sum(invalid_ids)

    def solution_first_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.solve(input_value)

    def solution_second_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.solve_2(input_value)
