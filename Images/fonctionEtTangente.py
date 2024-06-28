import numpy as np
import matplotlib.pyplot as plt

def hello():
	x = np.linspace(-8, 8, 1000)
	y1 = 3*x**2-3
	y2 = 12*x - 15

	plt.figure()
	plt.axhline(color='k')
	plt.axvline(color='k')
	plt.plot(x, y1, label=r"$ f(x) = 3x^2-3 $")
	plt.plot(x, y2, label=r"$ f(x) = 12x - 15 $")
	plt.grid(True)
	plt.legend()
	plt.xlim(-6, 6)
	plt.savefig("fonctionEtTangente.png")
	plt.show()


if __name__ == "__main__":
	hello()
