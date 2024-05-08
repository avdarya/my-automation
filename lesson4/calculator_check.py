import pytest
from calculator import Calculator

# @pytest.mark.skip(reason='reasom')
# @pytest.mark.xfail(strict=True)
# @pytest.mark.custom_positive
@pytest.mark.parametrize('num1, num2, result', [
  (4, 5, 9),
  (-6, -10, -16),
  (-6, 6, 0),
  (5.3, 4.6, 9.9),
  (0, 4, 4),
])
def check_sum_nums(num1, num2, result):
  calculator = Calculator()
  res = calculator.sum(num1, num2)
  if isinstance(num1, float) or isinstance(num2, float):
    numDigits = len(str(result).split('.')[1])
    roundedRes = round(res, numDigits)
    assert roundedRes == result
  else:
    assert res == result


def check_div_positive():
  calculator = Calculator()
  res = calculator.div(10, 2)
  assert res == 5

def check_div_by_zero():
  calculator = Calculator()
  with pytest.raises(ArithmeticError):
    calculator.div(10, 0)

@pytest.mark.parametrize('nums, result',[
  ([], 0),
  ([1, 2, 3, 4, 5], 3)
])
def check_avg_list(nums, result):
  calculator = Calculator()
  res = calculator.avg(nums)
  assert res == result