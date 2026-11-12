import sys
# import cowsay
from saying import hello

# if len(sys.argv) == 2:
#   cowsay.cow("hello, " + sys.argv[1])

if len(sys.argv) == 2:
  hello(sys.argv[1])