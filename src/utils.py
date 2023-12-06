"""Utility classes and methods."""

from io import TextIOWrapper
from typing import Generator
from copy import deepcopy


class FileReader:
    """Class for reading files."""

    def __init__(self, file: TextIOWrapper) -> None:
        """Construct a new file reader.
        
        Args:
            file (TextIOWrapper): The file to read.
        """
        self.file: TextIOWrapper = file
        self.lines: list = self.file.readlines()
        self.file.seek(0)

    def read_file_until(self, target: int) -> str:
        """Read the file until a certain line.
        
        Args:
            target (int): Number of the line to be read to.

        Returns:
            str: String with the content of the file up until ``target``.
        """
        if target > len(self.lines):
            return self.file.read()

        output: str = ""

        for line_num in range(0, target + 1):
            output += self.lines[line_num]

        return output


# Calculates all possible combinations of values in the input list.
def get_combinations(input_list: list[int]) -> Generator[list[int], None, None]:
    """Calculate all possible combinations of values of a given list.
    
    Args:
        input_list (list[int]): List with values for which combinations should be computed.

    Returns:
        Generator[list[int], None, None]: A generator for all value combinations.
    """
    masks: list[int] = [1 << i for i in range(len(input_list))]
    for i in range(1 << len(input_list)):
        yield [ss for mask, ss in zip(masks, input_list) if i & mask]


def convert_to_int(input_list: list[str]) -> list[int]:
    """Convert a list of binary numbers to a list of decimal numbers.
    
    Args:
        input_list (list[str]): List with numbers in binary representation.

    Returns:
        list[int]: List with decimal representations of the values in ``input_list``.
    """
    copy: list[int] = deepcopy(input_list)
    for i in range(0, len(input_list)):
        copy[i] = int(input_list[i], 2)

    return copy
