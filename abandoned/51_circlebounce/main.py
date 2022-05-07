from fractions import Fraction
from typing import List

M = 1_000_000_007

# class Fraction:
#   """ Class representing a fraction with a numerator and denominator """
  
#   def __init__(self, numerator: int, denominator: int = None):
#     self.numerator = numerator
#     self.denominator = 1 if denominator == None else denominator
  
#   def __mul__(self, other):
#     return Fraction(
#       self.numerator * other.numerator,
#       self.denominator * other.denominator
#     )
  
#   def __add__(self, other):
#     return Fraction(
#       self.numerator + other.numerator,
#       self.denominator + other.denominator
#     )
  
#   def __neg__(self):
#     return Fraction(-self.numerator, self.denominator)
  
#   def __str__(self):
#     return f"{self.numerator}/{self.denominator}"
  
#   __repr__ = __str__


class Matrix:
  """ Class representing a 2x2 matrix of fractions """

  def __init__(self, elements: List[Fraction]):
    self.elements = elements
  
  def __str__(self):
    return f"{self.elements[0]} {self.elements[1]}; {self.elements[2]} {self.elements[3]}"
  
  __repr__ = __str__
  
  def __mul__(self, other):
    if isinstance(other, Matrix):
      return self.mul_matrix(other)
    else:
      return self.mul_vector(other)
  
  def mul_matrix(self, other):
    return Matrix([
      (self.elements[0] * other.elements[0]) + (self.elements[1] * other.elements[2]),
      (self.elements[0] * other.elements[1]) + (self.elements[1] * other.elements[3]),
      (self.elements[2] * other.elements[0]) + (self.elements[3] * other.elements[2]),
      (self.elements[2] * other.elements[1]) + (self.elements[3] * other.elements[3])
    ])
  
  def mul_vector(self, other):
    return [0, 0]


def matrix_modulo_M(m: Matrix):
  elements = m.elements.copy()
  mod_elements = [None] * len(elements)
  for i, frac in enumerate(elements):
    mod_frac = Fraction(frac.numerator % M, frac.denominator % M)
    mod_elements[i] = mod_frac
  return Matrix(mod_elements)

def main():
  a, b, n = tuple(map(int, input().split()))

  # 1. Find first collision point
  collision_x = Fraction(-1) + Fraction(2 * (b ** 2), (a ** 2) + (b ** 2))
  collision_y = Fraction(2 * a * b, (a ** 2) + (b ** 2))

  
  # 2. Set up matrices representing the linear transformation of rotation
  NUM_MATRICES = 5
  matrices: List[Matrix] = [None] * NUM_MATRICES
  matrices[0] = Matrix([ -collision_x, collision_y, -collision_y, -collision_x ])
  print(f"collision: ({collision_x}, {collision_y})")
  print(f"matrix: {matrices[0]}")
  for i in range(len(matrices) - 1):
    mul = matrices[i] * matrices[i]
    matrices[i + 1] = matrix_modulo_M(mul)
  print(matrices)

if __name__ == "__main__":
  main()