# Interactive Julia Set Explorer
![New Project (3)](https://github.com/edtireli/JuliaSet-Holomorphic-dynamics/assets/129996957/b9002326-9db7-4d6a-ba60-02a7296967cc)
This project provides an interactive visualization tool for exploring the Julia set, a complex fractal that emerges from iterating a holomorphic function over the complex plane. Users can dynamically zoom into regions of interest by clicking on the plot, revealing the fractal's intricate structure at various scales.

Author: Edis Devin Tireli, M.Sc, Ph.D. student

Affiliation: [Copenhagen University](https://www.ku.dk/english/)
## Mathematical Background
### Holomorphic Functions

In complex analysis, a holomorphic function is one that is complex differentiable at every point in its domain. More formally, a function $` f: \mathbb{C} 
\rightarrow \mathbb{C} `$ is said to be holomorphic if, for every $`z_0`$ in its domain, the limit

 $` \lim_{{z \to z_0}} \frac{{f(z) - f(z_0)}}{{z - z_0}} `$

exists. This implies that holomorphic functions are infinitely differentiable and thus analytic. The Julia set is intimately connected with the dynamics of holomorphic functions.

### Julia Sets

The Julia set of a complex function $` f `$, denoted $` J(f) `$, is the set of points in the complex plane that exhibit chaotic behavior under iteration of $` f `$. Mathematically, it can be described as the closure of the set of repelling periodic points. For a given complex parameter $` c `$, the filled-in Julia set $` K(f) `$ includes points $` z \in \mathbb{C} `$ such that the sequence $` \{f^n(z)\} `$ remains bounded. The boundary of this set is the Julia set $` J(f) `$.

For functions of the form $` f(z) = z^n + c `$, the behavior of the sequence $` f(z), f(f(z)), f(f(f(z))), \ldots `$ is determined by the initial point $` z `$ and the parameter $` c `$. The set is fractal and has a Hausdorff dimension greater than its topological dimension.

## Features

- **Interactivity**: Click to zoom in on areas within the plot to explore the Julia set in greater detail.
- **Custom Functions**: Users can input their own holomorphic function in the form $` f(z) = z^n + c `$ to generate unique Julia sets.
- **Optimized Performance**: Computation is accelerated using Numba, a Just-In-Time compiler for Python, facilitating real-time exploration.

## How to Use

### Installation

Ensure Python is installed on your system, along with the required packages: `numpy`, `matplotlib`, and `numba`. Install them using `pip` if necessary:

```bash
pip install numpy matplotlib numba
```

### Running the Script

Execute the script `julia_explorer.py` from the command line:

```bash
python julia_explorer.py
```

You will be prompted to enter a holomorphic function. Provide it in some usual form, e.g. `z^n + c`, or `sin(z)` or `exp(z)`:

```plaintext
Enter a function of z and c, like 'z^2 + c':
f(z, c) = z^2 + c
```
In the above case we choose the famous Mandelbrot set. A plot will then appear, showing the Julia set for your function. Click to zoom and investigate the fractal's complexity. See below for the given example: 

![Mandelbrot](https://github.com/edtireli/JuliaSet-Holomorphic-dynamics/assets/129996957/83191e32-8aa8-4d11-8615-4db257a887a8)
and see below for an example of a region of the Mandelbrot set above - can you find it on your own?
![Mandelbrot_1](https://github.com/edtireli/JuliaSet-Holomorphic-dynamics/assets/129996957/fa7a2ba0-66ba-4f20-8297-9344d34e1fcb)

## Contributing

We encourage contributions. Feel free to fork the repo, enhance the tool, and submit pull requests.

## License

This project is released under the MIT License - see the LICENSE file for details.

## Acknowledgments

- The mathematical community for the rich theory of complex dynamics.
- The developers of Numba for their exceptional work in accelerating Python code.
