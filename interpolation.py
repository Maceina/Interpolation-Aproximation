import numpy as np


def f(x):
    """
    Function given by tasks
    :param x: x value
    :return: y value
    """
    return (np.e ** (-x**2) * np.cos(x**2) * (x-3)*(x**2 + 3))
"""
    Calculates x range values using chebyshev polynomial formula
    :param count: Points count
    :param start: x range start
    :param end: x range end
    :return: Calculated x values array
    """

def chebyshev_range(count, start, end):
    range_x = []
    for i in range(count):
        temp = (end + start) / 2 + (end - start) / 2 * np.cos((2 * i + 1) * np.pi / (2 * count))
        range_x.append(temp)

    return range_x

    """
    Calculates coefficients for newton's interpolation formula
    :param range_x: All x values
    :param range_y: All y values
    :return: Calculated coefficients
    """
def newton_interpolation_coefficients(range_x, range_y):
    a = [range_y]
    for i in range(len(range_x)):
        a.append([])
        for j in range(1, len(range_x) - i):
            a[i + 1].append((a[i][j] - a[i][j - 1]) / (
                    range_x[np.min([i + j, len(range_x) - 1])] - range_x[np.max([i + j - (i + 1), 0])]))

    return [_a[0] for _a in a[:-1]]

"""
    Makes interpolation function
    :param range_x: all x values
    :param range_y: all y values
    :return: Interpolation function
        Inner function
        Calculates y value from the newton's interpolation function
        :param _x: x value
        :return: y value
        """
def newton_interpolation_f(range_x, range_y):
    a_coefficients = newton_interpolation_coefficients(range_x, range_y)

    def interpolation_f(_x):
        ff = a_coefficients[0]
        tmp = 1
        for ii in range(1, len(a_coefficients)):
            tmp *= (_x - range_x[ii - 1])
            ff += a_coefficients[ii] * tmp

        return ff

    return interpolation_f


def akima_points_derivative(range_x, range_y):
    """
    TODO: not working
    Calculates each point slope
    Source: https://en.wikipedia.org/wiki/Akima_spline
    :param range_x: x range values array
    :param range_y: y range values array
    :return: each point calculated slope values array
    """

    def m(index):
        """
        Slope of the line segment calculation (from wiki source)
        :param index: Point index
        :return: Calculated slope of the line segment
        """
        return (range_y[index + 1] - range_y[index]) / (range_x[index + 1] - range_x[index])

    range_s = []
    for i in range(2, len(range_x) - 2):
        range_s.append((np.abs(m(i + 1) - m(i)) * m(i - 1) + np.abs(m(i - 1) - m(i - 2)) * m(i)) / (
                np.abs(m(i + 1) - m(i)) + np.abs(m(i - 1) - m(i - 2))))

    return range_s


def U(start, end, x):
    return (1 - 2 * (1 / (start - end)) * (x - start)) * ((x - end) / (start - end)) ** 2


def V(start, end, x):
    return (x - start) * ((x - end) / (start - end)) ** 2


def hermite_interpolation_spline(range_x, range_y):
    range_dy = points_slopes(range_x, range_y)

    def spline_function(x):
        index = np.searchsorted(range_x, x)
        try:
            result = U(range_x[index - 1], range_x[index], x) * range_y[index - 1] + V(range_x[index - 1],
                                                                                       range_x[index],
                                                                                       x) * range_dy[index - 1] \
                     + U(range_x[index], range_x[index - 1], x) * range_y[index] \
                     + V(range_x[index], range_x[index - 1], x) * range_dy[index]
        except TypeError:
            return None
        return result

    return spline_function



def slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)


def points_slopes(range_x, range_y):
    """
    Calculates slopes for each interval between given points
    :param range_x: x values
    :param range_y: y values
    :return: Slopes array
    """

    slopes = []
    for i in range(len(range_x) - 1):
        if range_x[i] is None or range_x[i + 1] is None or range_y[i] is None or range_y[i + 1] is None:
            slopes.append(None)
        else:
            slopes.append(slope(range_x[i], range_y[i], range_x[i + 1], range_y[i + 1]))

    slopes.append(slopes[-1])
    return slopes


def parametric_interpolation(fx, fy, range_t):
    x_results = []
    y_results = []
    for t in range_t:
        x_results.append(fx(t))
        y_results.append(fy(t))

    return x_results, y_results