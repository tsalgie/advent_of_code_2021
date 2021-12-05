import re
from typing import List, Tuple

def its_a_bingo(boards: List[str]) -> List[str]:
    bingos = []
    for board in boards:
        l = board.split()
        board_array = [l[i:i + 5] for i in range(0, 25, 5)]
        rotated = list(zip(*board_array))[::-1]
        if ['X','X','X','X','X'] in board_array or ('X','X','X','X','X') in rotated:
            bingos.append(board)
    return bingos

def mark_boards(boards: List[str], draw: str):
    for i, board in enumerate(boards):
        boards[i] = re.sub(rf"\b{draw}\b", "X", board)

def puzzle(boards: List[str], draws: List[str]) -> int:
    for draw in draws:
        mark_boards(boards, draw)
        bingos = its_a_bingo(boards)
        if len(bingos) > 0:
            total = sum([int(i) if i.isnumeric() else 0 for i in bingos[0].split()])
            return int(draw) * total

def puzzle_02(boards: List[str], draws: List[str]) -> int:
    for draw in draws:
        mark_boards(boards, draw)
        bingos = its_a_bingo(boards)
        for bingo in bingos:
            if len(boards) == 1:
                total = sum([int(i) if i.isnumeric() else 0 for i in bingo.split()])
                return int(draw) * total
            boards.remove(bingo)
                
if __name__ == "__main__":
    with open('input.txt') as f:
        contents = list(map(lambda x : x.strip(), f.readlines()))
    draws = contents[0].split(',')
    boards = [' '.join(contents[2+i:8+i][:-1]) for i in range(0, len(contents)-4, 6)]
    print(f"{puzzle(boards[:], draws)}, {puzzle_02(boards[:], draws)}")
