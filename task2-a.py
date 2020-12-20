from interpolation import f, newton_interpolation_f, np, chebyshev_range
import matplotlib.pyplot as plt

x_range = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y_range = [-3.6229, -0.8406, 3.87781, 12.0286, 15.1934, 19.1629, 23.0103, 18.827, 17.7749, 12.6973, 7.09253, 2.32522]


# Made interpolation function
interpol_f = newton_interpolation_f(x_range, y_range)

# X and Y values calculation
# range_x = np.arange(1, 12, 12/n)
range_x = chebyshev_range(100, 1, 12)
range_y = [interpol_f(_x) for _x in range_x]

# Shows f(x) and interpolation graphs
plt.scatter(x_range, y_range, label='Month`s temp. avg.')
plt.plot(range_x, range_y, 'r', label='Temp. interpolation')

plt.xticks(x_range)
plt.xlabel('Month')
plt.ylabel('Temp. avg.')

plt.title("2006 Hungary temperature")
plt.grid(True)
plt.legend()
plt.show()