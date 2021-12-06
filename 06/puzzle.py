from typing import List
from collections import Counter

def puzzle(fish: List[int], days: int) -> int:
    ages = Counter(fish)
    ages = [ages[i,] for i in range(9)]
    for _ in range(days):
        ages = ages[1:7] + [ages[0] + ages[7], ages[8], ages[0]]
    return sum(ages)

if __name__ == "__main__":
    with open('input.txt') as f:
        contents = [int(i) for i in f.readline().strip().split(',')]
    print(f"{puzzle(contents, 80)}, {puzzle(contents, 256)}")
