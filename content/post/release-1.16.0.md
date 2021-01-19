+++
title = "New release of BornAgain: version 1.16"
date = "2019-08-01T8:30:10+02:00"
description = "BornAgain 1.16 has been released"
draft = false
comments = false
authors = ["pospelov"]
tags = ["Release"]
categories = ["News"]
+++

{{< alert theme="success" >}}
#### New release of BornAgain: version 1.16
{{< /alert >}}

We are glad to announce [BornAgain 1.16.0](https://www.bornagainproject.org/download/) release.

This release mostly extends the reflectometry support.
One of the main features available from now is access to
SLD/refractive index profile across sample layers, support for uncertainties in experimental data fitting and more resolution effects.

**Example highlights**

+ [Material SLD profile]({{% relref "documentation/examples/reflectometry/material-profile" %}})
+ [Material SLD profile with particles]({{% relref "documentation/examples/reflectometry/material-profile-with-particles" %}})
+ [Reflectometry fit with uncertanties]({{% relref "documentation/examples/fitting/extended/fit-with-uncertainties" %}})
+ [Beam divergence in reflectometry scan]({{% relref "documentation/examples/reflectometry/beam-full-divergence" %}})
+ [Resolution effects in TOF reflectometry]({{% relref "documentation/examples/reflectometry/tofr-with-resolution" %}})
+ [Angular divergence in reflectometry scan]({{% relref "documentation/examples/reflectometry/beam-angular-divergence" %}})

**API changes:**

* Python: major changes in SpecularSimulation interface. Please consult web-documentation for details.

**Other changes:**

* Support for arbitrary resolutions in reflectometry
* Importing reflectometry data as Qz-Intensity by default
* Numerous bug fixes
* Project back compatibility is broken

More details on our [issue tracker](http://apps.jcns.fz-juelich.de/redmine/versions/48).

As always, we very much welcome your comments and feedback!
