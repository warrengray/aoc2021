def readlines(filename):
  with open(filename) as f:
    return f.readlines()


def readints(filename):
  return [int(l) for l in readlines(filename)]
