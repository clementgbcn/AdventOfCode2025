import operator
from functools import reduce


from day_factory.day import Day
from day_factory.day_utils import TestEnum
from utils.input_parser import InputParser
from utils.utils import extract_int


class Day06(Day):
    FIRST_STAR_TEST_RESULT = 4277556
    SECOND_STAR_TEST_RESULT = 3263827

    OP_MAPPING = {"+": operator.add, "*": operator.mul}

    def __init__(self):
        super().__init__(self)

    @staticmethod
    def solve(input_value: InputParser) -> int:
        pb = input_value.get_table()
        ops = []
        results = []
        for o in pb[-1].split(" "):
            if o != "":
                ops.append(Day06.OP_MAPPING[o])
                results.append(1 if o == "*" else 0)
        for line in pb[:-1]:
            for idx, i in enumerate(extract_int(line)):
                results[idx] = ops[idx](results[idx], i)
        return sum(results)

    @staticmethod
    def solve_2(input_value: InputParser) -> int:
        pb = input_value.get_table()
        total = 0
        values = []
        current_ops = None
        for i in range(max(map(lambda x: len(x), pb))):
            if i < len(pb[-1]) and pb[-1][i] != " ":
                if current_ops is not None:
                    total += reduce(current_ops, values)
                current_ops = Day06.OP_MAPPING[pb[-1][i]]
                values = []
            value = ""
            for j in range(len(pb) - 1):
                value += pb[j][i] if i < len(pb[j]) else ""
            if value.strip() != "":
                values.append(int(value))
        total += reduce(current_ops, values)
        return total

    def solution_first_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.solve(input_value)

    def solution_second_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.solve_2(input_value)
