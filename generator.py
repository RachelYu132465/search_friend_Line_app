"""
Generate all possible 10-digit numbers starting with "09" followed by eight digits.
Users are prompted for allowed digits at each position.
"""
from __future__ import annotations

import itertools
from pathlib import Path

OUTPUT_FILE = Path("possible_numbers.txt")


def collect_digits(position: int) -> list[str]:
    """Prompt the user for allowed digits at the given position.

    The function keeps asking until a non-empty set of numeric characters is
    supplied. Commas and whitespace are ignored so inputs like "0 1 2" or
    "0,1,2" both work.
    """

    while True:
        raw = input(
            f"輸入第 {position} 位數可能出現的數字 (可用空白或逗號分隔): "
        )
        digits = []
        for char in raw:
            if char.isdigit():
                digits.append(char)
            elif char.isspace() or char == ",":
                continue
            else:
                print("請只輸入數字、空白或逗號。")
                digits = []
                break

        if digits:
            unique_digits = sorted(set(digits))
            return unique_digits

        print("至少需要一個有效數字，請重新輸入。")


def build_numbers(digit_choices: list[list[str]]) -> list[str]:
    """Combine the provided digit choices into full numbers with 09 prefix."""

    combinations = itertools.product(*digit_choices)
    return ["09" + "".join(combo) for combo in combinations]


def write_numbers(numbers: list[str]) -> None:
    """Write the generated numbers to the output file, one per line."""

    OUTPUT_FILE.write_text("\n".join(numbers), encoding="utf-8")
    print(f"已產生 {len(numbers)} 組，並寫入 {OUTPUT_FILE.resolve()}。")


def main() -> None:
    print("所有號碼一律以 09 開頭，請依序輸入後續 8 位數的可能數字。")
    digit_choices = [collect_digits(position) for position in range(1, 9)]

    numbers = build_numbers(digit_choices)
    write_numbers(numbers)


if __name__ == "__main__":
    main()
