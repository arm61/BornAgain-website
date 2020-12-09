+++
title = "VSCode editor"
weight = 10
+++

## VSCode editor

In this tutorial we explain how to run BornAgain Python examples in a convenient manner using the `VSCode` editor.
This is a community driven, lightweighted and open-source editor from Microsoft, which provides code highlighting for many languages and
can be extremely handy in any kind of script-related and code-related activity.

At this point we assume that the user has already installed BornAgain and a Python distribution as explained in
[Python installation section]({{% relref "documentation/installation/windows/python-original" %}}).

### Download and install VSCode

Download the editor from [official website](https://code.visualstudio.com).

{{< figscg src="python-code-step0.PNG" class="center" width="450px" caption="Download the installer">}}

{{< figscg src="python-code-step1.PNG" class="center" width="450px" caption="Run the installer">}}


### Add the BornAgain examples to VSCode

Start `VSCode` and you will find yourself on the welcome screen.

Add the folder with the BornAgain Python examples to the workspace
by clicking `Add workspace folder` as shown in the screenshot below.

{{< figscg src="../../python-anaconda/anaconda-running-step5-vscode.PNG" class="center" width="450px">}}

Choose the directory with the BornAgain Python examples at `C:/BornAgain-{{< release-string >}}/Examples/python`.
If you open any example, `VSCode` will require you to configure the Python interpreter to use. In the screenshot below, `VSCode` is complaining 
that no Python interpreter was selected and also suggests to install the so-called `pylint` plugin for a better code development experience.

{{< figscg src="python-code-step2.PNG" class="center" width="450px">}}

Click on `Select Python Interpreter` and select the interpreter you have installed previously. Install `pylint` too.
On the screenshot below `VSCode` is fully configured and ready for work.

{{< figscg src="python-code-step3.PNG" class="center" width="450px">}}

Finally you can run an example using the right mouse button.

{{< figscg src="../../python-anaconda/anaconda-running-step7-vscode.PNG" class="center" width="450px">}}

The script will be executed in a terminal embedded in `VSCode` and a scattering image will appear on the screen after simulation has completed.

{{< figscg src="../../python-anaconda/anaconda-running-step8-vscode.PNG" class="center" width="450px">}}

Now you can try to run other BornAgain Python examples and start your exciting journey in Python scripting with BornAgain!

