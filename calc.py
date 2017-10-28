import numbers
import math
from decimal import Decimal
from fractions import Fraction

# 四則演算
x = 16
y = 3
val = x + y
print(val)  # 19
val = x - y
print(val)  # 13
val = x * y
print(val)  # 48
val = x / y
print(val)  # 5.3333
val = x // y
print(val)  # 5
val = x % y
print(val)  # 1
val = int(x / y)
print(val)  # 5
val = float(x)
print(val)  # 16.0

# 複素数
val = 3 + 5j
print(val.conjugate())  # (3-5j)

# 乗数
val = pow(2, 3)
print(val)  # 8
val = 2 ** 3
print(val)  # 8

# number module
result = isinstance(1, numbers.Number)
print(result)   # true
result = isinstance(1.1, numbers.Number)
print(result)   # true
result = isinstance(-1, numbers.Number)
print(result)   # true
result = isinstance(5+3j, numbers.Number)
print(result)   # true
result = isinstance(True, numbers.Number)
print(result)   # true
result = isinstance('text', numbers.Number)
print(result)   # false

# math module
# 指数
val = math.exp(2)
print(val)  # 7.3890

# 対数
val = math.log(5)
print(val)  # 1.6094

# 三角関数
val = math.sin(math.pi / 2)
print(val)  # 1.0

# decimal module
x = Decimal('0.1')
print(x)        # 0.1
print(x * 3)    # 0.3

is_equal = (x * 33 == Decimal('3.3'))
print(is_equal) # true

# fractions module
x = Fraction(3, 7)
print(x)    # 3/7

y = x * 7
print(y)    # 3

z = x + 0.1
print(z)    # 0.5285714285

