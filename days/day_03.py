from functools import lru_cache

from day_factory.day import Day
from day_factory.day_utils import TestEnum
from utils.input_parser import InputParser


class Day03(Day):

    FIRST_STAR_TEST_RESULT = 357
    SECOND_STAR_TEST_RESULT = 3121910778619

    def __init__(self):
        super().__init__(self)

    @staticmethod
    def solve(input_value: InputParser) -> int:
        total = 0
        for joltage in input_value.get_iterator():
            m1, m2 = int(joltage[0]), None
            for i in range(1,len(joltage)-1):
                if int(joltage[i]) > m1:
                    m1 = int(joltage[i])
                    m2 = None
                elif m2 is None or int(joltage[i]) > m2:
                    m2 = int(joltage[i])
            if m2 is None or int(joltage[-1]) > m2:
                m2 = int(joltage[-1])
            total += m1 * 10 + m2
        return total

    @staticmethod
    def solve_2(input_value: InputParser) -> int:
        total = 0
        for joltage in input_value.get_iterator():
            total += Day03.get_biggest(joltage, 12)
        return total

    @staticmethod
    @lru_cache(maxsize=None)
    def get_biggest(v: str, s: int) -> int | None:
        if s == 0:
            return 0
        if len(v) < s:
            return None
        if len(v) == s:
            return int(v)
        left, right = Day03.get_biggest(v[1:], s-1), Day03.get_biggest(v[1:], s)
        if left is None and right is None:
            return None
        left = int(v[0])*(10**(s-1)) + left
        return max(left, right if right is not None else left)

    def solution_first_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.solve(input_value)

    def solution_second_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.solve_2(input_value)
