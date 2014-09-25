import py.test
import sys
#sys.path.append('/Users/nicolai/P/testungit/')
#sys.path.append('..')

from Calc import plus

def test_plus():
  result = plus(3,4)

  assert result == 7
