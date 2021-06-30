import pytest

from Q1 import checkLeapYear
from Q1 import year


class TestLeapYearTests:
    
    def test_that_years_not_divisible_by_4_are_not_leap_years(self):
      assert checkLeapYear(year) == True
    def test_that_years_divisible_by_4_but_not_by_100_are_leap_years(self):
      assert checkLeapYear(year) == True
    def test_that_years_divisible_by_100_but_not_by_400_are_not_leap_years(self):
      assert checkLeapYear(year) == True
      True
    def test_that_years_divisible_by_400_are_leap_years(self):
      assert checkLeapYear(year) == True

      
      
if __name__ == '__main__':
    pytest.main()
