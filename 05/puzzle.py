import re
from typing import List, Tuple, Dict
point = Tuple[int, int]

def line_coords(line: Tuple[point, point], diagonal: bool) -> List[point]:
    if not diagonal and line[0][0] != line[1][0] and line[0][1] != line[1][1]:
        return []
    increase = (int(line[0][0] < line[1][0]) or -1, int(line[0][1] < line[1][1]) or -1)
    x = range(line[0][0], line[1][0] + increase[0], increase[0])
    y = range(line[0][1], line[1][1] + increase[1], increase[1])
    x = [line[0][0]] * len(y) if len(x) == 1 else x
    y = [line[0][1]] * len(x) if len(y) == 1 else y
    return zip(x, y)

def puzzle(lines: List[Tuple[int, int, int, int]], diagonal: bool = False) -> int:
    vents: Dict[point, int] = dict()
    for line in lines:
        coords = line_coords((line[:2],line[2:]), diagonal)
        for coord in coords:
            vents[coord] = 1 if coord not in vents else vents[coord] + 1
    return len(list(filter(lambda x: x >= 2, vents.values())))

if __name__ == "__main__":
    with open('input.txt') as f:
        parse = lambda x: [int(i) for i in re.split(' |,', x.strip()) if i.isnumeric()]
        contents = list(map(parse, f.readlines()))
    print(f"{puzzle(contents)}, {puzzle(contents, True)}")
