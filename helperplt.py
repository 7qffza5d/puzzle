#make sure you have matplotlib installed and it can be run correctly in case you're running this in VSCode
#or run this in some online IDE for python
#just make sure you can use matplotlib
import matplotlib.pyplot as plt
#i dont remember if csv is a builtin package but make sure you can run it
import csv

points = []
with open('???.csv', 'r') as csvfile: #replace with the file name
    reader = csv.DictReader(csvfile)
    for row in reader:
        x = float(row['x'])
        y = float(row['y'])
        points.append((x, y))

x_vals = [p[0] for p in points]
y_vals = [p[1] for p in points]

plt.figure(figsize=(6,6))
plt.scatter(x_vals, y_vals, color='green', s=20)
plt.title(". _ . .")
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()