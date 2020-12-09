+++
title = "Run a first simulation"
weight = 40
+++

## Run a first simulation

This section explains how to run a first simulation.

* [Post installation steps](#post-installation-steps")
* [Running the first Python simulation](#running-the-first-python-simulation")
* [Running the BornAgain GUI](#running-the-borngain-gui")

#### Post installation steps

After the installation is complete, the location of the BornAgain libraries needs to be included into the `LD_LIBRARY_PATH` (or `DYLD_LIBRARY_PATH` for MacOS) and `PYTHONPATH` environment variables. This can be done by running the BornAgain setup script in a terminal:

```bash
source <install_dir>/bin/thisbornagain.sh
```

This command can also be placed in your `.bashrc` file (`.profile` for MacOS) to avoid having to run this command for each terminal session.

#### Running the first Python simulation

In your installation directory you will find the following directory structure:

```
|-- bin                   - Links to executables
|-- include
|   |-- BornAgain-{{< release-string-short >}}    - C++ headers for development purposes
|-- lib
|   |-- BornAgain-{{< release-string-short >}}    - The BornAgain libraries
|-- share
|   |-- BornAgain-{{< release-string-short >}}
|       |-- Examples      - Directory with examples
```

Run an example and enjoy your first BornAgain simulation plot.

```python
python <install_dir>/share/BornAgain-{{< release-string-short >}}/Examples/python/simulation/ex01_BasicParticles/CylindersAndPrisms.py
```
 
#### Running the BornAgain GUI

The BornAgain application can be run by executing following command
```bash
$ <install_dir>/bin/bornagain
```