+++
title = "Matplotlib configuration"
weight = 12
+++

## Matplotlib configuration

Images in BornAgain examples are generated using the Python library
[Matplotlib](https://matplotlib.org/).

Default settings can be overridden by command-line arguments,
by function arguments, or through Matplotlib ressources.

### Plot invocation

When running BornAgain through Python sripts, Matplotlib is invoked
either directly, or indirectly through BornAgain functions like
`plot_simulation_result`.
For direct invocation, see the [Matplotlib documentation](https://matplotlib.org/contents.html).
Here we are concerned with indirect inocation through standard BornAgain plot functions.

The function `plot_simulation_result`, and a number of lower-level functions,
are all implemented in the Python module
[`plot_utils`](https://github.com/scgmlz/BornAgain/blob/master/Wrap/python/plot_utils.py)
that is part of the `bornagain` module.
These functions support the keyword arguments

* `intensity_min`,
* `intensity_max`,
* `xlabel`,
* `ylabel`,
* `zlabel`,
* `cmap`: color map, see below,
* `aspect`: [aspect ratio](https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.set_aspect.html), can be 'auto', 'equal', or a number,
* `noshow`: if `True`, run Matplotlib in batch mode, without displaying a plot.

If a simulation script `sim.py` contains code like
```python
import bornagain as ba
...
if __name__ == '__main__':
    result = run_simulation()
    ba.plot_simulation_result(result, *sys.argv[1:])
```
then keyword arguments can be passed from the command line:
```bash
$ python3 sim.py cmap=jet intensity_min=2e-8 intensity_max=2
```

### Matplotlib ressources

Matplotlib default settings can be changed through ressource arguments or ressource files.
See the
[Matplotlib customizing tutorial](https://matplotlib.org/tutorials/introductory/customizing.html)
for an introduction to ressources;
see in particular the section on [`matplotlibrc` ressource files](https://matplotlib.org/tutorials/introductory/customizing.html#customizing-with-matplotlibrc-files).
Note, however, that the color map (`cmap`) ressource setting is ignored
when Matplotlib is used indirectly through BornAgain plot functions.

### Color map

Whenever plotting is done through `plot_simulation_result`,
or through one of the other functions from `plot_utils.py`,
BornAgain imposes its default color map "inferno".
Inferno is one of the five "perceptually uniform sequential" color maps
recommended in the
[Matplotlib color maps tutorial](https://matplotlib.org/tutorials/colors/colormaps.html#Perceptually).

![Matplotlib perceptually uniform sequential color maps](/img/matplotlib_pus_colormaps.png "Perceptually uniform sequential color maps from Matplotlib.")

Note that this choice of "inferno" is hard-coded,
and overrides the "cmap" setting from Matplotlib ressources.
It can however be overridden by a keyword argument, like `cmap='jet'`.
