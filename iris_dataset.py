import pandas as pd
import numpy as np

def estimate_coeff(sepallengthcm,petallengthcm):
	n = np.size(sepallengthcm)
	mean_x = np.mean(sepallengthcm)
	mean_y = np.mean(petallengthcm)
	c_xy = np.sum(petallengthcm*sepallengthcm) - n*mean_y*mean_x
	c_xx = np.sum(sepallengthcm*sepallengthcm) - n*mean_x*mean_x
	p = c_xy / c_xx
	q = mean_y - p*mean_x
	return (q,p)

def line(sepallengthcm,petallengthcm,b):
	plt.scatter(sepallengthcm,petallengthcm, color = "red")
	y_pred = b[0] + b[1]*sepallengthcm
	plt.plot(sepallengthcm, y_pred, color = "g")
	plt.xlabel('SepalLengthCm')
	plt.ylabel('PetalLengthCm')
	plt.show()

sepallengthcm = np.array(sepallengthcm)
petallengthcm = np.array(petallengthcm)
b = estimate_coeff(sepallengthcm,petallengthcm)
line(sepallengthcm,petallengthcm,b)