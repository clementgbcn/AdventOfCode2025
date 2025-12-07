from functools import lru_cache

from day_factory.day import Day
from day_factory.day_utils import TestEnum
from utils.input_parser import InputParser


class Day07(Day):
    FIRST_STAR_TEST_RESULT = 21
    SECOND_STAR_TEST_RESULT = 40

    grid = None

    def __init__(self):
        super().__init__(self)

    @staticmethod
    def solve(input_value: InputParser) -> int:
        grid = input_value.get_table()
        beams = set()
        idx = 0
        while grid[0][idx] != "S":
            idx += 1
        beams.add((0, idx))
        total = 0
        while len(beams) > 0:
            new_beams = set()
            for b in beams:
                x, y = b
                if x + 1 >= len(grid):
                    continue
                if grid[x + 1][y] == "^":
                    total += 1
                    new_beams.add((x + 1, y - 1))
                    new_beams.add((x + 1, y + 1))
                else:
                    new_beams.add((x + 1, y))
            beams = new_beams
        return total

    @staticmethod
    def solve_2_dfs(input_value: InputParser, input_type: TestEnum) -> int:
        grid = input_value.get_table()
        idx = 0
        while grid[0][idx] != "S":
            idx += 1
        beams = [(0, idx)]
        save = {}
        while len(beams) > 0:
            x, y = beams.pop()
            if (x, y) in save:
                continue
            if x + 1 >= len(grid):
                save[(x, y)] = 1
                continue
            if grid[x + 1][y] == "^":
                if (x + 1, y - 1) in save and (x + 1, y + 1) in save:
                    save[(x, y)] = save[(x + 1, y - 1)] + save[(x + 1, y + 1)]
                    continue
                beams.append((x, y))
                beams.append((x + 1, y - 1))
                beams.append((x + 1, y + 1))
            elif (x + 1, y) in save:
                save[(x, y)] = save[(x + 1, y)]
            else:
                beams.append((x, y))
                beams.append((x + 1, y))
        return save[(0, idx)]

    @staticmethod
    def solve_2(input_value: InputParser, input_type: TestEnum) -> int:
        grid = input_value.get_table()
        idx = 0
        while grid[0][idx] != "S":
            idx += 1
        Day07.grid = grid
        return Day07.compute_path(input_type, (0, idx))

    @staticmethod
    @lru_cache(maxsize=None)
    def compute_path(input_type: TestEnum, position) -> int:
        x, y = position
        if x + 1 >= len(Day07.grid):
            return 1
        if Day07.grid[x + 1][y] == "^":
            return Day07.compute_path(input_type, (x + 1, y - 1)) + Day07.compute_path(
                input_type, (x + 1, y + 1)
            )
        else:
            return Day07.compute_path(input_type, (x + 1, y))

    def solution_first_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.solve(input_value)

    def solution_second_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.solve_2(input_value, input_type)
