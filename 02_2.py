from util import readlines

EXAMPLE = """
forward 5
down 5
forward 8
up 3
down 8
forward 2
"""

EXAMPLE = EXAMPLE.strip().split("\n")

if __name__ == '__main__':
  def main():
    # moves = EXAMPLE
    moves = readlines('02.input.txt')
    horizontal, depth, aim = 0, 0, 0
    for move in moves:
      command, value = move.split(" ")
      value = int(value)
      if command == 'forward':
        horizontal += value
        depth += (aim * value)
      elif command == 'up':
        aim -= value
      elif command == 'down':
        aim += value

    return horizontal * depth


  print(main())
