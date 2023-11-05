from io import TextIOWrapper
from typing import Generator


class FileReader:

    def __init__(self, file: TextIOWrapper) -> None:
        self.file: TextIOWrapper = file
        self.lines: list = self.file.readlines()
        self.file.seek(0)

    def read_file_until(self, target: int) -> str:

        if target > len(self.lines):
            return self.file.read()

        output: str = ""

        for line_num in range(0, target + 1):
            output += self.lines[line_num]

        return output


# Calculates all possible combinations of values in the input list.
def get_combinations(input_list: list) -> Generator:
    masks: list = [1 << i for i in range(len(input_list))]
    for i in range(1 << len(input_list)):
        yield [ss for mask, ss in zip(masks, input_list) if i & mask]


def all_equal(list: list, indices: list) -> bool:
    to_compare = list[indices[0]]

    for i in indices:
        if list[i] != to_compare:
            return False

    return True


def convert_to_int(list: list) -> list:
    for i in range(0, len(list)):
        list[i] = int(list[i], 2)

    return list
