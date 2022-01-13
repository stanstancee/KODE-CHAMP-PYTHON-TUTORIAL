#generator short-hand
my_odds_gn = (x for x in range(3000) if not x % 2 == 0)
my_odds_lt = [x for x in range(3000) if not x % 2 == 0]
print(my_odds_gn) # <generator object <genexpr> at 0x7f2ae827c2e0>
print(my_odds_lt) # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# convert generator to a list
odds = list(my_odds_gn)
print(odds) # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# profiling
import sys
print(sys.getsizeof(my_odds_gn)) # 112 bytes
print(sys.getsizeof(my_odds_lt)) # 13000 bytes

import cProfile
cProfile.run('sum((x for x in range(3000) if not x % 2 == 0))') # 0.007 seconds
cProfile.run('sum([x for x in range(3000) if not x % 2 == 0])') # 0.001 seconds