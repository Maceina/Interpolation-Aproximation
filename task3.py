import matplotlib.pyplot as plt
from ast import literal_eval
import numpy as np
from interpolation import parametric_interpolation, hermite_interpolation_spline
from task3_data import x_range, y_range

n = 50  # Number of interpolation points
step = 0.1  # Graph's precision

# Reducing interpolation points to selected
t = range(n + 1)
x_range = x_range[::(306 // n)]
y_range = y_range[::(306 // n)]

ff = hermite_interpolation_spline(t, x_range)
ff2 = hermite_interpolation_spline(t, y_range)

xx, yy = parametric_interpolation(ff, ff2, np.arange(0, n, step))

plt.plot(xx, yy, 'r', label="Country's border")
plt.scatter(x_range, y_range, label=f"{n} Interpolation points")

plt.title('Hungary')
plt.legend()
plt.show()