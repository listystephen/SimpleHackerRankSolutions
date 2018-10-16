import numpy as np

order = int(raw_input())
print np.linalg.det([(map(float,raw_input().split())) for _ in xrange(order)])
