import numpy as np
import matplotlib.pyplot as plt

def hello():
	angles = np.linspace(0, np.arctan(4/3), 1000)

	plt.figure()
	plt.axhline(color='k')
	plt.axvline(color='k')
	plt.plot([3], [4], marker='o', label=r"$ z = 3 + 4i $")
	plt.plot([0, 3], [0, 4], label=r"$ |z| $")
	plt.plot(np.cos(angles), np.sin(angles), label=r"$ arg(z) $")
	plt.plot([0, 3], [0, 0], label=r"$ Re(z) = a $")
	plt.plot([3, 3], [0, 4], label=r"$ Im(z) = b $")
	plt.grid(True)
	plt.legend()
	plt.axis("equal")
	plt.xlim(-1, 5)
	plt.savefig("complexes.png")
	plt.show()


if __name__ == "__main__":
	hello()
