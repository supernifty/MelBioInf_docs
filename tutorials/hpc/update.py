#!/usr/bin/env python

import sys

def main(vs):
  variables = {}
  for line in open(vs, 'r'):
    k, v = line.strip('\n').split('=')
    variables[k] = v

  for line in sys.stdin:
    for var in variables:
      search = '\\env{%s}' % var
      if search in line:
        line = line.replace(search, variables[var])
    sys.stdout.write(line)

if __name__ == '__main__':
  main(sys.argv[1])
