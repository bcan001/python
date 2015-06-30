# http://matplotlib.org/users/pyplot_tutorial.html

import matplotlib.pyplot as plt
# plt.plot([1,2,3,4])
# plt.ylabel('some numbers')
# plt.show()


 # plt.axis[xmin, xmax, ymin, ymax]
# plt.plot([1,2,3,5], [1,4,9,16], 'ro')
# plt.axis([0, 6, 0, 20])
# plt.show()



# all sequences are converted to numpy arrays internally. The example below illustrates a plotting several lines with different format styles in one command using arrays.
import numpy as np
# evenly sampled time at 200ms intervals
# (start of the interval, end of the interval, spacing between values)
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
# [trangle, equation, shape]
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()

