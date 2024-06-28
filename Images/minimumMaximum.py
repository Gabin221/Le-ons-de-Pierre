import numpy as np
import matplotlib.pyplot as plt

def hello():
	x = np.linspace(-8, 8, 1000)
	y1 = x**2 - 4*x - 3
	y2 = 2*x - 4

	plt.figure()
	plt.axhline(color='k')
	plt.axvline(color='k')
	plt.plot(x, y1, label=r"$ f(x) = x^2 - 4x + 3 $")
	plt.plot(x, y2, label=r"$ f(x) = 2x - 4 $")
	plt.plot([2], [-7], marker="o", label=r"$ A = (2, -7) $")
	plt.grid(True)
	plt.legend()
	plt.xlim(-8, 8)
	plt.savefig("minimumMaximum2.png")
	plt.show()


if __name__ == "__main__":
	hello()
