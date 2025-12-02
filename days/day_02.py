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
        ranges = next(input_value.get_iterator()).split(',')
        total = 0
        for r in ranges:
            start, end = r.split('-')
            if len(start) % 2 == 1:
                a = 10 ** (len(start)//2)
            else:
                a = int(start[0:len(start)//2])
            if len(end) % 2 == 1:
                b = 10 ** (len(end)//2) - 1
            else:
                b = int(end[0:len(end)//2])
            for v in range(a, b+1):
                invalid_id = int(str(v)*2)
                if int(start) <= invalid_id <= int(end):
                    total += invalid_id
        return total

    @staticmethod
    def solve_2(input_value: InputParser) -> int:
        ranges = next(input_value.get_iterator()).split(',')
        total = 0
        for r in ranges:
            start, end = r.split('-')
            for candidate in range(int(start), int(end)+1):
                s = str(candidate)
                for size in range(1, len(s)//2+1):
                    if len(s) % size != 0:
                        continue
                    ptr = 0
                    is_valid = False
                    while ptr+2*size <= len(s):
                        if s[ptr:ptr+size] != s[ptr+size:ptr+2*size]:
                            is_valid = True
                            break
                        ptr += size
                    if not is_valid:
                        break
                else:
                    continue
                total += candidate
        return total

    def solution_first_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.solve(input_value)

    def solution_second_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.solve_2(input_value)
