# ******* 1. NumPy *******

# *** importing numpy ***
# import numpy
import numpy as np      # --> most commonly used
# from numpy import *

# *** simple array production ***
array = np.array([1, 4, 5, 8], float)
print(array)
type(array)

array3d = np.array([[1, 4, 5],
                   [3, 8, 2],
                   [7, 9, 6]], float)

# *** slicing arrays ***
# the inputs in the bracket represent; [start:end:step]
slicing1 = array3d[1, :]
print(slicing1)
# get the second element, indexing from the start and end
# the execution >>> array([3., 8., 2.])
slicing2 = array3d[:,2]
print(slicing2)
# get the third steps of every element (indexing start from 0)
# the execution >>> array([5, 2, 6])

reshapeArray = np.array(range(6), float)
reshapeArray = reshapeArray.reshape((3, 2))
print(reshapeArray)
# the execution >>> array([0., 1., 2., 3.])


# *** array operations provided similar to List ***
array3d.sum()
# np.sum(array3d)
array3d.prod()
# np.prod(array3d)
array3d.min()
array3d.max()
array3d.sort()

# *** argmin and argmax ***
array3d.argmin()
array3d.argmax()

# *** statistical quatities ***
array3d.mean()
array3d.var()   # variation
array3d.std()   # standard deviation

# *** dot product ***
dotArray1 = np.array([1, 2, 3], float)
dotArray2 = np.array([0, 1, 1], float)

np.dot(dotArray1, dotArray2)
np.outer(dotArray1, dotArray2)
np.inner(dotArray1, dotArray2)
np.cross(dotArray1, dotArray2)

# *** polynomial roots and equations evaluation ***
np.poly([-1, 1, 1, 10])
# the execution >>> array([1, -11, 9, 11, -10])
# the list of elements [-1, 1, 1, 10] represent the roots of the polynomial x^(4)-11x^(3)+9x^(2)+11x-10
np.roots([1, -11, 9, 11, -10])
# the execution >>> array([-1, 1, 1, 10])
np.polyint([1, 1, 1, 1])
# >>> array([0.25, 0.333333333, 0.5, 1., 0.])
np.polyder([0.25, 0.333333333, 0.5, 1., 0.])
# >>> array([1., 1., 1., 1.])
np.polyval([1, -2, 0, 2], 4)
# >>> 34
x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [0, 2, 1, 3, 7, 10, 11, 19]
np.polyfit(x, y, 2)
# >>> array([ 0.375 , -0.88690476, 1.05357143])


# ******* 2. Matplolib *******
# *** import numpy as np ***
import matplotlib.pyplot as plt

# *** plots and subplots ***
# Compute the x and y coordinates for points on sine and cosine curves
x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

# Plot the points using matplotlib
plt.plot(x, y_sin)
plt.plot(x, y_cos)
plt.xlabel('x axis label')
plt.ylabel('y axis label')
plt.title('Sine and Cosine')
plt.legend(['Sine', 'Cosine'])
plt.show()

# Set up a subplot grid that has height 2 and width 1,
# and set the first such subplot as active.
plt.subplot(2, 1, 1)
plt.plot(x, y_sin)
plt.title('Sine')

# Set the second subplot as active, and make the second plot.
plt.subplot(2, 1, 2)
plt.plot(x, y_cos)
plt.title('Cosine')

# Show the figure.
plt.show()

# *** image ***
# import numpy as np
from scipy.misc import imread, imresize
# import matplotlib.pyplot as plt

img = imread('assets/cat.jpg')
img_tinted = img * [1, 0.95, 0.9]

# Show the original image
plt.subplot(1, 2, 1)
plt.imshow(img)

# Show the tinted image
plt.subplot(1, 2, 2)

# A slight gotcha with imshow is that it might give strange results
# if presented with data that is not uint8. To work around this, we
# explicitly cast the image to uint8 before displaying it.
plt.imshow(np.uint8(img_tinted))
plt.show()