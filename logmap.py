import matplotlib.pyplot as plt

def logmap(r,x):
	return r*x*(1-x)

def experiment(r,x,n):
	for i in range(n) :
		print(x)
		x = logmap(r,x)

def table(r,x,y,n):
	for i in range(n) :
		print(x,y)
		x = logmap(r,x)
		y = logmap(r,y)

def attractors(r,x,n,epsilon):
	xs = []
	for i in range(n):
		xs.append(x);
		x = logmap(r,x)
		for j,y in enumerate(xs):
			if abs(x-y) < epsilon:
				return xs[j:]
	return None

def bifurcationDiagram():
	X = []
	Y = []
	for i in range(200):
		r = i*2/100
		xs = attractors(r,0.5,250,0.00001)
		if xs != None:
			for x in xs:
				X.append(r)
				Y.append(x)

	plt.plot(X, Y, '.', markersize=1)
	plt.show()
