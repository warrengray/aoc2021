from util import readints

INPUT = """
199
200
208
210
200
207
240
269
260
263
"""

INPUT = [int(i) for i in INPUT.strip().split("\n")]

if __name__ == '__main__':
  def main():
    windows = []
    measurements = readints('01.input.txt')
    for i in range(2, len(measurements)+3, 3):
      for j in reversed(range(3)):
        window = measurements[i-j:i-j+3]
        if len(window) < 3:
          break

        windows.append(sum(window))

    increases = 0
    last = None
    for depth in windows:
      if last is not None and depth > last:
        increases += 1
      last = depth

    return increases


  print(main())
