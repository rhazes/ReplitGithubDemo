import sys, os

MODULE = "src/"

sys.path.insert(0,MODULE)

import demo

if __name__ == '__main__':
  print(f" the imported var ::{demo.foo}")