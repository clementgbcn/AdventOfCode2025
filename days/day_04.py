from typing import List, Tuple

from day_factory.day import Day
from day_factory.day_utils import TestEnum
from utils.input_parser import InputParser


class Day04(Day):

    FIRST_STAR_TEST_RESULT = 13
    SECOND_STAR_TEST_RESULT = 43

    def __init__(self):
        super().__init__(self)

    @staticmethod
    def solve(input_value: InputParser) -> int:
        grid = [list(row) for row in input_value.get_table()]
        removable = Day04.get_accessible(grid)
        return len(removable)

    @staticmethod
    def solve_2(input_value: InputParser) -> int:
        grid = [list(row) for row in input_value.get_table()]
        total = 0
        while removable := Day04.get_accessible(grid):
            total += len(removable)
            for i, j in removable:
                grid[i][j] = "."
        return total

    @staticmethod
    def get_accessible(grid: List[List[str]]) -> List[Tuple[int, int]]:
        removable = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != "@":
                    continue
                count = 0
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if (x == 0 and y == 0) or not (0 <= i + x < len(grid)) or not (0 <= j + y < len(grid[0])) or grid[i + x][j + y] != "@":
                            continue
                        count += 1
                        if count > 3:
                            break
                    if count > 3:
                        break
                if count <= 3:
                    removable.append((i, j))
        return removable

    def solution_first_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.solve(input_value)

    def solution_second_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.solve_2(input_value)
