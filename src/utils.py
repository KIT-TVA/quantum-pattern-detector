from io import TextIOWrapper
from typing import Generator
from copy import deepcopy


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


def convert_to_int(list: list) -> list:
    copy = deepcopy(list)
    for i in range(0, len(list)):
        copy[i] = int(list[i], 2)

    return copy
