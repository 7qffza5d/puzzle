import matplotlib.pyplot as plt
import csv

# Read points from CSV
points = []
with open('???.csv', 'r') as csvfile: #replace with the file name
    reader = csv.DictReader(csvfile)
    for row in reader:
        x = float(row['x'])
        y = float(row['y'])
        points.append((x, y))

# Split into X and Y for plotting
x_vals = [p[0] for p in points]
y_vals = [p[1] for p in points]

# Plot
plt.figure(figsize=(6,6))
plt.scatter(x_vals, y_vals, color='green', s=20)
plt.title("owo what's this")
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
