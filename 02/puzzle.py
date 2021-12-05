from typing import List, Tuple

def puzzle(course: List[Tuple[str, str]]) -> int:
    position = {"forward": 0, "up": 0, "down": 0}
    for direction, amount in course:
        position[direction] += amount
    return position["forward"] * (position["down"] - position["up"])

def puzzle_02(course: List[Tuple[str, str]]) -> int:
    position = {"forward": 0, "up": 0, "down": 0, "depth": 0}
    for direction, amount in course:
        position[direction] += amount
        if direction == "forward":
            position["depth"] += (position["down"] - position["up"]) * amount
    return position["forward"] * position["depth"]

if __name__ == "__main__":
    parse = lambda x : [int(i) if i.isnumeric() else i for i in x.strip().split(" ")]
    with open('input.txt') as f:
        contents = list(map(parse, f.readlines()))
    print(f"{puzzle(contents)}, {puzzle_02(contents)}")
