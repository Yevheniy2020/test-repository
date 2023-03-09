import matplotlib.pyplot as plt
import numpy as np

def coefficients_calculation(x_values, y_values):
    average_x = 0
    average_y = 0
    average_xy = 0
    average_xx = 0
    n = len(x_values)
    for i in range(n):
        average_x += x_values[i]
        average_y += y_values[i]
        average_xy += x_values[i]*y_values[i]
        average_xx += x_values[i]**2
    average_x = average_x/n
    average_y = average_y/n
    average_xy = average_xy/n
    average_xx = average_xx/n
    d_x = average_xx - average_x**2
    a = (average_xy - average_x*average_y)/d_x
    b = average_y - a * average_x
    return (a, b)


Iarr = [6.65, 13.64, 16.05, 16.54, 16.12, 21.54, 26.35,
     23.07, 32.00, 40.31, 45.74, 55.08, 61.88, 72.01, 65.49]

Uarr = [0.0006047, 0.001143, 0.001309, 0.001359, 0.001449, 0.001798, 0.001996,
     0.002062, 0.002839, 0.003614, 0.004008, 0.004492, 0.005171, 0.005536, 0.005906]


(I, U) = coefficients_calculation(Iarr, Uarr)

print('I  = ', I)
print('U  = ', U)
R = U / I
print('R = ', R)
f = np.array([I*z+U for z in range(100)])

plt.plot(f)
plt.scatter(I, U, s= 2, c='blue')
plt.scatter(Iarr, Uarr, s= 2, c='red')
# plt.scatter(R,R, s= 2, c='yellow')
plt.grid(True)
plt.show()