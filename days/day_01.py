from day_factory.day import Day
from day_factory.day_utils import TestEnum
from utils.input_parser import InputParser


class Day01(Day):
    FIRST_STAR_TEST_RESULT = 3
    SECOND_STAR_TEST_RESULT = 6

    DIR = {"R": 1, "L": -1}

    def __init__(self):
        super().__init__(self)

    @staticmethod
    def password(input_value: InputParser) -> int:
        dial = 50
        pwd = 0
        for r in input_value.get_iterator():
            dial = (dial + Day01.DIR[r[0]] * int(r[1:])) % 100
            if dial == 0:
                pwd += 1
        return pwd

    @staticmethod
    def password_2(input_value: InputParser) -> int:
        dial = 50
        pwd = 0
        for r in input_value.get_iterator():
            v = int(r[1:])
            pwd += v // 100
            v %= 100
            if v == 0:
                continue
            prev_dial = dial
            dial += Day01.DIR[r[0]] * v
            if dial < 0 or dial >= 100 :
                pwd += 1 if prev_dial != 0 else 0
            elif dial == 0:
                pwd += 1
            dial %= 100
        return pwd

    def solution_first_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.password(input_value)

    def solution_second_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.password_2(input_value)
