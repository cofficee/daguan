import numpy as np
import math
x = np.array(np.random.normal(size=(3, 100)))
y = np.array(np.random.normal(size=(3, 100)))
c = np.dot(x.T, y)/math.sqrt(3)
print(np.var(c))
