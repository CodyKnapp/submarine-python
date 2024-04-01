import sys

from submarine import Submarine

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python main.py instruction_file_name")
        sys.exit()

    with open(sys.argv[1]) as fin:
        submarine = Submarine()
        for line in fin:
            submarine.navigate(line)

    print(f"Distance: {submarine.distance}")
    print(f"Depth: {submarine.depth}")
    print(f"Product: {submarine.distance * submarine.depth}")
