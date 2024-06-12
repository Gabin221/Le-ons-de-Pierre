import numpy as np
import matplotlib.pyplot as plt

def hello():
	angles = np.linspace(np.pi/2, 5*np.pi/2, 1000)

	plt.figure()
	plt.plot(np.cos(angles), np.sin(angles))
	plt.text(1.05, 0.02, "cos(x)")
	plt.text(0.01, 1.02, "sin(x)")
	plt.text(-1.3, 0.02, "-cos(x)")
	plt.text(0.01, -1.07, "-sin(x)")
	plt.xlim(-1.5, 1.5)
	plt.ylim(-1.5, 1.5)
	plt.grid(True)
	plt.axis("equal")
	plt.axhline(color = 'k')
	plt.axvline(color='k')
	plt.annotate("", xy=(0.5, 1.05), xycoords='data', xytext=(1.05, 0.5), textcoords='data', arrowprops=dict(arrowstyle="->", connectionstyle="angle3"))
	plt.text(1.05, 0.8, "intégrale")
	plt.annotate("", xy=(0.5, -1.05), xycoords='data', xytext=(1.05, -0.5), textcoords='data', arrowprops=dict(arrowstyle="->", connectionstyle="angle3"))
	plt.text(1.05, -0.8, "dérivée")
	plt.savefig("cercleTrigoDeriveeIntegrale.png")
	plt.show()


if __name__ == "__main__":
	hello()
