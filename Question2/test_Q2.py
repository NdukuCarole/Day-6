import pytest

from Q2 import lword
from Q2 import cat


class TestLength:


 def test_length_of_words(self):
  assert lword(str(cat)) == True
  
  

if __name__ == '__main__':
 pytest.main()
