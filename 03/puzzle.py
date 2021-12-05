from typing import List, Tuple

def most_least_common(diagnostics: List[str]) -> Tuple[str, str]:
    vals = [0] * len(diagnostics[0])
    for diag in diagnostics:
        for i, c in enumerate(diag):
            vals[i] += 1 if c == '1' else -1
    gamma = ''.join(['1' if i >= 0 else '0' for i in vals]) # most common
    epsilon = ''.join(['1' if i == '0' else '0' for i in gamma]) #least common
    return gamma, epsilon

def generator_scrubber(diagnostics: List[str], common: bool = True) -> str:
    current_diag = diagnostics
    for i in range(len(diagnostics[0])):
        if len(current_diag) == 1:
            break
        rare = most_least_common(current_diag)[0 if common else 1]
        current_diag = list(filter(lambda x: x[i] == rare[i], current_diag))
    return ''.join(current_diag)

def puzzle(diagnostics: List[str]) -> int:
    gamma, epsilon = most_least_common(diagnostics)
    return int(gamma, 2) * int(epsilon, 2)

def puzzle_02(diagnostics = List[str]) -> int:
    generator = generator_scrubber(diagnostics)
    scrubber = generator_scrubber(diagnostics, False)
    return int(generator, 2) * int(scrubber, 2)

if __name__ == "__main__":
    with open('input.txt') as f:
        contents = list(map(lambda x : x.strip(), f.readlines()))
    print(f"{puzzle(contents)}, {puzzle_02(contents)}")
