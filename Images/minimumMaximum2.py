import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return x**3 - 10*x**2 - 3*x + 30

def hello():
	x = np.linspace(-6, 12, 1000)
	y1 = x**3 - 10*x**2 - 3*x + 30

	plt.figure()
	plt.axhline(color='k')
	plt.axvline(color='k')
	plt.plot(x, y1, label=r"$ f(x) = x^3 - 10x^2 - 3x + 30 $")
	plt.plot([(10 - np.sqrt(109))/3], [f((10 - np.sqrt(109))/3)], marker="o", label=r"$ A \approx (-0.147, 30.222) $")
	plt.plot([(10 + np.sqrt(109))/3], [f((10 + np.sqrt(109))/3)], marker="o", label=r"$ B \approx (6.813, -138.37) $")
	plt.grid(True)
	plt.legend()
	plt.savefig("minimumMaximum2.png")
	plt.show()


if __name__ == "__main__":
	hello()
