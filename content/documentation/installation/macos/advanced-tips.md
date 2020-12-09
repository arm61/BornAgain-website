+++
title = "Advanced tips"
weight = 21
+++

## MacOS advanced tips

If your prefer to install the BornAgain python libraries not to the site-packages folder of your Python interpreter, but to some custom folder, you can do this in a following way.

* Run the `bornagain_install_python.py` script from application bundle:

```
$ python /Applications/BornAgain.app/Contents/libexec/BornAgain-{{< release-string-short >}}/bornagain_python_install.py
```

* Choose the option '[0]' - Generate bundle with BornAgain libraries, do not install it. 
You will get a message:

```
...
BornAgain Python bundle is successfully created in temporary directory 
'/var/folders/zt/0l4f_l_d46v5rkx668jqx0b4000lw7/T/bornagain_bundle'
...
```

* Go to the specified directory. Pay attention that on your system the name of this directory may differ from the name in this instruction.

```
$ cd /var/folders/zt/0l4f_l_d46v5rkx668jqx0b4000lw7/T/bornagain_bundle
```

* Set the environment variable `PYTHONUSERBASE` to the directory where you want the BornAgain libraries to be installed:

```
$ export PYTHONUSERBASE=/Users/me/my_python_extra
```

* Run the `setup.py` script to install the BornAgain core libraries to the specified folder

```
$ python setup.py install --user
```

* Check that the installation went successfully by typing

```
$ python -c "import bornagain"
```

If no error is displayed, the installation was successful.

You need to make sure that the `PYTHONUSERBASE` environment variable is always defined when you run your python scripts. You may also insert the corresponding export directive into your `.profile` configuration file:

```
$ export PYTHONUSERBASE=/Users/me/my_python_extra
```
