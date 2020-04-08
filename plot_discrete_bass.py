import sys
import matplotlib.pyplot as plt
import numpy as np
from discrete_bass_model import *

fig = plt.figure()
ax = plt.gca()

# Passing in the arguments from command line
p = float(sys.argv[1])
q = float(sys.argv[2])
M = int(sys.argv[3])
period = int(sys.argv[4])

# Getting the bass model
N, A = get_bass_model(p, q, M = M, period=period)

# Creating the time periods
t = list(range(0, period))

# Plotting the data. Changing size of points.
ax.plot(t, N, 'o', markersize = 4)

# Give a more cleaner look
# Removing the top and right spines.
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Setting label and title
ax.set_title('Adoption Count for p = {} and q = {}'.format(p, q))
ax.set_ylabel("New Customers")
ax.set_xlabel("Time (t)")

# Creating a clean layout
# Comment out plt.show() if you don't want a window to open
fig.tight_layout()
plt.show()

# saving image. Increase dpi for higher quality image
fig.savefig('bass-model', dpi = 500)
