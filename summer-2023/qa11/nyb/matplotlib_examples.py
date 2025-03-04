from matplotlib.pyplot import plot, title, show, legend

data_points = [(1,2.1), (2,3.2), (3,3.85), (4,5.15), (5,6.05)]
y_predictions = [2,3,4,5,6]

xs = [x for (x,y) in data_points]
ys = [y for (x,y) in data_points]

plot(xs, ys, 'ro')
plot(xs, y_predictions, label="predicted")
title("Linear regression")
legend()
show()
