'''
Part 1 - Numpy

Use this dataset for the first 4 questions.

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])

1. Define two custom numpy arrays, say A and B. Generate two new numpy arrays by stacking A and B vertically and horizontally.

2. Find common elements between A and B. [Hint : Intersection of two sets]

3. Extract all numbers from A which are within a specific range. eg between 5 and 10. [Hint: np.where() might be useful or boolean masks]

4. Filter the rows of iris_2d that has petallength (3rd column) > 1.5 and sepallength (1st column) < 5.0
'''
import numpy as np

# 1. Define two custom NumPy arrays, A and B
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[5, 6, 7], [8, 9, 10], [11, 12, 13]])

# Stack A and B vertically and horizontally
vertical_stack = np.vstack((A, B))
horizontal_stack = np.hstack((A, B))

print("Vertically Stacked Array:\n", vertical_stack)
print("\nHorizontally Stacked Array:\n", horizontal_stack)

# 2. Find common elements between A and B
common_elements = np.intersect1d(A, B)
print("\nCommon Elements Between A and B:", common_elements)

# 3. Extract all numbers from A that are within the range [5, 10]
filtered_A = A[(A >= 5) & (A <= 10)]
print("\nNumbers in A between 5 and 10:", filtered_A)

# 4. Load the iris dataset (only using 4 columns)
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])

# Filter rows where petal length (3rd column) > 1.5 and sepal length (1st column) < 5.0
filtered_rows = iris_2d[(iris_2d[:, 2] > 1.5) & (iris_2d[:, 0] < 5.0)]
print("\nFiltered Rows from iris_2d:\n", filtered_rows)

