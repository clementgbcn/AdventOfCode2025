import bisect
import heapq

from day_factory.day import Day
from day_factory.day_utils import TestEnum
from utils.input_parser import InputParser
from utils.utils import extract_int


class Day08(Day):
    FIRST_STAR_TEST_RESULT = 40
    SECOND_STAR_TEST_RESULT = 25272

    grid = None

    def __init__(self):
        super().__init__(self)

    @staticmethod
    def solve(input_value: InputParser, input_type: TestEnum) -> int:
        position = []
        for line in input_value.get_iterator():
            i = extract_int(line)
            position.append((i[0], i[1], i[2]))
        distances = []
        couples = []
        pb_size = 10 if input_type == TestEnum.TEST else 1000
        for idx in range(len(position) - 1):
            i = position[idx]
            for j in position[idx + 1 :]:
                dist = pow(i[0] - j[0], 2) + pow(i[1] - j[1], 2) + pow(i[2] - j[2], 2)
                k = bisect.bisect_right(distances, dist)
                if k >= pb_size:
                    continue
                distances.insert(k, dist)
                couples.insert(k, (i, j))
        circuits = {}
        circuit_count = 0
        nodes = []
        covered = set()
        for couple in couples[:pb_size]:
            a, b = couple
            covered.add(a)
            covered.add(b)
            if a in circuits and b in circuits and circuits[a] == circuits[b]:
                continue
            elif a in circuits and b in circuits and circuits[a] != circuits[b]:
                prev_circuit = circuits[b]
                for n in nodes[prev_circuit]:
                    circuits[n] = circuits[a]
                    nodes[circuits[a]].add(n)
                nodes[prev_circuit] = set()
            elif a not in circuits and b in circuits:
                circuits[a] = circuits[b]
                nodes[circuits[b]].add(a)
            elif a in circuits and b not in circuits:
                circuits[b] = circuits[a]
                nodes[circuits[a]].add(b)
            else:
                circuits[a] = circuit_count
                circuits[b] = circuit_count
                nodes.append({a, b})
                circuit_count += 1
        s = sorted([len(n) for n in nodes], reverse=True)
        return s[0] * s[1] * s[2]

    @staticmethod
    def solve_2(input_value: InputParser) -> int:
        position = []
        for line in input_value.get_iterator():
            i = extract_int(line)
            position.append((i[0], i[1], i[2]))
        couples = []
        for idx in range(len(position) - 1):
            i = position[idx]
            for j in position[idx + 1 :]:
                dist = pow(i[0] - j[0], 2) + pow(i[1] - j[1], 2) + pow(i[2] - j[2], 2)
                heapq.heappush(couples, (dist, (i, j)))
        circuits = {}
        circuit_count = 0
        nodes = []
        covered = set()
        while couples:
            dist, couple = heapq.heappop(couples)
            a, b = couple
            covered.add(a)
            covered.add(b)
            if a in circuits and b in circuits and circuits[a] == circuits[b]:
                pass
            elif a in circuits and b in circuits and circuits[a] != circuits[b]:
                prev_circuit = circuits[b]
                for n in nodes[prev_circuit]:
                    circuits[n] = circuits[a]
                    nodes[circuits[a]].add(n)
                nodes[prev_circuit] = set()
            elif a not in circuits and b in circuits:
                circuits[a] = circuits[b]
                nodes[circuits[b]].add(a)
            elif a in circuits and b not in circuits:
                circuits[b] = circuits[a]
                nodes[circuits[a]].add(b)
            else:
                circuits[a] = circuit_count
                circuits[b] = circuit_count
                nodes.append({a, b})
                circuit_count += 1
            if sorted([len(n) for n in nodes], reverse=True)[0] == len(position):
                return a[0] * b[0]
        return 0

    def solution_first_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.solve(input_value, input_type)

    def solution_second_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.solve_2(input_value)
