import numpy as np
import matplotlib.pyplot as plt
from numba import jit

# Get the user-defined function and set initial bounds accordingly
def get_user_function():
    print("Enter a function of z and c. For example, 'z^2 + c':")
    user_function = input("f(z, c) = ").strip()

    # Replace caret symbols with Python's exponentiation operator
    user_function_numeric = user_function.replace('^', '**')

    # Check if the user entered the Mandelbrot set function, which uses specific initial bounds
    mandelbrot_check = user_function_numeric.replace(' ', '').replace('np.', '')
    if 'z**2+c' in mandelbrot_check:
        initial_bounds = (-2-1j, 1+1j)
    else:
        initial_bounds = (-2-1j, 2+1j)

    # Prepare the function text to be compiled
    function_text = f"def holomorphic(z, c):\n    return {user_function_numeric}"

    # Create a local dictionary to exec the function definition
    local_dict = {}
    # Include numpy functions that might be used in the user-defined function
    numpy_functions = {'np': np, 'exp': np.exp, 'sin': np.sin, 'cos': np.cos}
    exec(function_text, numpy_functions, local_dict)

    # Extract the function from the local dictionary
    holomorphic_func = jit(nopython=True)(local_dict['holomorphic'])

    return user_function, user_function_numeric, initial_bounds, holomorphic_func


# Prompt user for the function, convert it for computation, and get initial bounds
user_input, user_function_numeric, initial_bounds, holomorphic = get_user_function()

# Function to compute the Julia set, optimized with Numba
@jit(nopython=True)
def compute_julia_set(re_min, re_max, im_min, im_max, width, height, max_iter, holomorphic_func):
    reals = np.linspace(re_min, re_max, width)
    imags = np.linspace(im_min, im_max, height)
    julia = np.empty((width, height), dtype=np.int32)
    for i in range(width):
        for j in range(height):
            c = complex(reals[i], imags[j])
            z = 0
            for n in range(max_iter):
                z = holomorphic_func(z, c)
                if abs(z) > 2:
                    julia[i, j] = n
                    break
            else:
                julia[i, j] = max_iter
    return julia.T

# Class for interactive exploration of the Julia set
class JuliaSetExplorerClickZoom:
    def __init__(self, initial_bounds, dim, max_iter):
        self.bounds = initial_bounds
        self.dim = dim
        self.max_iter = max_iter
        self.fig, self.ax = plt.subplots(figsize=(16, 9))
        self.ax.axis('off')
        plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
        self.fig.canvas.mpl_connect('button_press_event', self.onclick)
        self.zoom_factor = 0.6
        self.plot_julia(*self.bounds)

    def plot_julia(self, cmin, cmax):
        width, height = self.dim, int(self.dim * 9 / 16)
        julia_set = compute_julia_set(cmin.real, cmax.real, cmin.imag, cmax.imag, width, height, self.max_iter, holomorphic)
        self.ax.imshow(julia_set, extent=(cmin.real, cmax.real, cmin.imag, cmax.imag),
                       cmap='Spectral', interpolation='bilinear', aspect='auto', origin='lower')
        self.ax.set_title(f"Julia Set for f(z, c) = {user_input}")
        self.ax.figure.canvas.draw_idle()

    def onclick(self, event):
        if event.inaxes != self.ax: return
        x, y = event.xdata, event.ydata
        current_width = self.bounds[1].real - self.bounds[0].real
        current_height = self.bounds[1].imag - self.bounds[0].imag
        new_width = current_width * self.zoom_factor
        new_height = current_height * self.zoom_factor
        new_x_min = max(self.bounds[0].real, x - new_width / 2)
        new_x_max = min(self.bounds[1].real, x + new_width / 2)
        new_y_min = max(self.bounds[0].imag, y - new_height / 2)
        new_y_max = min(self.bounds[1].imag, y + new_height / 2)
        self.bounds = (complex(new_x_min, new_y_min), complex(new_x_max, new_y_max))
        self.ax.cla()
        self.plot_julia(*self.bounds)

    def show(self):
        plt.show()

# Set the dimensions and maximum iterations for the Julia set exploration
dim = 2000
max_iter = 100

# Create an instance of the explorer and show the plot
click_explorer = JuliaSetExplorerClickZoom(initial_bounds, dim, max_iter)
click_explorer.show()
