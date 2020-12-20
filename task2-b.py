import matplotlib.pyplot as plt
from scipy import interpolate
import numpy as np
from interpolation import hermite_interpolation_spline

x_range = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y_range = [-3.6229, -0.8406, 3.87781, 12.0286, 15.1934, 19.1629, 23.0103, 18.827, 17.7749, 12.6973, 7.09253, 2.32522]

interpolation_f = hermite_interpolation_spline(x_range, y_range)

plt.scatter(x_range, y_range, label='Month`s avg. temp')
plt.plot(np.arange(x_range[0], x_range[-1], 0.01),
         [interpolation_f(_x) for _x in np.arange(x_range[0], x_range[-1], 0.01)],
         'r', label='Spline')

plt.xlabel('Month')
plt.ylabel('Temp. avg.')
plt.title('Ermito interpoliavimo splainas')

plt.grid(True)
plt.legend()
plt.show()