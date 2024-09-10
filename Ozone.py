import numpy as np
import matplotlib.pyplot as ply
import math

# Based on data from Davidson, "Update on Ozone Trends in California's South Coast Air Basin," Air and Waste, 43, 226, 1993.

y_days = np.array([91, 105, 106, 108, 88, 91, 58, 82, 81, 65, 61, 48, 61, 43, 33, 36])
X_index = np.array([16.7, 17.1, 18.2, 18.1, 17.2, 18.2, 16.0, 17.2, 18.0, 17.2, 16.9, 17.1, 18.2, 17.3, 17.5, 16.6])

linear_function = lambda x : (x * 15.2964) - 192.9844

linear_model = np.array([linear_function(xi) for xi in X_index])

up_conf_func = lambda xi : ((xi * 15.2964) - 192.9844) + (2.1448 * math.sqrt(566.20 * ((1 / 16) + (((xi - 17.3438) ** 2)/6.3794))))
low_conf_func = lambda xi : ((xi * 15.2964) - 192.9844) - (2.1448 * math.sqrt(566.20 * ((1 / 16) + (((xi - 17.3438) ** 2)/6.3794))))

prediction_x = np.array([i for i in np.arange(X_index.min(), X_index.max(), 0.1)])

low_conf_bound = np.array([low_conf_func(xi) for xi in prediction_x])
up_conf_bound = np.array([up_conf_func(xi) for xi in prediction_x])

low_pred_func = lambda xi : ((xi * 15.2964) - 192.9844) - (2.1448 * math.sqrt(566.20 * (1 + (1 / 16) + (((xi - 17.3438) ** 2)/6.3794))))
up_pred_func = lambda xi : ((xi * 15.2964) - 192.9844) + (2.1448 * math.sqrt(566.20 * (1 + (1 / 16) + (((xi - 17.3438) ** 2)/6.3794))))

low_pred_bound = np.array([low_pred_func(xi) for xi in prediction_x])
up_pred_bound = np.array([up_pred_func(xi) for xi in prediction_x])

ply.scatter(X_index, y_days)
ply.plot(X_index, linear_model, label='Linear Model')
ply.plot(prediction_x, low_conf_bound, label='Lower Confidence Bound')
ply.plot(prediction_x, up_conf_bound, label='Upper Confidence Bound')
ply.plot(prediction_x, low_pred_bound, label='Lower Prediction Bound')
ply.plot(prediction_x, up_pred_bound, label='Upper Prediction Bound')
ply.title('Days Ozone Exceeded 0.20ppm v. Meteorological Index')
ply.xlabel('Index')
ply.ylabel('Days (Ozone Exceeded 0.20ppm)')
ply.legend(loc='upper left', prop={'size': 6})
ply.savefig('Ozone_Figure.png')
ply.show()