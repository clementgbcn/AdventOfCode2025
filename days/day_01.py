from day_factory.day import Day
from day_factory.day_utils import TestEnum
from utils.input_parser import InputParser


class Day01(Day):
    FIRST_STAR_TEST_RESULT = 3
    SECOND_STAR_TEST_RESULT = 6

    def __init__(self):
        super().__init__(self)

    @staticmethod
    def password(input_value: InputParser) -> int:
        dial = 50
        pwd = 0
        for rotation in input_value.get_iterator():
            dial = (dial + (1 if rotation[0] == "R" else -1) * int(rotation[1:])) % 100
            if dial == 0:
                pwd += 1
        return pwd

    @staticmethod
    def password_2(input_value: InputParser) -> int:
        dial = 50
        pwd = 0
        for rotation in input_value.get_iterator():
            r = int(rotation[1:])
            pwd += r // 100
            r = r % 100
            if r == 0:
                continue
            prev_dial = dial
            dial += (1 if rotation[0] == "R" else -1) * r
            if dial >= 100:
                dial -= 100
                pwd += 1
            elif dial < 0:
                dial += 100
                pwd += 1 if prev_dial != 0 else 0
            elif dial == 0:
                pwd += 1
        return pwd

    def solution_first_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.password(input_value)

    def solution_second_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.password_2(input_value)
