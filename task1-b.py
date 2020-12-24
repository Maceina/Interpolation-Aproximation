from interpolation import f, newton_interpolation_f, chebyshev_range, np
import matplotlib.pyplot as plt

# Number of points
n = 30

# Interpolation function ranges
range_start = -3
range_end = 3
step_size = (range_end - range_start) / n

# X and Y values calculation using chebyshev polynomial
x_range_cheb = chebyshev_range(n, range_start, range_end)
y_range_cheb = [f(x) for x in x_range_cheb]

# Made interpolation function
interpol_f = newton_interpolation_f(x_range_cheb, y_range_cheb)

# Shows f(x) and interpolation graphs
plt.plot(np.arange(range_start, range_end, 0.01), [f(x) for x in np.arange(range_start, range_end, 0.01)], 'b',
         label='f(x)')
plt.plot(np.arange(range_start, range_end, 0.01), [interpol_f(x) for x in np.arange(range_start, range_end, 0.01)], 'r',
         label=f'{n} points interpolation function')
plt.scatter(x_range_cheb, y_range_cheb, color='g', label='Interpolation points')

plt.title('f(x) interpolation using Chebyshev x')
plt.xlabel('x')
plt.ylabel('f(x)')

plt.grid(True)
plt.legend()
plt.show()