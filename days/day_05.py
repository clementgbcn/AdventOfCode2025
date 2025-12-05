import bisect
from typing import List, Tuple


from day_factory.day import Day
from day_factory.day_utils import TestEnum
from utils.input_parser import InputParser


class Day05(Day):

    FIRST_STAR_TEST_RESULT = 3
    SECOND_STAR_TEST_RESULT = 14

    def __init__(self):
        super().__init__(self)

    @staticmethod
    def solve(input_value: InputParser) -> int:
        ranges: List[Tuple[int, int]] = []
        iterator = input_value.get_iterator()
        for line in iterator:
            if line == "":
                break
            a, b = list(map(lambda x: int(x), line.split('-')))
            ranges.append((a, b))
        total = 0
        for ingredient in iterator:
            for r in ranges:
                if r[0] <= int(ingredient) <= r[1]:
                    total += 1
                    break
        return total

    @staticmethod
    def solve_2(input_value: InputParser) -> int:
        start: List[int] = []
        end: List[int] = []
        iterator = input_value.get_iterator()
        for line in iterator:
            if line == "":
                break
            a, b = list(map(lambda x: int(x), line.split('-')))
            i = bisect.bisect_left(start, a)
            j = bisect.bisect_left(end, b)
            if len(start) == i:
                # It means it is the last one
                start.append(a)
                end.append(b)
            elif i == 0:
                if len(end) == j:
                    # It means it is the last one
                    start = [a]
                    end = [b]
                elif b < start[j]:
                    start = [a] + start[j:]
                    end = [b] + end[j:]
                else:
                    start = [a] + start[j+1:]
                    end = end[j:]
            elif a <= end[i-1]:
                if len(end) == j:
                    # It means it is the last one
                    end[i-1] = b
                    start = start[:i]
                    end = end[:i]
                elif b < start[j]:
                    end[i-1] = b
                    start = start[:i] + start[j:]
                    end = end[:i] + end[j:]
                else:
                    end[i-1] = end[j]
                    start = start[:i] + start[j+1:]
                    end = end[:i] + end[j+1:]
            else:
                if len(end) == j:
                    # It means it is the last one
                    end[i] = b
                    start[i] = a
                    start = start[: i + 1]
                    end = end[: i + 1]
                elif b < start[j]:
                    start = start[:i] + [a] + start[j:]
                    end = end[:i] + [b] + end[j:]
                else:
                    start[i] = a
                    end[i] = end[j]
                    start = start[:i+1] + start[j+1:]
                    end = end[:i+1] + end[j+1:]
        total = 0
        for i in range(len(start)):
            total += end[i] - start[i] + 1
        return total

    def solution_first_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.solve(input_value)

    def solution_second_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.solve_2(input_value)
