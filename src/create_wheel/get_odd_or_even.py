from typing import List

def get_even(number_list: List[int]) -> List[int]:
  return [n for n in number_list if n % 2 == 0]
  
def get_odd(number_list: List[int]) -> List[int]:
  return [n for n in number_list if n % 2 != 0]