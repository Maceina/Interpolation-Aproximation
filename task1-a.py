from interpolation import f, newton_interpolation_f, np
import matplotlib.pyplot as plt

MAX_Y = 3.5

# Number of pointss
n = 30

# Interpolation function range
range_start = -3
range_end = 3
step_size = (range_end - range_start) / n

# X and Y values calculation
x_range = np.arange(range_start, range_end, step_size)
x_range = np.append(x_range, range_end)
y_range = [f(x) for x in x_range]

# Made interpolation function
interpol_f = newton_interpolation_f(x_range, y_range)

# Shows f(x) and interpolation graphs
plt.plot(np.arange(range_start, range_end, 0.01), [f(x) for x in np.arange(range_start, range_end, 0.01)], 'b',
         label='f(x)')
plt.plot(np.arange(range_start, range_end, 0.01), [interpol_f(x) for x in np.arange(range_start, range_end, 0.01)], 'r', label=f'{n} points interpolation function')
plt.scatter(x_range, y_range, color='g', label='Interpolation points')

plt.title("f(x) interpolation")
plt.xlabel('x')
plt.ylabel('f(x)')

plt.ylim(top=3.5, bottom=-10)
plt.grid(True)
plt.legend()
plt.show()