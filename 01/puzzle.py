from typing import List

def sonar_sweep(depths: List[int], frame_size: int) -> int:
    return sum(
        [
            sum(depths[i:i + frame_size]) < sum(depths[i + 1:i + 1 + frame_size])
            for i in range(len(depths) - frame_size)
        ]   
    )

def sonar_sweep_02(depths: List[int], frame_size: int) -> int:
    total = 0
    current = [0,sum(depths[0:frame_size])]
    for i in range(1, len(depths) - frame_size + 1):
        current[0], current[1] = current[1], sum(depths[i:i + frame_size])
        total += 1 if current[0] < current[1] else 0
    return total

if __name__ == "__main__":
    with open('input.txt') as f:
        contents = list(map(lambda x : int(x.strip()), f.readlines()))
    print(f"{sonar_sweep(contents, 1)}, {sonar_sweep(contents, 3)}")
    print(f"{sonar_sweep_02(contents, 1)}, {sonar_sweep_02(contents, 3)}")
