import numpy as np
import matplotlib.pyplot as plt

def hello():
	x = np.linspace(-5, 5, 1000)
	y = 4*x**2 + 5*x - 4

	plt.figure()
	plt.axhline(color = 'k')
	plt.axvline(color='k')
	plt.plot(x, y, label=r"$ f(x) = 4x^{2} + 5x - 4 $")
	plt.plot([(-5 - np.sqrt(89))/8], [0], marker="o", label=r"$ x_{1} = \frac{-5 - \sqrt{89}}{8} $")
	plt.plot([(-5 + np.sqrt(89))/8], [0], marker="o", label=r"$ x_{2} = \frac{-5 + \sqrt{89}}{8} $")
	plt.grid(True)
	plt.legend()
	plt.xlim(-4, 3)
	plt.ylim(-10, 50)
	plt.savefig("resolutionEquationSecondDegre.png")
	plt.show()


if __name__ == "__main__":
	hello()
