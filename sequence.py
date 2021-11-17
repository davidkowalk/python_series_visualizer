from matplotlib import pyplot as plt

def render(s, n=1, m=10):
	"""
	Takes a sequence and an interval [n, m) and renders out the series.
	"""

	x = list()
	y = list()
	sum = 0

	for i in range(n, m):
		x.append(i)
		sum += s(i)
		y.append(sum)

	#Render
	plt.plot(x,y)
	plt.show()

	# Return x and y
	return x, y
