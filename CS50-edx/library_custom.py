import sys
import lib_helper

if len(sys.argv) == 2:
    lib_helper.hello(sys.argv[1])
    lib_helper.goodbye(sys.argv[1])