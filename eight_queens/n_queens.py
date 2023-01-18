import argparse
from itertools import permutations

def parse_arguments(args):
    n = args.n
    if n is None:
        print("Please, provide the number of queens using --n argument.")
        raise SystemExit(1)
    if(n <= 4):
        print("N should be an int greater then 4.")
        raise SystemExit(1)
    return n

def calculate_solutions(n: int):
    solutions = []
    cols = range(n)
    for pemutation in permutations(cols):
        diag_right = set(pemutation[i]+i for i in cols)
        diag_left = set(pemutation[i]-i for i in cols)
        if (n == len(diag_right)) and (n == len(diag_left)):
            solutions.append(pemutation)
    return solutions

if __name__ == "__main__":
    parser = argparse.ArgumentParser()  
    parser.add_argument("--n", type=int, help='Number of queens and board (nxn)')
    args = parser.parse_args()
    n = parse_arguments(args)
    solutions = calculate_solutions(n)
    print(f'Found {len(solutions)} solutions.')
    while True:
        try:
            num = int(input(f'Enter the solution number (0-{len(solutions)-1}) or other key to quit: '))
            print(solutions[num])
        except:
            break