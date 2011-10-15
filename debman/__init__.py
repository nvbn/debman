from functools import partial
from debman import Debman, DebmanPlugins
import sys

def main():
    func = partial(Debman, DebmanPlugins())
    for arg in filter(lambda arg: arg.find('-') == 0, sys.argv[1:]):
        func = partial(func, arg[1:])
    try:
        func()(filter(lambda arg: arg.find('-') != 0, sys.argv[1:]))
    except KeyError:
        sys.stdout.write('\nNo such command!\n')
