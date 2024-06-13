import numpy as np
import matplotlib.pyplot as plt

def hello():
	x1 = np.linspace(-10, 15, 1000)
	x2 = np.linspace(0.00001, 15, 1000)
	y1 = np.log(x2)
	y2 = np.exp(x1)
	y3 = x1

	plt.figure()
	plt.axhline(color = 'k')
	plt.axvline(color='k')
	plt.plot(x1, y2, label=r"$ f(x) = log(x) $")
	plt.plot(x2, y1, label=r"$ f(2) = e^{x} $")
	plt.plot(x1, y3, label=r"$ f(x) = x $")
	plt.grid(True)
	plt.legend()
	plt.axis('equal')
	plt.xlim(0, 5)
	plt.ylim(-3, 10)
	plt.savefig("reciproqueLogExp.png")
	plt.show()


if __name__ == "__main__":
	hello()
