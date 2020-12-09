+++
title = "Python troubleshooting"
weight = 30
+++

## Python troubleshooting

When BornAgain is installed on the system, its library directory is automatically added to the `PYTHONPATH` environment directory.

{{< figscg src="python-troubleshooting1.png" class="center" width="450px">}}

This enables the use of the `import bornagain` statement in any Python script and run this script using the Python interpreter installed on the system.

Sometimes this process can fail. The following checklist can be useful to tackle possible  causes of the problem.

* [How many Python distributions are installed on the system?]({{% relref "#how-many-python" %}})
* [Does the Python interpreter version matches the BornAgain installation?]({{% relref "#does-interpreter-match" %}})
* [Are you using the Anaconda installation?]({{% relref "#is-anaconda" %}})
* [Are you using a native Python installation?]({{% relref "#is-native-python" %}})

<hr>

#### How many Pythons are installed on the system? 
{{% anchor "how-many-python" %}}

Please note that having more than one Python interpreter installed on the system is potentially error-prone and requires some skills from the user 
to be able to manage their co-existence. If you have more than one Python, please consider uninstalling all of them but one.

<hr>

#### Does the Python interpreter version matches the BornAgain installation?
{{% anchor "does-interpreter-match" %}}

BornAgain is a `64-bit` application and requires a `64-bit` Python installed on the system. Additionally, you can't use BornAgain intended for Python
{{% recommended-python %}} together with an older Python 2.7.
Please make sure that the Python version number, as specified
in the BornAgain installer name (e.g. `{{% installer-win-name "3.7" %}}`),
matches the Python installation on your system.

<hr>

#### Are you using the Anaconda installation?
{{% anchor "is-anaconda" %}}

If you have installed Python using the Anaconda installer, please make sure that you are using the `Anaconda Prompt`, `Anaconda Navigator` and
can run BornAgain scripts from the command line, as explained in 
[Install Python with the Anaconda installer]({{% relref "documentation/installation/windows/python-anaconda" %}}).

<hr>

#### Are you using a native Python installation?
{{% anchor "is-native-python" %}}

If you have installed Python manually using the installer from [Python.org](https://www.python.org/download), try to run it from the `Windows command prompt`, as explained in
[Manual Python installation]({{% relref "documentation/installation/windows/python-original" %}}).
