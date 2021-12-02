from util import readints

if __name__ == '__main__':
  def main():
    increases = 0
    last = None
    for depth in readints('01.input.txt'):
      if last is not None and depth > last:
        increases += 1
      last = depth

    return increases


  print(main())
